from ..nparray.isdtype import boolDtype
from ._darray import *
from ._dnumber import *
from .color import Color, parsecolor

__all__ = [
    "Color",
    "allNone",
    "allNones",
    "args",
    "bols",
    "int0",
    "int0s",
    "int1s",
    "ints",
    "intsmin",
    "list2float",
    "list2int",
    "list2num",
    "list4float",
    "list4int",
    "list4num",
    "listchose",
    "num0",
    "num0s",
    "num1s",
    "nums",
    "numsmin",
    "parsecolor",
    "range_num",
    "is_array_like",
    "change_array_like",
]


def args(*args, data=None, x=None, y=None):
    lens = len(args)
    if lens == 1:
        data = args[0]
    elif lens == 2:
        x, y = args[0], args[1]
    elif lens > 2:
        raise ValueError("argsは最大2つまで指定してください")
    if (data is not None and (x is not None or y is not None)) or (
        data is None and (x is None or y is None)
    ):
        raise ValueError("組み合わせが不正です")
    return (data, x, y)


def bols(j, o=True):
    if boolDtype(j):
        return bool(j)
    return o
