from argparse import ArgumentParser

def main():

  parser = ArgumentParser()
  parser.add_argument('-b', '--base-path', required=True)

  parser.add_argument('-p', '--port', type=int, default=8000)
  parser.add_argument('--host', default='0.0.0.0')
  parser.add_argument('--cors', default=['*'], nargs='*', type=str, help='CORS allowed origins')

  args = parser.parse_args()

  import os
  from dslog import Logger

  base_path = os.path.abspath(args.base_path)
  logger = Logger.click().prefix('[ANNOTATION]')
  logger(f'Running annotation pipeline at "{base_path}"...')

  import asyncio
  from multiprocessing import Process
  from pipeteer import http
  import kv.rest
  import uvicorn
  from fastapi.middleware.cors import CORSMiddleware
  from moveread.pipelines.annotation.preprocessed import PreprocessedAnnotation, local_storage, queue_factory

  pipe = PreprocessedAnnotation()

  queues_path = os.path.join(base_path, 'queues.sqlite')
  get_queue = queue_factory(queues_path)
  storage = local_storage(base_path)
  params = PreprocessedAnnotation.Params(logger=logger, **storage)

  Qout = get_queue(('output',), PreprocessedAnnotation.Output)
  Qs = pipe.connect(Qout, get_queue, params)

  artifs = pipe.run(Qs, params)
  artifs.api.mount('/queues', http.mount(pipe, Qout, get_queue, params))
  artifs.api.mount('/blobs', kv.rest.api(storage['blobs']))

  artifs.api.add_middleware(CORSMiddleware, allow_origins=args.cors, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

  ps = {
    id: Process(target=asyncio.run, args=(f,))
    for id, f in artifs.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifs.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()


if __name__ == '__main__':
  # import debugpy
  # debugpy.listen(("0.0.0.0", 5678))
  # print("Waiting for debugger attach...")
  # debugpy.wait_for_client()
  # print("Debugger attached")

  import os
  import sys

  os.chdir('/home/m4rs/mr-github/rnd/annotation/annotation/dev/full-demo')
  sys.argv.extend(['-b', '.'])
  main()