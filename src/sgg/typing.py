"""フレームワーク全体で使用する型を設定しているモジュール"""

from typing import (Any, Callable, Collection, Literal, TypeAlias, TypeVar, Union,
                    overload)

import numpy as np
from numpy.typing import ArrayLike, NDArray

__all__ = [
    "_T",
    "ColorType",
    "ColorTypeN",
    "FunctionType",
    "ListFloat2",
    "ListFloat4",
    "ListInt2",
    "ListInt4",
    "Listlike",
    "ListNumbertype2",
    "ListNumbertype4",
    "n_array",
    "nListlike",
    "NPstr2",
    "o_array",
    "RGBAColorType",
    "RGBColorType",
    "TupleFloat2",
    "TupleFloat4",
    "TupleInt2",
    "TupleInt4",
    "TupleNumbertype2",
    "TupleNumbertype4",
    "Type_bool",
    "ArrayLike",
    "Any",
    "Callable",
    "Collection",
    "Literal",
    "TypeAlias",
    "TypeVar",
    "overload",
    "ArrayLikeNumber",
    "TypeArrayLikeNumber",
    "TypeArray2LikeNumber",
    "TypeArraysLikeNumber",
    "ArrayLikeString",
    "TypeArrayLikeString",
    "TypeArray2LikeString",
    "TypeArraysLikeString",
    "ArrayLikeNS",
    "TypeArrayLikeNS",
    "TypeArray2LikeNS",
    "TypeArraysLikeNS",
]
_T = TypeVar("_T")
# list like and numpy list
Listlike: TypeAlias = list | tuple
nListlike: TypeAlias = np.ndarray | Listlike
NPstr2: TypeAlias = np.ndarray[str, str] | np.ndarray[np.str_, np.str_]
TupleNumbertype2: TypeAlias = tuple[np.number, np.number]
TupleNumbertype4: TypeAlias = tuple[np.number, np.number, np.number, np.number]
TupleInt2: TypeAlias = tuple[int, int]
TupleInt4: TypeAlias = tuple[int, int, int, int]
TupleFloat2: TypeAlias = tuple[float, float]
TupleFloat4: TypeAlias = tuple[float, float, float, float]
ListNumbertype2: TypeAlias = list[np.number, np.number]
ListNumbertype4: TypeAlias = list[np.number, np.number, np.number, np.number]
ListInt2: TypeAlias = list[int, int]
ListInt4: TypeAlias = list[int, int, int, int]
ListFloat2: TypeAlias = list[float, float]
ListFloat4: TypeAlias = list[float, float, float, float]


# 関数型
def _f():
    pass


FunctionType = type(_f)
# bool
Type_bool: TypeAlias = bool | np.bool
# Graph
o_array: TypeAlias = (
    list[int, float, str]
    | tuple[int, float, str]
    | NDArray[np.str_]
    | NDArray[np.int_]
    | NDArray[np.floating]
)
n_array: TypeAlias = list | tuple | NDArray

# グラフのデータの型ヒント

# 数値
ArrayLikeNumber = TypeVar("ArrayLikeNumber", bound=Union[np.generic, int, float])
TypeArrayLikeNumber: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeNumber]]
TypeArray2LikeNumber: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeNumber]]
TypeArraysLikeNumber: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeNumber]]
# 文字列
ArrayLikeString = TypeVar("ArrayLikeString", bound=Union[np.str_, str])
TypeArrayLikeString: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeString]]
TypeArray2LikeString: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeString]]
TypeArraysLikeString: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeString]]
# 数値+文字列
ArrayLikeNS = TypeVar("ArrayLikeNS", bound=Union[np.generic, int, float, np.str_, str])
TypeArrayLikeNS: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeNS]]
TypeArray2LikeNS: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeNS]]
TypeArraysLikeNS: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeNS]]


# Color
RGBColorType: TypeAlias = str | tuple[float, float, float]
RGBAColorType: TypeAlias = (
    str | TupleFloat4 | tuple[RGBColorType, float] | tuple[TupleFloat4, float]
)
ColorType: TypeAlias = RGBColorType | RGBAColorType
ColorTypeN: TypeAlias = ColorType | None
