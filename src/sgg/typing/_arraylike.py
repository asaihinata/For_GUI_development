from collections.abc import Sequence
from datetime import date, datetime, timedelta
from types import NoneType
from typing import Any, SupportsIndex

import numpy as np
from numpy._typing import _NestedSequence, _SupportsArray
from numpy.dtypes import StringDType

__all__ = [
    "_AnyShape",
    "_ArrayLikeBool_co",
    "_ArrayLikeBytes_co",
    "_ArrayLikeComplex_co",
    "_ArrayLikeDT64_co",
    "_ArrayLikeFloat_co",
    "_ArrayLikeInt_co",
    "_ArrayLikeNone_co",
    "_ArrayLikeNumber_co",
    "_ArrayLikeStr_co",
    "_ArrayLikeString_co",
    "_ArrayLikeStringDtype_co",
    "_ArrayLikeStrings_co",
    "_ArrayLikeTD64_co",
    "_Shape",
    "_ShapeInt",
    "_ShapeLike",
    "Typeaxis",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
# 形状
type _Shape = tuple[int, ...]
type _AnyShape = tuple[Any, ...]
type _ShapeLike = SupportsIndex | Sequence[SupportsIndex]
"""shapeタプルに変換可能なものなら何でも"""
type _ShapeInt = int | tuple[int, ...]
# bool
type _ArrayLikeBool_co = _DualArrayLike[np.dtype[np.bool | np.bool_], bool]
# number
type _ArrayLikeInt_co = _DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer], int | bool
]
type _ArrayLikeFloat_co = _DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.floating],
    float | bool,
]
type _ArrayLikeComplex_co = _DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.number], complex
]
type _ArrayLikeNumber_co = _DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.number], int | float | complex | bool
]
# string and bytes
type _ArrayLikeString_co = _DualArrayLike[
    np.dtype[np.character] | StringDType,
    bytes | str,
]
type _ArrayLikeStr_co = _DualArrayLike[np.dtype[np.str_], str]
type _ArrayLikeBytes_co = _DualArrayLike[np.dtype[np.bytes_], bytes]
type _ArrayLikeStringDtype_co = _DualArrayLike[StringDType, str]
type _ArrayLikeStrings_co = _ArrayLikeStr_co | _ArrayLikeBytes_co | _ArrayLikeStringDtype_co
# date
type _ArrayLikeDT64_co = _DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.str_ | np.datetime64],
    int | bool | str | datetime | date,
]
type _ArrayLikeTD64_co = _DualArrayLike[
    np.dtype[np.bool | np.bool_ | np.integer | np.timedelta64],
    bool | int | timedelta,
]
# None
type _ArrayLikeNone_co = _DualArrayLike[
    np.dtype[NoneType],
    NoneType,
]
# その他
type Typeaxis = _ShapeLike | None
"""`axis`専用の型ヒント"""
