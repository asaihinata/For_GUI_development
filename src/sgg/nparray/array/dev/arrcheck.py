import numpy as np

from ..exceptions import *

__all__ = [
    "_arrisuint",
    "is_array_like",
    "change_array_like",
    "_uint_check",
    "_scalar_check",
    "_intarraylike_check",
]


def _scalar_check(element):
    return np.isscalar(element)


def _uint_check(value):
    if _scalar_check(value):
        raise NoScalarError(value)
    if not _intarraylike_check(value):
        raise UIntError(value)


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
        except (ValueError, TypeError):
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
