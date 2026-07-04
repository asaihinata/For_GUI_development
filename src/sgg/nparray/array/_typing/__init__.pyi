from datetime import date, datetime
from typing import Any, TypeAlias, TypeAliasType, TypeVar, Union

import numpy as np
from numpy._typing import (_ArrayLikeAnyString_co, _ArrayLikeBool_co,
                           _ArrayLikeNumber_co, _ArrayLikeTD64_co, _CharLike_co,
                           _ComplexLike_co, _FloatLike_co, _IntLike_co, _NestedSequence,
                           _UIntLike_co)

__all__ = [
    "_ArrayLikeAnyString_co",
    "_ArrayLikeNumber_co",
    "_ArrayLikeBool_co",
    "_ArrayLikeTD64_co",
    "_DTypeT",
    "_ShapeT" "TypeNumber",
    "_NumberT",
    "TypeStr",
    "_StrT",
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
    "ArrayLikeAny",
    "TypeArrayLikeAny",
    "TypeArray2LikeAny",
    "TypeArraysLikeAny",
    "ArrayLikedatetime",
    "TypeArrayLikedatetime",
    "TypeArray2Likedatetime",
    "TypeArraysLikedatetime",
    "ArrayLikeBool",
    "TypeArrayLikeBool",
    "TypeArray2LikeBool",
    "TypeArraysLikeBool",
    "_CharType",
    "ArrayLikeDateParse",
    "DateParseScalar",
    "_ArrayLikeDateParse_co",
]
_ShapeT = TypeVar("_ShapeT", bound=np._Shape, default=np._AnyShape, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype, default=np.dtype, covariant=True)
_CharType = TypeVar(
    "CharType", bound=np.dtype, default=np.dtype[np.str_], covariant=True
)
TypeNumber: TypeAlias = (
    _FloatLike_co | _IntLike_co | _UIntLike_co | np.generic | _ComplexLike_co
)
_NumberT = TypeAliasType("_NumberT", TypeNumber)
TypeStr: TypeAlias = _CharLike_co | np.character
_StrT = TypeAliasType("_StrT", TypeStr)
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
# 日付
ArrayLikedatetime = TypeVar("ArrayLikedatetime", bound=np.datetime64)
TypeArrayLikedatetime: TypeAlias = np.ndarray[tuple[int], np.dtype[np.datetime64]]
TypeArray2Likedatetime: TypeAlias = np.ndarray[tuple[int, int], np.dtype[np.datetime64]]
TypeArraysLikedatetime: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[np.datetime64]]
# bool
ArrayLikeBool = TypeVar("ArrayLikedatetime", bound=Union[np.bool_, bool])
TypeArrayLikeBool: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeBool]]
TypeArray2LikeBool: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeBool]]
TypeArraysLikeBool: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeBool]]
# Any
ArrayLikeAny = TypeVar("ArrayLikeAny", bound=Union[Any])
TypeArrayLikeAny: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeAny]]
TypeArray2LikeAny: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeAny]]
TypeArraysLikeAny: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeAny]]
ArrayLikeDateParse = TypeVar(
    "ArrayLikeDateParse",
    bound=Union[str, bytes, np.str_, np.bytes_, datetime, date, np.datetime64],
)
DateParseScalar: TypeAlias = (
    str | bytes | np.str_ | np.bytes_ | datetime | date | np.datetime64
)
_ArrayLikeDateParse_co: TypeAlias = (
    DateParseScalar
    | _NestedSequence[DateParseScalar]
    | np.ndarray[Any, np.dtype[np.str_ | np.bytes_ | np.object_ | np.datetime64]]
)
