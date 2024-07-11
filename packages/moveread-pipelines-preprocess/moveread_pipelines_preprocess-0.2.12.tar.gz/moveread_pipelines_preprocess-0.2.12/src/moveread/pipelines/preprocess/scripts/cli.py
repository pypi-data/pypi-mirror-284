from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument('-q', '--queues', required=True)
  parser.add_argument('--images', required=True)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)

  args = parser.parse_args()

  import os
  from dslog import Logger
  queues_path = os.path.join(os.getcwd(), args.queues)
  images_path = os.path.join(os.getcwd(), args.images)
  
  logger = Logger.click().prefix('[PREPROCESS]')
  logger(f'Running preprocessing...')
  logger(f'Images path: "{images_path}"')
  logger(f'Queues path: "{queues_path}"')
  
  from typing import Sequence
  import asyncio
  from functools import cache
  from multiprocessing import Process
  from kv import FilesystemKV
  import uvicorn
  from fastapi.middleware.cors import CORSMiddleware
  from pipeteer import QueueKV
  from moveread.pipelines.preprocess import Preprocess, Output

  @cache
  def get_queue(path: Sequence[str], type: type):
    return QueueKV.sqlite(type, queues_path, table='-'.join(path))
  
  blobs = FilesystemKV[bytes](images_path)
  Qout = get_queue(('output',), Output)

  wkf = Preprocess()
  params = Preprocess.Params(logger=logger, blobs=blobs, images_path=images_path)
  Qs = wkf.connect(Qout, get_queue, params)
  artifacts = wkf.run(Qs, params)
  artifacts.api.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

  ps = {
    id: Process(target=asyncio.run, args=(f,)) for id, f in artifacts.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifacts.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()

if __name__ == '__main__':
  import sys
  import os
  os.chdir('/home/m4rs/mr-github/rnd/dfy-pipeline/preprocess/dev/demo')
  sys.argv.extend('-q queues.sqlite --images images'.split(' '))
  main()