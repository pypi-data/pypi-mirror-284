import functools
import operator
from typing import TypeVar, Iterable

_T = TypeVar("_T")
_V = TypeVar("_V")


def flatten(the_list: Iterable[Iterable[_T]]) -> list[_T]:
    return functools.reduce(operator.iconcat, the_list, [])
