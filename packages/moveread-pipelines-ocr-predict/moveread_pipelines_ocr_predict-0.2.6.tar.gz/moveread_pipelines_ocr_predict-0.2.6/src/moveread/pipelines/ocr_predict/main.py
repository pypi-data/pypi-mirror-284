from typing import Unpack, TypeAlias, Sequence
import base64
import asyncio
from haskellian import iter as I, either as E, funcs as F
from kv import KV, ReadError as KVReadError
from pipeteer.queues import ReadQueue, WriteQueue, ReadError as QReadError
import tf.serving as tfs
from dslog import Logger
from .spec import Input, Preds

Err: TypeAlias = QReadError | KVReadError | tfs.PredictErr

@E.do[tfs.PredictErr]()
async def predict_batches(
  b64imgs: Sequence[Sequence[str]], *, id: str,
  logger: Logger, **params: Unpack[tfs.Params],
):
  results: Preds = []
  for i, batch in I.batch(8, b64imgs).enumerate():
    preds = (await tfs.multipredict(batch, **params)).unsafe()
    logger(f'"{id}": Batch {i}', level='DEBUG')
    results.extend(preds)

  return results

async def run(
  Qin: ReadQueue[Input],
  Qout: WriteQueue[Preds], *,
  blobs: KV[bytes],
  logger = Logger.rich().prefix('[OCR PREDS]'),
  **params: Unpack[tfs.Params]
):
  """Runs predections by reading task images as keys of `images`. Appends a `State` entry first, then all `Preds`"""
  
  @E.do[Err]()
  async def run_one():
    id, task = (await Qin.read()).unsafe()
    logger(f'Predicting "{id}"')
    
    imgs = await asyncio.gather(*[
      asyncio.gather(*[blobs.read(url).then(E.unsafe) for url in ply_urls])
      for ply_urls in task.ply_boxes
    ])
    b64imgs = I.ndmap(F.flow(base64.urlsafe_b64encode, bytes.decode), imgs)

    if task.endpoint:
      logger(f'Predicting with endpoint "{task.endpoint}"', level='DEBUG')
      custom_params = params | tfs.Params(endpoint=task.endpoint)
      res = await predict_batches(b64imgs, id=id, logger=logger, **custom_params)
      if res.tag == 'right':
        results = res.value
      else:
        logger(f'Failed to predict with endpoint "{task.endpoint}", fallbacking to default. Error:', res.value, level='WARNING')
        results = (await predict_batches(b64imgs, id=id, logger=logger, **params)).unsafe()
    else:
      results = (await predict_batches(b64imgs, id=id, logger=logger, **params)).unsafe()
    

    logger(f'Done predicting "{id}"')
    (await Qout.push(id, results)).unsafe()
    (await Qin.pop(id)).unsafe()
  
  while True: 
    try:
      res = await run_one()
      if res.tag == 'left':
        logger(f'Prediction error', res.value, level='ERROR')
        await asyncio.sleep(1)
      else:
        await asyncio.sleep(0) # release the loop
    except Exception as e:
      logger('Unexpected exception:', e, level='ERROR')
      await asyncio.sleep(1)