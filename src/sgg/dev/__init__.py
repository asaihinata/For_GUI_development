from .color import parsecolor
from .common._darray import *
from .common._dnumber import *

__all__ = [
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
    if isinstance(j, bool):
        return j
    return o


def bol(vals, other=False):
    if isinstance(vals, bool):
        return vals
    return other
