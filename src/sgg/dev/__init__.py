import numpy as np

from .color import parsecolor
from .common._darray import *
from .common._dnumber import *

__all__ = [
    "_flatten",
    "bols",
    "change_array_like",
    "int0",
    "int0s",
    "int1s",
    "ints",
    "intsmin",
    "is_array_like",
    "list2int",
    "list2num",
    "list4float",
    "listchose",
    "num0",
    "num0s",
    "num1s",
    "nums",
    "parsecolor",
    "range_num",
    "tonparray",
]


def bols(j, o=True):
    if isinstance(j, bool) or (
        isinstance(j, np.generic) and np.issubdtype(j, np.bool | np.bool_)
    ):
        return j
    return o


def _flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list | tuple):
            result.extend(_flatten(item))
        else:
            result.append(item)
    return result
