"""フレームワーク全体で使用する型を設定しているモジュール"""

from collections.abc import Iterable
from typing import Any, Callable, Collection, Literal, TypeAlias, TypeVar, overload

import numpy as np
from numpy.typing import ArrayLike, NDArray

__all__ = [
    "_T",
    "ColorType",
    "ColorTypeN",
    "FunctionType",
    "labeltype",
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
    "Type_Iterableint",
    "Type_Iterablestr",
    "Type_npFloat",
    "Type_npFloats",
    "Type_npInt",
    "Type_npInts",
    "ArrayLike",
    "Any",
    "Callable",
    "Collection",
    "Literal",
    "TypeAlias",
    "TypeVar",
    "overload",
]
_T = TypeVar("_T")
# Iterable
Type_Iterablestr: TypeAlias = Iterable[str]
Type_Iterableint: TypeAlias = Iterable[int]
# number
Type_npInt: TypeAlias = np.int8 | np.int16 | np.int32 | np.int64
Type_npInts: TypeAlias = int | Type_npInt
Type_npFloat: TypeAlias = np.float16 | np.float32 | np.float64
Type_npFloats: TypeAlias = float | Type_npFloat
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


# function type
def _f():
    pass


FunctionType = type(_f)
# bool
Type_bool: TypeAlias = bool | np.bool
# Graph
labeltype: TypeAlias = str | list | tuple | None
o_array: TypeAlias = (
    list[int, float, str]
    | tuple[int, float, str]
    | NDArray[np.str_]
    | NDArray[np.int_]
    | NDArray[np.floating]
)
n_array: TypeAlias = list | tuple | NDArray
# Color
RGBColorType: TypeAlias = str | tuple[float, float, float]
RGBAColorType: TypeAlias = (
    str | TupleFloat4 | tuple[RGBColorType, float] | tuple[TupleFloat4, float]
)
ColorType: TypeAlias = RGBColorType | RGBAColorType
ColorTypeN: TypeAlias = ColorType | None
