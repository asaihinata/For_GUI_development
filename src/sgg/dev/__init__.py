import numpy as np

from .color import parsecolor
from .common._darray import *
from .common._dnumber import *

__all__ = [
    "_flatten",
    "_is_str",
    "_SET_OBJ",
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


class _SET_OBJ:
    def _to_str(self, s):
        if isinstance(s, str):
            return s
        if isinstance(s, np.str_):
            return str(s)

    def _is_number(self, val):
        if isinstance(val, int | float | complex) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.number)
        ):
            return True
        return False

    def _is_real(self, val):
        if isinstance(val, int | float) or (
            isinstance(val, np.generic)
            and np.issubdtype(val.dtype, np.integer | np.floating)
        ):
            return True
        return False

    def _to_real(self, val):
        if isinstance(val, int | float):
            return val
        elif isinstance(val, np.generic):
            if np.issubdtype(val.dtype, np.integer):
                return int(val)
            elif np.issubdtype(val.dtype, np.floating):
                return float(val)
            raise TypeError
        raise TypeError

    def _to_str_flat_list(self, array):
        if isinstance(array, list | tuple):
            return _flatten(array)
        elif isinstance(array, range):
            return list(array)
        elif isinstance(array, np.ndarray) and array.dtype.kind == "U":
            return array.ravel().tolist()
        elif isinstance(array, str):
            return [array]
        elif isinstance(array, np.str_):
            return [str(array)]
        raise TypeError(f"{array}には文字列のみが入った配列を指定してください")

    def _to_number(self, val):
        if isinstance(val, int | np.integer):
            return int(val)
        elif isinstance(val, float | np.floating):
            return float(val)
        elif isinstance(val, complex | np.complexfloating):
            return complex(val)

    def _is_number(self, val):
        if isinstance(val, int | float | complex) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.number)
        ):
            return True
        return False

    def _to_flat_list(self, array):
        if np.isscalar(array):
            return [array]
        elif isinstance(array, list | tuple):
            return _flatten(array)
        elif isinstance(array, range):
            return list(array)
        elif isinstance(array, np.ndarray):
            return array.ravel().tolist()
