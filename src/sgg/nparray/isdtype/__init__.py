"""numpyのdtypeに関するモジュール"""

import numpy as np

__all__ = [
    "booldDtype",
    "complexdDtype",
    "floatdDtype",
    "intdDtype",
    "integerdDtype",
    "numberdDtype",
    "strdDtype",
    "uintdDtype",
    "boolDtype",
    "complexDtype",
    "floatDtype",
    "intDtype",
    "integerDtype",
    "numberDtype",
    "strDtype",
    "uintDtype",
]


def booldDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.bool_)
    return isinstance(obj, bool | np.bool_)


def boolDtype(obj):
    return isinstance(obj, bool | np.bool_)


def complexdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.complexfloating)
    return isinstance(obj, complex | np.complexfloating)


def complexDtype(obj):
    return isinstance(obj, complex | np.complexfloating)


def floatdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.floating)
    return isinstance(obj, float | np.floating)


def floatDtype(obj):
    return isinstance(obj, float | np.floating)


def intdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.complexfloating)
    return isinstance(obj, int | np.int8 | np.int16 | np.int32 | np.int64)


def intDtype(obj):
    return isinstance(obj, int | np.int8 | np.int16 | np.int32 | np.int64)


def integerdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.complexfloating)
    return isinstance(obj, int | np.integer)


def integerDtype(obj):
    return isinstance(obj, int | np.integer)


def numberdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.number)
    return isinstance(obj, int | float | complex | np.number)


def numberDtype(obj):
    return isinstance(obj, int | float | complex | np.number)


def uintdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.uint8 | np.uint16 | np.uint32 | np.uint64)
    return isinstance(obj, int | np.uint8 | np.uint16 | np.uint32 | np.uint64)


def uintDtype(obj):
    return isinstance(obj, int | np.uint8 | np.uint16 | np.uint32 | np.uint64)


def strdDtype(obj):
    if isinstance(obj, np.ndarray):
        return np.issubdtype(obj.dtype, np.character | np.str_ | np.bytes_)
    return isinstance(obj, str | np.character | np.str_ | np.bytes_)


def strDtype(obj):
    return isinstance(obj, str | np.character | np.str_ | np.bytes_)
