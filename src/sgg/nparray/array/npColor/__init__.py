"""
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,redやgreenなどのカラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
"""

from re import compile, findall

from matplotlib.colors import to_hex, to_rgb, to_rgba
from numpy import array, fromiter, nditer, uint8

from ..nparray import NPArray, is_array_like
from ._data import Get_color

__all__ = ["NPColor"]
_HEX6_RE = compile(r"^#[0-9a-f]{6}$")
_HEX3_RE = compile(r"^#[0-9a-f]{3}$")
_RGB_RE = compile(r"^rgb\((\d+),(\d+),(\d+)\)$")
_HSV_RE = compile(r"^hsv\((\d+),(\d+),(\d+)\)$")


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
        colors = _check(color)
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


def _check(name):
    if name[0] == "#":
        if _HEX6_RE.match(name):
            val = findall(_HEX6_RE, name)[0][1:]
            return fromiter(
                (int(val[i : i + 2], 16) for i in range(0, len(val), 2)), dtype=uint8
            )
        if _HEX3_RE.match(name):

            def sets(t):
                return f"{t}{t}"

            val = findall(_HEX3_RE, name)[0][1:]
            return fromiter(
                (int(sets(val[i : i + 1]), 16) for i in range(0, len(val))), dtype=uint8
            )
    if _RGB_RE.match(name):
        return array(findall(_RGB_RE, name)[0], dtype=uint8)
    if _HSV_RE.match(name):
        return array(findall(_HSV_RE, name)[0], dtype=uint8)
