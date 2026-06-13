"""
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,カラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
"""

from matplotlib.colors import to_hex, to_rgb, to_rgba
from numpy import array, nditer

from ..npArray import NPArray, is_array_like
from ._color_check import check
from .data import Get_color

__all__ = ["NPColor"]


class NPColor(NPArray):
    def __init__(self, color):
        if isinstance(color, str):
            super().__init__([self.__get_val(color)], depth_limit=1)
        elif is_array_like(color):
            super().__init__(
                [self.__get_val(str(i)) for i in nditer(array(color))], depth_limit=1
            )
        else:
            raise TypeError("colorの値が不正です")

    def __repr__(self):
        return f"NPColor({self.data})"

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.get(key)

    def __get_val(self, color):
        colorname = Get_color.gets(color)
        if colorname is not None:
            return colorname[1]
        colors = check(color)
        if colors is not None:
            return to_hex(colors / 255)
        raise ValueError("値が不正です")

    def tohex(self):
        self.data = array([to_hex(i) for i in self.data])
        return self

    def torgba(self):
        self.data = array([to_rgba(i, alpha=1) for i in self.data])
        return self

    def torgb(self):
        self.data = array([to_rgb(i) for i in self.data])
        return self
