"""numpyのdtypeに関するモジュール"""

import numpy as np

__all__ = [
    "boolDtype",
    "complexDtype",
    "floatDtype",
    "intDtype",
    "integerDtype",
    "numberDtype",
    "strDtype",
    "uintDtype",
]


def boolDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, bool | np.bool_)


def complexDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, complex | np.complexfloating)


def floatDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, float | np.floating)


def intDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, int | np.int8 | np.int16 | np.int32 | np.int64)


def integerDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, int | np.integer)


def numberDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, int | float | complex | np.number)


def uintDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, int | np.uint8 | np.uint16 | np.uint32 | np.uint64)


def strDtype(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.dtype
    return isinstance(obj, str | np.character)
