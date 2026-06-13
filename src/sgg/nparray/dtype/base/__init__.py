"""numpyのdtypeに関するモジュール"""

from numpy import issubdtype, ndarray

__all__ = ["baseDtype"]


class baseDtype:
    def __init__(self, arr, dtype):
        dt = arr.dtype if isinstance(arr, ndarray) else arr
        self.__bols = (
            any(issubdtype(dt, i) for i in dtype)
            if isinstance(dtype, list)
            else issubdtype(dt, dtype)
        )

    def __bool__(self):
        return self.__bols

    @property
    def judge(self):
        return self.__bols
