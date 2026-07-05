import numpy as np

__all__ = ["_arrisuint", "is_array_like", "change_array_like"]


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
