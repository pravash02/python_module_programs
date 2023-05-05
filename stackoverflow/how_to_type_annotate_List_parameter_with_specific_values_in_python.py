from typing import List
from enum import Enum


class HelloWorld(Enum):
    _hello = "hello"
    _world = "world"


def foo(bar: List[HelloWorld]):
    assert all(b in [HelloWorld._hello, HelloWorld._world] for b in bar)


foo(["hello", HelloWorld._world])
