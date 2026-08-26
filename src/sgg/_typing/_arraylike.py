from collections.abc import Sequence
from datetime import date, datetime, timedelta
from types import NoneType
from typing import Any, Literal, SupportsIndex

import numpy as np
from numpy._typing import NDArray, _NestedSequence, _SupportsArray
from numpy.dtypes import StringDType

__all__ = [
    "_AnyShape",
    "_ArrayDT64",
    "_ArrayLikeBool_co",
    "_ArrayLikeBytes_co",
    "_ArrayLikeComplex_co",
    "_ArrayLikeDT64_co",
    "_ArrayLikeFloat_co",
    "_ArrayLikeInt_co",
    "_ArrayLikeNone_co",
    "_ArrayLikeNumber_co",
    "_ArrayLikeRealNumeric_co",
    "_ArrayLikeStr_co",
    "_ArrayLikeString_co",
    "_ArrayLikeStringDtype_co",
    "_ArrayLikeStrings_co",
    "_ArrayLikeTD64_co",
    "_ArrayLikeTD64s_co",
    "_ComparisonDT64",
    "_DateWord_NAT",
    "_DateWord_NOW",
    "_DateWord_TODAY",
    "_DateWordAll",
    "_DT64Date_co",
    "_DT64Now_co",
    "_NaTValue_co",
    "_Shape",
    "_ShapeInt",
    "_ShapeLike",
    "NDArray",
    "NDBool",
    "NDBool_",
    "NDBools",
    "NDBytes_",
    "NDCharacter",
    "NDDatetime64",
    "NDFloating",
    "NDInteger",
    "NDNumber",
    "NDStr_",
    "NDString",
    "NDStringDtype",
    "NDTimedelta64",
    "NestedList",
    "RAny",
    "RBool",
    "RBool_",
    "RBools",
    "RBytes_",
    "RCharacter",
    "RComplex",
    "RComplex128",
    "RComplex64",
    "RDatetime64",
    "RFloat16",
    "RFloat64",
    "RInt64",
    "RInt8",
    "RNumber",
    "RObject",
    "RStr",
    "RStr_",
    "RString",
    "RTimedelta64",
    "RUInt64",
    "RUInt8",
    "RVoid",
    "Typeaxis",
]
type __DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
type __ReturnDtype[DTypeT: np.generic] = NDArray[DTypeT] | DTypeT
# 形状
type _Shape = tuple[int, ...]
type _AnyShape = tuple[Any, ...]
type _ShapeLike = SupportsIndex | Sequence[SupportsIndex]
"""shapeタプルに変換可能なものなら何でも"""
type _ShapeInt = int | tuple[int, ...]
type NestedList = list["NestedList"]
# bool
type _ArrayLikeBool_co = __DualArrayLike[np.dtype[np.bool | np.bool_], bool]
# number
type _ArrayLikeInt_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer], int | bool
]
type _ArrayLikeFloat_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.floating],
    float | bool,
]
type _ArrayLikeRealNumeric_co = _ArrayLikeBool_co | _ArrayLikeInt_co | _ArrayLikeFloat_co
type _ArrayLikeComplex_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.number], complex
]
type _ArrayLikeNumber_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.number], int | float | complex | bool
]
# string and bytes
type _ArrayLikeString_co = __DualArrayLike[
    np.dtype[np.character] | StringDType,
    bytes | str,
]
type _ArrayLikeStr_co = __DualArrayLike[np.dtype[np.str_], str]
type _ArrayLikeBytes_co = __DualArrayLike[np.dtype[np.bytes_], bytes]
type _ArrayLikeStringDtype_co = __DualArrayLike[StringDType, str]
type _ArrayLikeStrings_co = _ArrayLikeStr_co | _ArrayLikeBytes_co | _ArrayLikeStringDtype_co
# date
type _DateWord_TODAY = Literal["TODAY", "today", b"TODAY", b"today"]
type _DateWord_NOW = Literal["NOW", "now", b"NOW", b"now"]
type _DateWord_NAT = Literal["NAT", "NaT", "nat", b"NAT", b"NaT", b"nat"]
type _DateWordAll = Literal[_DateWord_TODAY, _DateWord_NOW, _DateWord_NAT]
type _DT64Date_co = _NestedSequence[_DateWord_TODAY]
type _DT64Now_co = _NestedSequence[_DateWord_NOW]
type _NaTValue_co = _NestedSequence[_DateWord_NAT]
type _ArrayDT64 = _NestedSequence[np.datetime64] | np.datetime64
type _ComparisonDT64 = _ArrayDT64 | datetime | date
type _ArrayLikeDT64_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.str_ | np.bytes_ | np.datetime64],
    int | bool | str | bytes | datetime | date | _DateWordAll,
]
type _ArrayLikeTD64_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.timedelta64],
    bool | int | timedelta,
]
type _ArrayLikeTD64s_co = __DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.timedelta64],
    bool | int | timedelta | _DateWordAll,
]
# None
type _ArrayLikeNone_co = __DualArrayLike[
    np.dtype[NoneType],
    NoneType,
]
# NDArray
type NDBool = NDArray[np.bool]
type NDBool_ = NDArray[np.bool_]
type NDBools = NDArray[np.bool | np.bool_]
type NDInteger = NDArray[np.integer]
type NDFloating = NDArray[np.floating]
type NDNumber = NDArray[np.number]
type NDStr_ = NDArray[np.str_]
type NDBytes_ = NDArray[np.bytes_]
type NDCharacter = NDArray[np.character]
type NDStringDtype = _ArrayLikeStringDtype_co
type NDString = NDCharacter | NDStringDtype
type NDDatetime64 = NDArray[np.datetime64]
type NDTimedelta64 = NDArray[np.timedelta64]
# 戻り値
type RBool = __ReturnDtype[np.bool]
type RBool_ = __ReturnDtype[np.bool_]
type RBools = __ReturnDtype[np.bool | np.bool_]
type RInt8 = __ReturnDtype[np.int8]
type RInt64 = __ReturnDtype[np.int64]
type RUInt8 = __ReturnDtype[np.uint8]
type RUInt64 = __ReturnDtype[np.uint64]
type RFloat16 = __ReturnDtype[np.float16]
type RFloat64 = __ReturnDtype[np.float64]
type RComplex64 = __ReturnDtype[np.complex64]
type RComplex128 = __ReturnDtype[np.complex128]
type RComplex=__ReturnDtype[np.complex128|np.complex64]
type RNumber = __ReturnDtype[np.number]
type RStr = NDArray[np.str_] | str
type RStr_ = __ReturnDtype[np.str_]
type RBytes_ = __ReturnDtype[np.bytes_]
type RCharacter = __ReturnDtype[np.character]
type RString = NDArray[np.str_ | np.bytes_] | np.ndarray[
    _AnyShape, StringDType
] | np.str_ | np.bytes_ | StringDType
type RDatetime64 = __ReturnDtype[np.datetime64]
type RTimedelta64 = __ReturnDtype[np.timedelta64]
type RObject = __ReturnDtype[np.object_]
type RVoid = __ReturnDtype[np.void]
type RAny = NDArray[Any] | Any
# その他
type Typeaxis = _ShapeLike | None
"""`axis`専用の型ヒント"""
