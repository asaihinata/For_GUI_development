"""マーカーを設定するモジュール"""

import numpy as np
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

__all__ = ["Marker"]


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
