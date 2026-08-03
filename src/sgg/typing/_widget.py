from typing import Literal, TypedDict, TypeVar, Union

import numpy as np

__all__ = [
    "ColorType",
    "ColorTypeN",
    "Dict_2DGraph",
    "Dict_3DGraph",
    "Dict_LinefillGraph",
    "Dict_PieGraph",
    "Dict_Polar",
    "Dict_Radar",
    "GetList",
    "Type_icon",
    "Type_Marker",
    "Type_Solid",
    "TypeArray2LikeNS",
    "TypeArray2LikeNumber",
    "TypeArray2LikeString",
    "TypeArrayLikeNS",
    "TypeArrayLikeNumber",
    "TypeArrayLikeString",
    "TypeArraysLikeNS",
    "TypeArraysLikeNumber",
    "TypeArraysLikeString",
    "Typetuple_float64",
]
# 色
type ColorType = str
type ColorTypeN = str | None

# dialogのアイコン
type Type_icon = Literal["error", "info", "question", "warning"]

# グラフ
# 数値
_ArrayLikeNumber = TypeVar("_ArrayLikeNumber", bound=Union[np.number, int, float])
type TypeArrayLikeNumber = np.ndarray[tuple[int], np.dtype[_ArrayLikeNumber]]
type TypeArray2LikeNumber = np.ndarray[tuple[int, int], np.dtype[_ArrayLikeNumber]]
type TypeArraysLikeNumber = np.ndarray[tuple[int, ...], np.dtype[_ArrayLikeNumber]]
# 文字列
_ArrayLikeString = TypeVar("_ArrayLikeString", bound=Union[np.str_, str])
type TypeArrayLikeString = np.ndarray[tuple[int], np.dtype[_ArrayLikeString]]
type TypeArray2LikeString = np.ndarray[tuple[int, int], np.dtype[_ArrayLikeString]]
type TypeArraysLikeString = np.ndarray[tuple[int, ...], np.dtype[_ArrayLikeString]]
# 数値 + 文字列
_ArrayLikeNS = TypeVar(
    "_ArrayLikeNS", bound=Union[np.generic, int, float, np.str_, str]
)
type TypeArrayLikeNS = np.ndarray[tuple[int], np.dtype[_ArrayLikeNS]]
type TypeArray2LikeNS = np.ndarray[tuple[int, int], np.dtype[_ArrayLikeNS]]
type TypeArraysLikeNS = np.ndarray[tuple[int, ...], np.dtype[_ArrayLikeNS]]
type Typetuple_float64 = tuple[np.float64, np.float64]
# 配列
type GetList = np.ndarray
# その他
type Type_Solid = Literal["-", "--", "-.", ":", "None", " ", ""]
type Type_Marker = Literal[
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


# 基本的なウィジェットのキーワード引数の型ヒントを保存するclass
class _Dict_Graph_base(TypedDict):
    key: str | None = ...
    title: str = ...
    size: tuple[int | float, int | float] = (500, 400)
    dpi: int | float = 100
    fg: ColorTypeN = "#000000"
    bg: ColorTypeN = "#ffffff"
    tight_layout: bool = True


class Dict_2DGraph(_Dict_Graph_base):
    alpha: int | float = 1.0
    xlabel: str = ...
    ylabel: str = ...
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    xmajorint: bool = True
    ymajorint: bool = True
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
    xticksdirection: Literal["out", "in", "inout"] = "out"
    yticksdirection: Literal["out", "in", "inout"] = "out"


class Dict_PieGraph(_Dict_Graph_base):
    alpha: int | float = 1.0


class Dict_LinefillGraph(_Dict_Graph_base):
    xlabel: str = ...
    ylabel: str = ...
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    xmajorint: bool = True
    ymajorint: bool = True
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
    xticksdirection: Literal["out", "in", "inout"] = "out"
    yticksdirection: Literal["out", "in", "inout"] = "out"


class Dict_3DGraph(_Dict_Graph_base):
    alpha: int | float = 1.0
    xlabel: str = ...
    ylabel: str = ...
    zlabel: str = ...
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xyz: bool = True
    grid_x: bool = False
    grid_y: bool = False
    grid_z: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    xmajorint: bool = True
    ymajorint: bool = True
    zmajorint: bool = True
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
    zticksshow: bool = False
    xticksdirection: Literal["out", "in", "inout"] = "out"
    yticksdirection: Literal["out", "in", "inout"] = "out"
    znumticks: int | float | None = None
    mouse_rotation: bool = True
    elev: int | float = 30
    azim: int | float = 45


class Dict_Polar(_Dict_Graph_base):
    alpha: int | float = 1.0
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False


class Dict_Radar(_Dict_Graph_base):
    alpha: int | float = 1.0
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
