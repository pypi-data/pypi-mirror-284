from argparse import ArgumentParser


def main():

  parser = ArgumentParser()
  parser.add_argument('-i', '--input', required=True)
  parser.add_argument('-o', '--output', required=True)
  parser.add_argument('-b', '--blobs')

  parser.add_argument('-p', '--port', type=int, default=8000)
  parser.add_argument('--host', default='0.0.0.0')

  args = parser.parse_args()

  from dslog import Logger
  logger = Logger.click().prefix('[ANNOTATION]')
  logger('Starting annotation pipeline...')
  logger('- Input:', args.input)
  logger('- Output:', args.output)

  from pipeteer import QueueKV
  import uvicorn
  from fastapi.middleware.cors import CORSMiddleware
  from moveread.pipelines.annotation import Annotation

  task = Annotation()
  Qin = QueueKV.sqlite(Annotation.Input, args.input)
  Qout = QueueKV.sqlite(Annotation.Output, args.output)

  api = task.run({'Qin': Qin, 'Qout': Qout}, {'logger': logger, 'images_path': args.blobs})
  api.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
  uvicorn.run(api, host=args.host, port=args.port)

if __name__ == '__main__':
  print('What the fuck vscode')
  main()