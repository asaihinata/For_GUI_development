import numpy as np
from numpy._typing import (_BoolCodes, _ComplexFloatingCodes, _DTypeLike,
                           _FloatingCodes, _NestedSequence, _NumberCodes,
                           _SignedIntegerCodes, _SupportsArray,
                           _UnsignedIntegerCodes,_CharacterCodes)

from sgg.typing import _DT64Codes_All, _TD64Codes_All

__all__ = [
    "_BoolDTypeLike",
    "_ComplexDtypeLike",
    "_DtypeLikeDT",
    "_DTypeLikeFloat",
    "_DTypeLikeInt",
    "_DtypeLikeTD",
    "_NumericDTypeLike",
    "_RealNumericDTypeLike",
    "_StringsDTypeLike",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
# 真偽型
type _BoolDTypeLike = _DTypeLike[np.bool_ | np.bool] | type[bool] | _BoolCodes
# 数値
type _NumericDTypeLike = _DTypeLike[np.number] | type[int|float|complex] | _NumberCodes
type _DTypeLikeInt = _DTypeLike[np.integer] | type[int] | _SignedIntegerCodes | _UnsignedIntegerCodes
type _DTypeLikeFloat = _DTypeLike[np.floating] | type[float] | _FloatingCodes
type _RealNumericDTypeLike = _DTypeLikeInt | _DTypeLikeFloat
type _ComplexDtypeLike = np.dtype[np.complexfloating] | type[complex] | _ComplexFloatingCodes
# 文字列
type _StringsDTypeLike = _DTypeLike[np.str_ | np.bytes_] | np.dtypes.StringDType | type[str | bytes] | _CharacterCodes
# 日付
type _DtypeLikeDT = _DTypeLike[np.datetime64] | _DT64Codes_All
type _DtypeLikeTD = _DTypeLike[np.timedelta64] | _TD64Codes_All
