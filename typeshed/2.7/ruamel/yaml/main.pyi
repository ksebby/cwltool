# Stubs for ruamel.yaml.main (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, AnyStr, BinaryIO, IO, List, Tuple, Union
from ruamel.yaml.loader import *
import StringIO

VersionType = Union[List[int], str, Tuple[int, int]] 
StreamType = Union[BinaryIO, IO[str], StringIO.StringIO]

def load(stream: StreamType,
         Loader: Any =...,
         version: VersionType = None) -> Any: ...

def round_trip_load(stream: StreamType,
                    version: VersionType = None) -> Any: ...

def dump(data: Any) -> Any: ...

def round_trip_dump(data: Any) -> Any: ...
