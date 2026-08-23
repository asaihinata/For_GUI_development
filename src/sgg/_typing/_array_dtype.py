import numpy as np
import numpy._typing as npt

import sgg._typing as sgt

__all__ = [
    "_BoolDTypeLike",
    "_ComplexDtypeLike",
    "_DTypeLike",
    "_DtypeLikeDT",
    "_DtypeLikeDTs",
    "_DTypeLikeF32",
    "_DTypeLikeF64",
    "_DTypeLikeFloat",
    "_DTypeLikeInt",
    "_DtypeLikeTD",
    "_DtypeLikeTDs",
    "_DualArrayLike",
    "_NumericDTypeLike",
    "_RealNumericDTypeLike",
    "_StringsDTypeLike",
    "DTypeNLike",
]
type _DTypeLike[ScalarT: np.generic] = (
    type[ScalarT] | np.dtype[ScalarT] | npt._SupportsDType[np.dtype[ScalarT]]
)
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    npt._SupportsArray[DTypeT]
    | npt._NestedSequence[npt._SupportsArray[DTypeT]]
    | BuiltinT
    | npt._NestedSequence[BuiltinT]
)
# 真偽型
type _BoolDTypeLike = type[bool] | _DTypeLike[np.bool_ | np.bool] | npt._BoolCodes
# 数値
type _NumericDTypeLike = type[int | float | complex] | _DTypeLike[
    np.number
] | npt._NumberCodes
type _DTypeLikeInt = type[int] | _DTypeLike[
    np.integer
] | npt._SignedIntegerCodes | npt._UnsignedIntegerCodes
type _DTypeLikeFloat = type[float] | _DTypeLike[np.floating] | npt._FloatingCodes
type _DTypeLikeF32 = _DTypeLike[np.float32] | npt._Float32Codes
type _DTypeLikeF64 = type[float] | _DTypeLike[np.float64] | npt._Float64Codes
type _RealNumericDTypeLike = _DTypeLikeInt | _DTypeLikeFloat
type _ComplexDtypeLike = type[complex] | np.dtype[
    np.complexfloating
] | npt._ComplexFloatingCodes
# 文字列
type _StringsDTypeLike = type[str | bytes] | _DTypeLike[
    np.str_ | np.bytes_
] | np.dtypes.StringDType | npt._CharacterCodes
# 日付
type _DtypeLikeDT = _DTypeLike[np.datetime64] | sgt._DT64Code_All
type _DtypeLikeDTs = _DTypeLike[np.datetime64] | sgt._DT64Codes_All
type _DtypeLikeTD = _DTypeLike[np.timedelta64] | sgt._TD64Code_All
type _DtypeLikeTDs = _DTypeLike[np.timedelta64] | sgt._TD64Codes_All
# その他
type DTypeNLike = npt.DTypeLike | None
