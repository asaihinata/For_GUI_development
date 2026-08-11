import numpy as np

__all__ = [
    "change_array_like",
    "is_array_like",
    "list2int",
    "list2num",
    "list4float",
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
        result = np.array(data, **kwargs)
    elif hasattr(data, "__array__"):
        data = data.__array__()
        l = data.ndim
        if l < 1 or (0 < ndmin and l < ndmin) or (0 < ndmax and ndmax < l):
            raise TypeError
        result = data
    elif isinstance(data, np.ndarray):
        l = data.ndim
        if l < 1 or (0 < ndmin and l < ndmin) or (0 < ndmax and ndmax < l):
            raise TypeError
        result = data
    else:
        raise TypeError
    if isinstance(result,np.ndarray) and result.dtype.kind=="M":
        return np.datetime_as_string(result)
    return result

def is_array_like(obj):
    if (isinstance(obj, np.ndarray) and 1 <= obj.ndim) or isinstance(
        obj, list | tuple | range
    ):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


def change_array_like(obj):
    if (isinstance(obj, np.ndarray) and 1 <= obj.ndim) or isinstance(
        obj, list | tuple | range
    ):
        return True
    elif np.isscalar(obj):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


def list2num(lin=None):
    if change_array_like(lin):
        arr = np.asanyarray(lin)
        if np.issubdtype(arr.dtype, np.number) and arr.shape == (2,):
            return True
    return False


def list2int(lin=None):
    if change_array_like(lin):
        arr = np.asanyarray(lin)
        if np.issubdtype(arr.dtype, np.integer) and arr.shape == (2,):
            return True
    return False


def list4float(lin=None):
    if change_array_like(lin):
        arr = np.asanyarray(lin)
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
