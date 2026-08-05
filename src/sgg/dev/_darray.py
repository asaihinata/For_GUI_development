import numpy as np

__all__ = [
    "allNone",
    "allNones",
    "change_array_like",
    "is_array_like",
    "list2float",
    "list2int",
    "list2num",
    "list4float",
    "list4int",
    "list4num",
    "listchose",
    "tonparray",
]


def tonparray(data, *, ndmin=0, ndmax=0):
    if isinstance(data, list | tuple | range):
        kwargs = {}
        if ndmin:
            kwargs["ndmin"] = ndmin
        if ndmax:
            kwargs["ndmax"] = ndmax
        return np.array(data, **kwargs)
    elif not isinstance(data, np.ndarray) and hasattr(data, "__array__"):
        data = data.__array__()
        l = data.ndim
        if l < 1 or (0 < ndmin and l < ndmin) or (0 < ndmax and ndmax < l):
            raise TypeError
        return data
    elif isinstance(data, np.ndarray):
        l = data.ndim
        if l < 1 or (0 < ndmin and l < ndmin) or (0 < ndmax and ndmax < l):
            raise TypeError
        return data
    raise TypeError


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
