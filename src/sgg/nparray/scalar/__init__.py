"""
numpyのスカラー値に関するモジュール

参考
https://numpy.org/doc/stable/reference/arrays.scalars.html
"""

import numpy as np

from ..isdtype import boolDtype, floatDtype, intDtype, numberDtype, strDtype

__all__ = ["ScalarNum", "ScalarInt", "ScalarFloat", "ScalarStr", "ScalarBool"]


class ScalarNum:
    def __init__(self, val):
        if not np.isscalar(val) or not numberDtype(val):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarNum({self.__val})"

    def __int__(self):
        return int(self.__val)

    def __float__(self):
        return float(self.__val)


class ScalarInt:
    def __init__(self, val):
        if not np.isscalar(val) or not intDtype(val):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarInt({self.__val})"

    def __int__(self):
        return int(self.__val)

    def __float__(self):
        return float(self.__val)


class ScalarFloat:
    def __init__(self, val):
        if not np.isscalar(val) or not floatDtype(val):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarFloat({self.__val})"

    def __int__(self):
        return int(self.__val)

    def __float__(self):
        return float(self.__val)


class ScalarStr:
    def __init__(self, val):
        if not np.isscalar(val) or not strDtype(val):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarStr({self.__val})"

    def __str__(self):
        return str(self.__val)


class ScalarBool:
    def __init__(self, val):
        if not np.isscalar(val) or not boolDtype(val):
            raise TypeError
        self.__val = val

    def __repr__(self):
        return f"ScalarBool({self.__val})"

    def __bool__(self):
        return bool(self.__val)
