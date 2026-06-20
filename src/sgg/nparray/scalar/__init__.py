"""
numpyのスカラー値に関するモジュール

参考
https://numpy.org/doc/stable/reference/arrays.scalars.html
"""

import numpy as np

__all__ = ["ScalarStr", "ScalarStr", "ScalarBool"]


class ScalarNum:
    def __init__(self, val):
        if isinstance(val, int | float):
            pass
        elif not np.isscalar(val) or not np.issubdtype(val, np.number):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarNum({self.__val})"

    def __int__(self):
        return int(self.__val)

    def __float__(self):
        return float(self.__val)


class ScalarStr:
    def __init__(self, val):
        if isinstance(val, str):
            pass
        elif not np.isscalar(val) or not np.issubdtype(val, np.character):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarStr({self.__val})"

    def __str__(self):
        return str(self.__val)


class ScalarBool:
    def __init__(self, val):
        if isinstance(val, bool):
            pass
        elif not np.isscalar(val) or not np.issubdtype(val, np.bool_):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarBool({self.__val})"

    def __bool__(self):
        return bool(self.__val)
