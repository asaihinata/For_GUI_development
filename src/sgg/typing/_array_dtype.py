import numpy as np
import numpy._typing as npt

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
    "DTypeNLike",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    npt._SupportsArray[DTypeT]
    | npt._NestedSequence[npt._SupportsArray[DTypeT]]
    | BuiltinT
    | npt._NestedSequence[BuiltinT]
)
# 真偽型
type _BoolDTypeLike = npt._DTypeLike[np.bool_ | np.bool] | type[bool] | npt._BoolCodes
# 数値
type _NumericDTypeLike = npt._DTypeLike[np.number] | type[
    int | float | complex
] | npt._NumberCodes
type _DTypeLikeInt = npt._DTypeLike[np.integer] | type[
    int
] | npt._SignedIntegerCodes | npt._UnsignedIntegerCodes
type _DTypeLikeFloat = npt._DTypeLike[np.floating] | type[float] | npt._FloatingCodes
type _RealNumericDTypeLike = _DTypeLikeInt | _DTypeLikeFloat
type _ComplexDtypeLike = np.dtype[np.complexfloating] | type[
    complex
] | npt._ComplexFloatingCodes
# 文字列
type _StringsDTypeLike = npt._DTypeLike[
    np.str_ | np.bytes_
] | np.dtypes.StringDType | type[str | bytes] | npt._CharacterCodes
# 日付
type _DtypeLikeDT = npt._DTypeLike[np.datetime64] | _DT64Codes_All
type _DtypeLikeTD = npt._DTypeLike[np.timedelta64] | _TD64Codes_All
# その他
type DTypeNLike = npt.DTypeLike | None
