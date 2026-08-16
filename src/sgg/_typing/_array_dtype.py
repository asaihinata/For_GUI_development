import numpy as np
import numpy._typing as npt

from sgg._typing import _DT64Codes_All, _TD64Codes_All

__all__ = [
    "_BoolDTypeLike",
    "_ComplexDtypeLike",
    "_DtypeLikeDT",
    "_DTypeLikeF32",
    "_DTypeLikeF64",
    "_DTypeLikeFloat",
    "_DTypeLikeInt",
    "_DtypeLikeTD",
    "_DualArrayLike",
    "_NumericDTypeLike",
    "_RealNumericDTypeLike",
    "_StringsDTypeLike",
    "DTypeNLike",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    npt._SupportsArray[DTypeT]
    | npt._NestedSequence[npt._SupportsArray[DTypeT]]
    | BuiltinT
    | npt._NestedSequence[BuiltinT]
)
# 真偽型
type _BoolDTypeLike = type[bool] | npt._DTypeLike[np.bool_ | np.bool] | npt._BoolCodes
# 数値
type _NumericDTypeLike = type[int | float | complex] | npt._DTypeLike[
    np.number
] | npt._NumberCodes
type _DTypeLikeInt = type[int] | npt._DTypeLike[
    np.integer
] | npt._SignedIntegerCodes | npt._UnsignedIntegerCodes
type _DTypeLikeFloat = type[float] | npt._DTypeLike[np.floating] | npt._FloatingCodes
type _DTypeLikeF32 = npt._DTypeLike[np.float32] | npt._Float32Codes
type _DTypeLikeF64 = type[float] | npt._DTypeLike[np.float64] | npt._Float64Codes
type _RealNumericDTypeLike = _DTypeLikeInt | _DTypeLikeFloat
type _ComplexDtypeLike = type[complex] | np.dtype[
    np.complexfloating
] | npt._ComplexFloatingCodes
# 文字列
type _StringsDTypeLike = type[str | bytes] | npt._DTypeLike[
    np.str_ | np.bytes_
] | np.dtypes.StringDType | npt._CharacterCodes
# 日付
type _DtypeLikeDT = npt._DTypeLike[np.datetime64] | _DT64Codes_All
type _DtypeLikeTD = npt._DTypeLike[np.timedelta64] | _TD64Codes_All
# その他
type DTypeNLike = npt.DTypeLike | None
