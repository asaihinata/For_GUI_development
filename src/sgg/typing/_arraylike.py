from collections.abc import Sequence
from typing import Any, SupportsIndex
from types import NoneType

import numpy as np
from numpy._typing import _NestedSequence, _SupportsArray
from numpy.dtypes import StringDType

__all__ = [
    "_AnyShape",
    "_ArrayLikeNone_co",
    "_Array1D",
    "_ArrayLikeAnyString_co",
    "_ArrayLikeBool_co",
    "_ArrayLikeBytes_co",
    "_ArrayLikeComplex_co",
    "_ArrayLikeFloat_co",
    "_ArrayLikeInt_co",
    "_ArrayLikeNumber_co",
    "_ArrayLikeStr_co",
    "_ArrayLikeString_co",
    "_ArrayLikeDT64_co",
    "_ArrayLikeUInt_co",
    "_DualArrayLike",
    "_Shape",
    "_ShapeLike",
    "_StringDTypeSupportsArray",
    "Typeaxis",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
# 配列
type _Array1D[ScalarT: np.generic] = np.ndarray[tuple[int], np.dtype[ScalarT]]
# 形状
type _Shape = tuple[int, ...]
type _AnyShape = tuple[Any, ...]
type _ShapeLike = SupportsIndex | Sequence[SupportsIndex]
"""shapeタプルに変換可能なものなら何でも"""
# bool
type _ArrayLikeBool_co = _DualArrayLike[np.dtype[np.bool | np.bool_ | bool], bool]
# number
type _ArrayLikeUInt_co = _DualArrayLike[np.dtype[np.bool | np.unsignedinteger], bool]
type _ArrayLikeInt_co = _DualArrayLike[np.dtype[np.bool | np.integer], int]
type _ArrayLikeFloat_co = _DualArrayLike[
    np.dtype[np.bool | np.integer | np.floating],
    float,
]
type _ArrayLikeComplex_co = _DualArrayLike[np.dtype[np.bool | np.number], complex]
type _ArrayLikeNumber_co = _DualArrayLike[
    np.dtype[np.bool | np.number], int | float | complex
]
# string and bytes
type _StringDTypeSupportsArray = _SupportsArray[StringDType]
"""可変長文字列型(StringDType)のデータを持った配列"""
type _ArrayLikeStr_co = _DualArrayLike[np.dtype[np.str_], str]
type _ArrayLikeBytes_co = _DualArrayLike[np.dtype[np.bytes_], bytes]
type _ArrayLikeString_co = _DualArrayLike[StringDType, str]
type _ArrayLikeAnyString_co = _DualArrayLike[
    np.dtype[np.character] | StringDType,
    bytes | str,
]
# date
type _ArrayLikeDT64_co = _DualArrayLike[
    np.dtype[np.bool | np.integer | np.datetime64],
    int,
]
# None
type _ArrayLikeNone_co = _DualArrayLike[
    np.dtype[NoneType],
    NoneType,
]
# その他
type Typeaxis = _ShapeLike | None
"""`axis`専用の型ヒント"""
