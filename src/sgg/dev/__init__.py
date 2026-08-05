from ._darray import *
from ._dnumber import *
from .color import parsecolor

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
