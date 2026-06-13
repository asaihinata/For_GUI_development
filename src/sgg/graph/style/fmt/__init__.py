"""マーカー,線種,色を一度に設定するモジュール"""

import numpy as np

from ....nparray import NPString

__all__ = ["FMT", "fmtstyle", "FMTLineList", "FMTColorList", "FMTMarkList"]
FMT_COLOR = ["b", "g", "r", "c", "m", "y", "k", "w"]
FMT_MARKER = [
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
    "P",
    "*",
    "h",
    "H",
    "+",
    "x",
    "X",
    "D",
    "d",
    "|",
    "_",
]
FMT_SOLID = ["-", "--", "-.", ":"]


class FMT:
    def __init__(self, marker=None, solid=None, color=None):
        self.__txt = f"{marker if marker in FMT_MARKER else ''}{solid if solid in FMT_SOLID else ''}{color if color in FMT_COLOR else ''}"

    def __str__(self):
        return self.__txt

    @property
    def txt(self):
        return self.__txt


class fmtstyle:
    def __init__(self, arr, style="color"):
        style = style.lower()
        if style == "marker":
            style = FMT_MARKER
        elif style == "solid":
            style = FMT_SOLID
        else:
            style = FMT_COLOR
        if isinstance(arr, str):
            self.__arr = np.array([arr])
        elif isinstance(arr, list | tuple):
            self.__arr = np.array(arr)
        else:
            self.__arr = arr
        self.__arr = np.array([i if i in style else "" for i in np.nditer(self.__arr)])

    def __iter__(self):
        return iter(self.__arr)

    @property
    def arr(self):
        return self.__arr


class FMTLineList(NPString):
    def __init__(self, data):
        lists = ["-", "--", "-.", "-."]
        if data is None:
            data = [""]
        elif isinstance(data, str):
            if data in lists:
                data = [data]
            else:
                data = [""]
        elif isinstance(data, list | tuple):
            data = [i if isinstance(i, str) and i in lists else "" for i in data]
        super().__init__(data, depth_limit=1)

    def __getitem__(self, key):
        return super().__getitem__(key)


class FMTColorList(NPString):
    def __init__(self, data):
        lists = ["r", "g", "b", "c", "m", "y", "k", "w"]
        if data is None:
            data = [""]
        elif isinstance(data, str):
            if data in lists:
                data = [data]
            else:
                data = [""]
        elif isinstance(data, list | tuple):
            data = [i if isinstance(i, str) and i in lists else "" for i in data]
        super().__init__(data, depth_limit=1)

    def __getitem__(self, key):
        return super().__getitem__(key)


class FMTMarkList(NPString):
    def __init__(self, data):
        lists = [
            "o",
            "+",
            "*",
            ".",
            "x",
            "_",
            "|",
            "square",
            "diamond",
            "^",
            "v",
            "<",
            ">",
            "pentagram",
            "hexagram",
        ]
        if data is None:
            data = [""]
        elif isinstance(data, str):
            if data in lists:
                data = [data]
            else:
                data = [""]
        elif isinstance(data, list | tuple):
            data = [i if isinstance(i, str) and i in lists else "" for i in data]
        super().__init__(data, depth_limit=1)

    def __getitem__(self, key):
        return super().__getitem__(key)
