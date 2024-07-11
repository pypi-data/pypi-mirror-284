import os
from argparse import ArgumentParser

def env(variable: str, *, default = None, required: bool = True) -> dict:
  if (value := os.getenv(variable, default)) is not None:
    return dict(default=value)
  return dict(required=required)

def main():
  parser = ArgumentParser(description='DFY Puller')
  parser.add_argument('--sql', **env('SQL_CONN_STR'), help='SQL connection string')
  parser.add_argument('--blob', **env('BLOB_CONN_STR'), help='DFY Blobs connection string')
  parser.add_argument('--pipeline', **env('PIPELINE_ENDPOINT'), help='Pipeline endpoint')
  parser.add_argument('--token', **env('PIPELINE_TOKEN'), help='Pipeline token')

  parser.add_argument('--interval', **env('PULL_INTERVAL', default=60), type=int, help='Interval between pulls')

  args = parser.parse_args()
  endpoint = args.pipeline.rstrip('/')

  from dslog import Logger
  logger = Logger.click().prefix('[PULLER]')
  logger(f'Starting puller...')
  logger(f'- Endpoint: {args.pipeline}')
  logger(f'- Interval: {args.interval}s')

  import asyncio
  from kv import KV, ClientKV
  from sqlmodel import create_engine
  from pipeteer import http
  from moveread.pipelines.dfy import DFYPipeline
  from moveread.dfy_connector import Puller

  HEADERS = { 'Authorization': f'Bearer {args.token}' }
  req = http.bound_request(headers=HEADERS)
  pipe = DFYPipeline()
  Qpush, *_ = http.clients(pipe, f'{endpoint}/queues', request=req)
  blobs = ClientKV(f'{endpoint}/blobs', request=req)
  online_blobs = KV.of(args.blob)
  engine = create_engine(args.sql)

  puller = Puller(Qpush=Qpush, pipeline_blobs=blobs, dfy_blobs=online_blobs, logger=logger)
  asyncio.run(puller.loop(engine, args.interval))

if __name__ == '__main__':
  print('Executing as main')
  from dotenv import load_dotenv
  load_dotenv()
  main()