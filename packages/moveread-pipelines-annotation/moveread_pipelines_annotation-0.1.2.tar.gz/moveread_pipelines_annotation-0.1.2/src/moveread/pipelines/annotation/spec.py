from typing import Sequence, TypedDict, NotRequired, Literal
from dataclasses import dataclass
from pipeteer import Task
from fastapi import FastAPI
from dslog import Logger
from moveread.core import Player

def url_join(a: str, b: str):
  return a.rstrip('/') + '/' + b.lstrip('/')

@dataclass
class Input:
  title: str
  boxes: Sequence[str]
  pgn: Sequence[str]

@dataclass
class Item(Input):
  id: str

  @staticmethod
  def at_url(url: str):
    def bound(entry: tuple[str, Input]):
      id, input = entry
      boxes = [url_join(url, box) for box in input.boxes]
      return Item(boxes=boxes, pgn=input.pgn, id=id, title=input.title)
    return bound

@dataclass
class Ok:
  meta: Player.Meta
  tag: Literal['ok'] = 'ok'

@dataclass
class Repreprocess:
  tag: Literal['repreprocess'] = 'repreprocess'

Output = Ok | Repreprocess

class Params(TypedDict):
  logger: NotRequired[Logger]
  images_path: NotRequired[str|None]

class Annotation(Task[Input, Output, Params, FastAPI]):
  Input = Input
  Output = Output
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = FastAPI

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Queues, params: Params) -> FastAPI:
    from .sdk import AnnotationSDK
    from ._api import api
    return api(AnnotationSDK(**queues), **params)