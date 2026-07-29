import numpy as np
from numpy._typing import _DTypeLike, _NestedSequence, _SupportsArray

__all__ = [
    "_ArangeNumber_DtypeLike",
    "_BoolDTypeLike",
    "_ComplexDtypeLike",
    "_DTypeLike",
    "_DTypeLikeF32",
    "_DTypeLikeF64",
    "_DTypeLikeFloat",
    "_DTypeLikeI64",
    "_DualArrayLike",
    "_FloatsNumericDTypeLike",
    "_IntsNumericDTypeLike",
    "_NumericDTypeLike",
    "_RealNumericDTypeLike",
    "_StringDTypeLike",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
# 真偽型
type _BoolDTypeLike = np.dtype[np.bool_ | np.bool] | type[bool]
# 数値
type _ArangeNumber_DtypeLike = _DTypeLike[np.integer | np.floating]
type _NumericDTypeLike = _DTypeLike[np.number] | type[int] | type[float] | type[complex]
"""数値全般のdtype"""
type _RealNumericDTypeLike = _DTypeLike[np.integer | np.floating] | type[int] | type[
    float
]
"""`実数`全般のdtype"""
type _IntsNumericDTypeLike = _DTypeLike[np.integer] | type[int]
"""`整数`全般のdtype"""
type _DTypeLikeI64 = _DTypeLike[np.int64] | np._Int64Codes
type _DTypeLikeF32 = _DTypeLike[np.float32] | np._Float32Codes
type _DTypeLikeF64 = type[float] | _DTypeLike[np.float64] | np._Float64Codes
type _DTypeLikeFloat = type[float] | _DTypeLike[np.float32 | np.float64] | str
type _FloatsNumericDTypeLike = _DTypeLike[np.floating] | type[float]
"""`浮動小数型`全般のdtype"""
type _ComplexDtypeLike = np.dtype[np.complexfloating] | type[complex]
"""`複素数`全般のdtype"""
# 文字列
type _StringDTypeLike = np.dtype[np.str_ | np.bytes_] | type[str] | type[bytes]
"""numpyとPythonの文字列全般の型の型ヒント"""
# 日付
type _DTypeLikeDT64 = _DTypeLike[np.timedelta64] | np._TD64Codes