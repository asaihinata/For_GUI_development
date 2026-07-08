r"""
src\sgg\nparray内の例外メッセージのモジュール
"""

from numpy.exceptions import VisibleDeprecationWarning

from sgg.exceptions import *


class ShapeError(ValueError, IndexError):
    def __init__(self, shape):
        self.__shape = shape

    def __str__(self):
        return str(f"shape({self.__shape})が正しい値ではありません")


class NoScalarError(ValueError, IndexError):
    def __init__(self, element):
        self.__element = element

    def __str__(self):
        return str(f"{self.__element}はスカラー値ではありません")
