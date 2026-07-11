import numpy as np

from sgg.exceptions import *

__all__ = [
    "_arrisuint",
    "_int_co_check",
    "_intarraylike_check",
    "_scalar_check",
    "change_array_like",
    "is_array_like",
]


def _int_co_check(obj):
    obj = np.asanyarray(obj)
    if not np.issubdtype(obj.dtype, np.integer):
        raise TypeError(f"{obj.dtype}には整数型を指定してください")


def _scalar_check(element):
    return np.isscalar(element)


def _intarraylike_check(obj):
    try:
        arr = np.asarray(obj)
    except Exception:
        return False
    if arr.dtype.kind in "iub":
        return True
    if arr.dtype.kind == "f":
        return arr.size > 0 and np.all(np.mod(arr, 1) == 0) and np.all(np.isfinite(arr))
    if arr.dtype.kind == "O":
        try:
            arr.astype(np.int64)
            return True
        except ValueError, TypeError:
            return False
    return False


def _arrisuint(arr):
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)
    if np.issubdtype(arr.dtype, np.integer):
        return np.all(arr > 0) and np.all(np.equal(np.mod(arr, 1), 0))
    else:
        return False


def is_array_like(obj):
    if isinstance(obj, np.ndarray | list | tuple | range):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


def change_array_like(obj):
    if isinstance(obj, np.ndarray | list | tuple | range):
        return True
    elif np.isscalar(obj):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False
