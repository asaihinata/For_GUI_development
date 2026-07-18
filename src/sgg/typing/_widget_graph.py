from typing import Literal, TypeVar, Union

import numpy as np

__all__ = [
    "ArrayLikeNS",
    "ArrayLikeNumber",
    "ArrayLikeString",
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
    "Typeget_Array_Number",
    "Typeget_Array_NumStr",
    "Typeget_Arrays_Number",
    "Typeget_Arrays_NumStr",
    "Typetuple_float64",
]
# 数値
ArrayLikeNumber = TypeVar("ArrayLikeNumber", bound=Union[np.number, int, float])
type TypeArrayLikeNumber = np.ndarray[tuple[int], np.dtype[ArrayLikeNumber]]
type TypeArray2LikeNumber = np.ndarray[tuple[int, int], np.dtype[ArrayLikeNumber]]
type TypeArraysLikeNumber = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeNumber]]
# 文字列
ArrayLikeString = TypeVar("ArrayLikeString", bound=Union[np.str_, str])
type TypeArrayLikeString = np.ndarray[tuple[int], np.dtype[ArrayLikeString]]
type TypeArray2LikeString = np.ndarray[tuple[int, int], np.dtype[ArrayLikeString]]
type TypeArraysLikeString = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeString]]
# 数値 + 文字列
ArrayLikeNS = TypeVar("ArrayLikeNS", bound=Union[np.generic, int, float, np.str_, str])
type TypeArrayLikeNS = np.ndarray[tuple[int], np.dtype[ArrayLikeNS]]
type TypeArray2LikeNS = np.ndarray[tuple[int, int], np.dtype[ArrayLikeNS]]
type TypeArraysLikeNS = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeNS]]
type Typeget_Arrays_Number = np.ndarray[tuple[int, ...], np.dtype[np.number]]
type Typeget_Array_Number = np.ndarray[tuple[int], np.dtype[np.number]]
type Typeget_Array_NumStr = np.ndarray[tuple[int], np.dtype[np.number | np.character]]
type Typeget_Arrays_NumStr = np.ndarray[
    tuple[int, ...], np.dtype[np.number | np.character]
]
type Typetuple_float64 = tuple[np.float64, np.float64]
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
