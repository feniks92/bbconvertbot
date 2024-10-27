from dataclasses import dataclass

from pybit.unified_trading import HTTP

from .Convert import ConvertHTTP


@dataclass
class BybitClient(HTTP, ConvertHTTP):
    def __init__(self, **args):
        super().__init__(**args)
