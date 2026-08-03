from typing import Literal, TypeVar, Union

import numpy as np

__all__ = [
    "ColorType",
    "ColorTypeN",
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
