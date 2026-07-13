"""フレームワーク全体で使用する型を設定しているモジュール"""

from datetime import date, datetime
from typing import Any, Literal, TypeAlias, TypeAliasType, TypeVar, Union, overload

import numpy as np
from numpy._typing import (
    _ArrayLikeAnyString_co,
    _ArrayLikeBool_co,
    _ArrayLikeNumber_co,
    _ArrayLikeTD64_co,
    _CharLike_co,
    _ComplexLike_co,
    _DT64Codes,
    _DTypeLikeTD64,
    _FloatLike_co,
    _IntLike_co,
    _NestedSequence,
    _UIntLike_co,
)
from numpy.typing import ArrayLike

__all__ = [
    "_ArrayLikeAnyString_co",
    "_ArrayLikeBool_co",
    "_ArrayLikeDateParse_co",
    "_ArrayLikeNumber_co",
    "_ArrayLikeTD64_co",
    "_CharType",
    "_DATE_UNITL",
    "_dt64_unit",
    "_DT64Codes",
    "_DTypeLikeTD64",
    "_DTypeT",
    "_get_dt64_unit",
    "_NATIVETIME_UNITL",
    "_NumberT",
    "_ShapeT",
    "_StrT",
    "Any",
    "ArrayLike",
    "ArrayLikeAny",
    "ArrayLikeBool",
    "ArrayLikeDateParse",
    "ArrayLikedatetime",
    "ArrayLikeNS",
    "ArrayLikeNumber",
    "ArrayLikeString",
    "ColorType",
    "ColorTypeN",
    "DateParseScalar",
    "DateUnit",
    "Incomplete",
    "Literal",
    "NativeTimeUnit",
    "overload",
    "Type_icon",
    "Type_Marker",
    "Type_Solid",
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
    "TypeNumber",
    "TypeStr",
    "Typetuple_float64",
    "TypeVar",
]
# 色
ColorType: TypeAlias = str
ColorTypeN: TypeAlias = str | None
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
# 数値 + 文字列
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
# dialogのアイコン
Type_icon: TypeAlias = Literal["error", "info", "question", "warning"]
_ShapeT = TypeVar("_ShapeT", bound=np._Shape, default=np._AnyShape, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.generic, default=np.dtype, covariant=True)
_CharType = TypeVar(
    "CharType", bound=np.dtype, default=np.dtype[np.str_], covariant=True
)
TypeNumber: TypeAlias = (
    _FloatLike_co | _IntLike_co | _UIntLike_co | np.generic | _ComplexLike_co
)
_NumberT = TypeAliasType("_NumberT", TypeNumber)
TypeStr: TypeAlias = _CharLike_co | np.character
_StrT = TypeAliasType("_StrT", TypeStr)
_DATE_UNITL = Literal["Y", "M", "W", "D", b"Y", b"M", b"W", b"D"]
_NATIVETIME_UNITL = Literal[
    "h", "m", "s", "ms", "us", "μs", b"h", b"m", b"s", b"ms", b"us"
]
_MDT64Codes = Literal[
    "datetime64[Y]",
    "|datetime64[Y]",
    "=datetime64[Y]",
    "<datetime64[Y]",
    ">datetime64[Y]",
    "datetime64[M]",
    "|datetime64[M]",
    "=datetime64[M]",
    "<datetime64[M]",
    ">datetime64[M]",
    "datetime64[W]",
    "|datetime64[W]",
    "=datetime64[W]",
    "<datetime64[W]",
    ">datetime64[W]",
    "datetime64[D]",
    "|datetime64[D]",
    "=datetime64[D]",
    "<datetime64[D]",
    ">datetime64[D]",
    "datetime64[h]",
    "|datetime64[h]",
    "=datetime64[h]",
    "<datetime64[h]",
    ">datetime64[h]",
    "datetime64[m]",
    "|datetime64[m]",
    "=datetime64[m]",
    "<datetime64[m]",
    ">datetime64[m]",
    "datetime64[s]",
    "|datetime64[s]",
    "=datetime64[s]",
    "<datetime64[s]",
    ">datetime64[s]",
    "datetime64[ms]",
    "|datetime64[ms]",
    "=datetime64[ms]",
    "<datetime64[ms]",
    ">datetime64[ms]",
    "datetime64[us]",
    "|datetime64[us]",
    "=datetime64[us]",
    "<datetime64[us]",
    ">datetime64[us]",
    "datetime64[ns]",
    "|datetime64[ns]",
    "=datetime64[ns]",
    "<datetime64[ns]",
    ">datetime64[ns]",
    "datetime64[ps]",
    "|datetime64[ps]",
    "=datetime64[ps]",
    "<datetime64[ps]",
    ">datetime64[ps]",
    "datetime64[fs]",
    "|datetime64[fs]",
    "=datetime64[fs]",
    "<datetime64[fs]",
    ">datetime64[fs]",
    "datetime64[as]",
    "|datetime64[as]",
    "=datetime64[as]",
    "<datetime64[as]",
    ">datetime64[as]",
    "M8[Y]",
    "|M8[Y]",
    "=M8[Y]",
    "<M8[Y]",
    ">M8[Y]",
    "M8[M]",
    "|M8[M]",
    "=M8[M]",
    "<M8[M]",
    ">M8[M]",
    "M8[W]",
    "|M8[W]",
    "=M8[W]",
    "<M8[W]",
    ">M8[W]",
    "M8[D]",
    "|M8[D]",
    "=M8[D]",
    "<M8[D]",
    ">M8[D]",
    "M8[h]",
    "|M8[h]",
    "=M8[h]",
    "<M8[h]",
    ">M8[h]",
    "M8[m]",
    "|M8[m]",
    "=M8[m]",
    "<M8[m]",
    ">M8[m]",
    "M8[s]",
    "|M8[s]",
    "=M8[s]",
    "<M8[s]",
    ">M8[s]",
    "M8[ms]",
    "|M8[ms]",
    "=M8[ms]",
    "<M8[ms]",
    ">M8[ms]",
    "M8[us]",
    "|M8[us]",
    "=M8[us]",
    "<M8[us]",
    ">M8[us]",
    "M8[ns]",
    "|M8[ns]",
    "=M8[ns]",
    "<M8[ns]",
    ">M8[ns]",
    "M8[ps]",
    "|M8[ps]",
    "=M8[ps]",
    "<M8[ps]",
    ">M8[ps]",
    "M8[fs]",
    "|M8[fs]",
    "=M8[fs]",
    "<M8[fs]",
    ">M8[fs]",
    "M8[as]",
    "|M8[as]",
    "=M8[as]",
    "<M8[as]",
    ">M8[as]",
]
DateUnit: TypeAlias = _DATE_UNITL
NativeTimeUnit: TypeAlias = _NATIVETIME_UNITL
DateUnitSet: TypeAlias = _DT64Codes | np._TD64Unit
MDateUnitSet: TypeAlias = _MDT64Codes | np._TD64Unit

def _dt64_unit(spec: Literal[DateUnitSet]) -> str: ...
def _get_dt64_unit(dtype_str: Literal[MDateUnitSet], auto: str = "D") -> str: ...

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
Incomplete: TypeAlias = Any
Type_Solid: TypeAlias = Literal["-", "--", "-.", ":", "None", " ", ""]
Type_Marker: TypeAlias = Literal[
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
Typeget_Arrays_Number: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[np.number]]
Typeget_Arrays_NumStr: TypeAlias = np.ndarray[
    tuple[int, ...], np.dtype[np.number | np.character]
]
Typeget_Arrays: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[Any]]
Typeget_Array_Number: TypeAlias = np.ndarray[tuple[int], np.dtype[np.number]]
Typeget_Array_NumStr: TypeAlias = np.ndarray[
    tuple[int], np.dtype[np.number | np.character]
]
Typeget_Array: TypeAlias = np.ndarray[tuple[int], np.dtype[np.number]]
Typetuple_float64: TypeAlias = tuple[np.float64, np.float64]
Typeaxis: TypeAlias = np._ShapeLike | None
