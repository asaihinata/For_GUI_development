from collections.abc import Sequence
from datetime import date, datetime
from typing import Any, SupportsIndex, TypeVar, Union

import numpy as np
from numpy._typing import _NestedSequence

__all__ = [
    "_AnyShape",
    "_ArrayLikeDateParse_co",
    "_Shape",
    "_ShapeLike",
    "_ShapeT",
    "ArrayLikeAny",
    "ArrayLikeBool",
    "ArrayLikeDateParse",
    "ArrayLikedatetime",
    "ArrayLikeNS",
    "ArrayLikeNumber",
    "ArrayLikeString",
    "DateParseScalar",
    "TypeArray2LikeAny",
    "TypeArray2LikeBool",
    "TypeArray2Likedatetime",
    "TypeArray2LikeNS",
    "TypeArray2LikeNumber",
    "TypeArray2LikeString",
    "TypeArrayLikeAny",
    "TypeArrayLikeBool",
    "TypeArrayLikedatetime",
    "TypeArrayLikeNS",
    "TypeArrayLikeNumber",
    "TypeArrayLikeString",
    "TypeArraysLikeAny",
    "TypeArraysLikeBool",
    "TypeArraysLikedatetime",
    "TypeArraysLikeNS",
    "TypeArraysLikeNumber",
    "TypeArraysLikeString",
    "Typeaxis",
    "Typeget_Array",
    "Typeget_Array_Number",
    "Typeget_Array_NumStr",
    "Typeget_Arrays",
    "Typeget_Arrays_Number",
    "Typeget_Arrays_NumStr",
    "Typetuple_float64",
]
type _Shape = tuple[int, ...]
type _AnyShape = tuple[Any, ...]
type _ShapeLike = SupportsIndex | Sequence[SupportsIndex]
# 数値
ArrayLikeNumber = TypeVar("ArrayLikeNumber", bound=Union[np.generic, int, float])
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
# 日付
ArrayLikedatetime = TypeVar("ArrayLikedatetime", bound=np.datetime64)
type TypeArrayLikedatetime = np.ndarray[tuple[int], np.dtype[np.datetime64]]
type TypeArray2Likedatetime = np.ndarray[tuple[int, int], np.dtype[np.datetime64]]
type TypeArraysLikedatetime = np.ndarray[tuple[int, ...], np.dtype[np.datetime64]]
# bool
ArrayLikeBool = TypeVar("ArrayLikedatetime", bound=Union[np.bool_, bool])
type TypeArrayLikeBool = np.ndarray[tuple[int], np.dtype[ArrayLikeBool]]
type TypeArray2LikeBool = np.ndarray[tuple[int, int], np.dtype[ArrayLikeBool]]
type TypeArraysLikeBool = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeBool]]
# Any
ArrayLikeAny = TypeVar("ArrayLikeAny", bound=Union[Any])
type TypeArrayLikeAny = np.ndarray[tuple[int], np.dtype[ArrayLikeAny]]
type TypeArray2LikeAny = np.ndarray[tuple[int, int], np.dtype[ArrayLikeAny]]
type TypeArraysLikeAny = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeAny]]
_ShapeT = TypeVar("_ShapeT", bound=_Shape, default=_AnyShape, covariant=True)
ArrayLikeDateParse = TypeVar(
    "ArrayLikeDateParse",
    bound=Union[str, bytes, np.str_, np.bytes_, datetime, date, np.datetime64],
)
type DateParseScalar = (
    str | bytes | np.str_ | np.bytes_ | datetime | date | np.datetime64 | int
)
type _ArrayLikeDateParse_co = (
    DateParseScalar
    | _NestedSequence[DateParseScalar]
    | np.ndarray[Any, np.dtype[np.str_ | np.bytes_ | np.object_ | np.datetime64]]
)
type Typeget_Arrays_Number = np.ndarray[tuple[int, ...], np.dtype[np.number]]
type Typeget_Arrays_NumStr = np.ndarray[
    tuple[int, ...], np.dtype[np.number | np.character]
]
type Typeget_Arrays = np.ndarray[tuple[int, ...], np.dtype[Any]]
type Typeget_Array_Number = np.ndarray[tuple[int], np.dtype[np.number]]
type Typeget_Array_NumStr = np.ndarray[tuple[int], np.dtype[np.number | np.character]]
type Typeget_Array = np.ndarray[tuple[int], np.dtype[np.number]]
type Typetuple_float64 = tuple[np.float64, np.float64]
type Typeaxis = _ShapeLike | None
