from pathlib import Path

from numpy import where

from ...nparray import NPColor
from ...readfile import Getcsv

__all__ = ["Color", "parsecolor"]


class Color:
    def __init__(self, color):
        colors = _gets(color)
        self.__color = NPColor(color)[0] if colors is None else f"#{colors[1]}"

    def __repr__(self):
        return f"Color({self.__color})"

    def __str__(self):
        return str(self.__color)

    @property
    def color(self):
        return str(self.__color)


def _gets(colorname):
    cds = Getcsv(Path(__file__).parent / "color.csv").get_numpy()
    c, _ = where(colorname == cds)
    if c.size == 0:
        return None
    return cds[c][0]


def parsecolor(val, other=None):
    if val is None:
        return other
    return Color(val).color
