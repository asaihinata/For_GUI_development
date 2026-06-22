import numpy as np

__all__ = [
    "allNone",
    "allNones",
    "list2num",
    "list2int",
    "list2float",
    "list4num",
    "list4int",
    "list4float",
    "listchose",
    "is_array_like",
    "change_array_like",
]


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


def allNone(a, b=None):
    return True if a is None and b is None else False


def allNones(a, b=None, other=None):
    if (a is not None and b is not None) or (a is not None and b is None):
        return a
    elif a is None and b is not None:
        return b
    return other


def list2num(lin=None):
    if change_array_like(lin):
        arr = np.array(lin)
        if np.issubdtype(arr.dtype, np.number) and arr.shape == (2,):
            return True
    return False


def list2int(lin=None):
    if change_array_like(lin):
        arr = np.array(lin)
        if np.issubdtype(arr.dtype, np.integer) and arr.shape == (2,):
            return True
    return False


def list2float(lin=None):
    if change_array_like(lin):
        arr = np.array(lin)
        if np.issubdtype(arr.dtype, np.floating) and arr.shape == (2,):
            return True
    return False


def list4num(lin=None):
    if change_array_like(lin):
        arr = np.array(lin)
        if np.issubdtype(arr.dtype, np.number) and arr.shape == (4,):
            return True
    return False


def list4int(lin=None):
    if change_array_like(lin):
        arr = np.array(lin)
        if np.issubdtype(arr.dtype, np.integer) and arr.shape == (4,):
            return True
    return False


def list4float(lin=None):
    if change_array_like(lin):
        arr = np.array(lin)
        if np.issubdtype(arr.dtype, np.floating) and arr.shape == (4,):
            return True
    return False


def listchose(val, arr, other=None):
    if isinstance(arr, tuple | list) and other == None:
        other = arr[0]
    elif not isinstance(arr, tuple | list) and other == None:
        other = arr
    if val in arr:
        return val
    return other
