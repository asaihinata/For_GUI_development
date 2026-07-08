"""マーカーを設定するモジュール"""

import numpy as np
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

from sgg.nparray import NPArray

__all__ = ["Marker", "MarkerList"]


class Marker:
    marker_list = [
        ".",
        ",",
        "o",
        "v",
        "^",
        "<",
        ">",
        "1",
        "2",
        "3",
        "4",
        "8",
        "s",
        "p",
        "*",
        "h",
        "H",
        "+",
        "x",
        "D",
        "d",
        "|",
        "_",
        "P",
        "X",
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        "None",
        "none",
        " ",
        "",
    ]

    def __init__(self, marker, fill=None, cap=None, transform=None, join=None):
        if fill not in ["full", "left", "right", "bottom", "top", "none"]:
            fill = "none"
        if cap not in ["butt", "round", "projecting"]:
            cap = None
        if join not in ["miter", "round", "bevel"]:
            join = None
        if isinstance(transform, np.number):
            transform = float(transform)
        else:
            transform = 0
        self.marker = MarkerStyle(
            marker,
            fillstyle=fill,
            transform=Affine2D().rotate_deg(transform),
            joinstyle=join,
            capstyle=cap,
        )

    def __contains__(self, value):
        return value in self.marker_list


class MarkerList(NPArray):
    def __new__(cls, marker, fill=None, cap=None, transform=None, join=None):
        marker = [marker] if isinstance(marker, str | int) else marker
        return super().__new__(
            cls,
            [Marker(i, fill, cap, transform, join).marker for i in marker],
            dtype=MarkerStyle,
            max_ndim=1,
        )

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, val):
        return super().__getitem__(val)

    def __str__(self):
        return str(self.data[0])

    def __repr__(self):
        return f"MarkerList({self.data})"
