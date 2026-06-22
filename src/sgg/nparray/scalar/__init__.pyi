"""
numpyのスカラー値に関するモジュール

参考
https://numpy.org/doc/stable/reference/arrays.scalars.html
"""

import numpy as np

__all__ = ["ScalarNum", "ScalarInt", "ScalarFloat", "ScalarStr", "ScalarBool"]

class ScalarNum:
    def __init__(self, val: int | float | np.number) -> None:
        """数値型全般に関するオブジェクト

        :param val: 値を指定する
        :type val: int | float | np.number
        """

    def __repr__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...

class ScalarInt:
    def __init__(self, val: int | np.integer) -> None:
        """整数の型に関するオブジェクト

        :param val: 値を指定する
        :type val: int | np.integer
        """

    def __repr__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...

class ScalarFloat:
    def __init__(self, val: float | np.floating) -> None:
        """浮動小数点数の型に関するオブジェクト

        :param val: 値を指定する
        :type val: float | np.floating
        """

    def __repr__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...

class ScalarStr:
    def __init__(self, val: str | np.character) -> None:
        """文字列型に関するオブジェクト

        :param val: 値を指定する
        :type val: str | np.character
        """

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class ScalarBool:
    def __init__(self, val: bool | np.bool_) -> None:
        """真偽型に関するオブジェクト

        :param val: 値を指定する
        :type val: bool | np.bool_
        """

    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
