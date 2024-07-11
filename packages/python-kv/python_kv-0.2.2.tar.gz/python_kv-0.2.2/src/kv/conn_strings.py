from typing_extensions import TypeVar, overload
from urllib.parse import urlparse, parse_qs, unquote
from pydantic import BaseModel, ConfigDict
from kv import KV

T = TypeVar('T')

class Params(BaseModel):
  model_config = ConfigDict(extra='forbid')
  prefix: str | None = None

class HTTPParams(Params):
  token: str | None = None

class AzureBlobParams(Params):
  container: str | None = None

class SQLParams(Params):
  table: str

@overload
def parse(conn_str: str) -> KV[bytes]:
  ...
@overload
def parse(conn_str: str, type: type[T] | None = None) -> KV[T]:
  ...
def parse(conn_str: str, type: type[T] | None = None):
  parsed_url = urlparse(conn_str) # 'file://path/to/base?prefix=hello'
  scheme = parsed_url.scheme # 'file'
  netloc = parsed_url.netloc # 'path'
  path = unquote(parsed_url.path) # '/to/base'
  endpoint = netloc + path # 'path/to/base'
  query = parse_qs(parsed_url.query) # { 'prefix': ['hello'] }
  query = { k: v[0] for k, v in query.items() }

  if scheme in ('http', 'https'):
    params = HTTPParams(**query)
    from kv.http import ClientKV
    url = f'{scheme}://{endpoint}'
    kv = ClientKV.new(url, type, token=params.token)

  elif scheme == 'azure+blob':
    params = AzureBlobParams(**query)
    from kv.azure import BlobKV, BlobContainerKV
    if params.container:
      kv = BlobContainerKV.from_conn_str(endpoint, params.container, type)
    else:
      kv = BlobKV.from_conn_str(endpoint, type)

  elif scheme == 'sqlite':
    params = SQLParams(**query)
    from kv import SQLiteKV
    kv = SQLiteKV.at(endpoint, type, table=params.table)

  elif scheme.startswith('sql+'):
    params = SQLParams(**query)
    from kv import SQLKV
    proto = scheme.removeprefix('sql+')
    url = f'{proto}://{endpoint}'
    kv = SQLKV.new(url, type, table=params.table)

  elif scheme == 'file':
    params = Params(**query)
    from kv import FilesystemKV
    kv = FilesystemKV.new(endpoint, type)

  elif scheme.startswith('redis'):
    params = Params(**query)
    if scheme.startswith('redis+'):
      scheme = scheme.removeprefix('redis+')
    url = f'{scheme}://{endpoint}'
    from kv import RedisKV
    kv = RedisKV.from_url(url, type)

  else:
    raise ValueError(f'Unknown scheme: {scheme}')
  
  return kv.prefixed(params.prefix) if params.prefix else kv