from re import compile, findall

import numpy as np
from matplotlib.colors import to_hex
from numpy import array, fromiter, nditer, uint8, where

from ._color import COLOR_LIST

__all__ = ["Color", "parsecolor"]
cds = np.array(COLOR_LIST)
_HEX6_RE = compile(r"^#[0-9a-f]{6}$")
_HEX3_RE = compile(r"^#[0-9a-f]{3}$")
_RGB_RE = compile(r"^rgb\((\d+),(\d+),(\d+)\)$")
_HSV_RE = compile(r"^hsv\((\d+),(\d+),(\d+)\)$")


def is_array_like(obj):
    if isinstance(obj, np.ndarray | list | tuple | range):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


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


class Color:
    def __init__(self, color):
        if isinstance(color, str):
            self.colors = self.__get_val(color)
        elif is_array_like(color):
            self.colors = [self.__get_val(str(i)) for i in nditer(array(color))]
        else:
            raise TypeError("colorの値が不正です")

    @classmethod
    def __get_val(cls, color):
        colorname = _gets(color)
        if colorname is not None:
            return colorname[1]
        colors = _check(color)
        if colors is not None:
            return to_hex(colors / 255)
        raise ValueError("値が不正です")

    def __repr__(self):
        return f"Color({self.colors})"

    def __str__(self):
        return str(self.colors)

    @property
    def color(self):
        return str(self.colors)


def _gets(colorname):
    c, _ = where(colorname == cds)
    if c.size == 0:
        return None
    return cds[c][0]


def parsecolor(val, other=None):
    if val is None:
        return other
    return Color(val).color
