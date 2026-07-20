from typing import Any

import numpy as np
from numpy._typing import (_DTypeLikeComplex, _NestedSequence, _SupportsArray,
                           _SupportsDType)
from numpy.dtypes import StringDType

__all__ = [
    "_ArrayLikeAnyString_co",
    "_ComplexDtypeLike",
    "_NumericDTypeLike",
    "_RealNumericDTypeLike",
]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
# 数値
type _NumericDTypeLike = (
    type[bool]
    | type[int]
    | type[float]
    | type[complex]
    | np.dtype[np.bool_ | np.number[Any]]
    | _SupportsDType[np.dtype[np.bool_ | np.number[Any]]]
    | str
)
"""数値全般のdtype"""
type _RealNumericDTypeLike = (
    type[bool]
    | type[int]
    | type[float]
    | np.dtype[np.bool_ | np.integer[Any] | np.floating[Any]]
    | _SupportsDType[np.dtype[np.bool_ | np.integer[Any] | np.floating[Any]]]
    | str
)
"""`実数`全般のdtype"""
type _ComplexDtypeLike = _DTypeLikeComplex
"""`複素数`全般のdtype"""
# 文字列
type _ArrayLikeAnyString_co = _DualArrayLike[
    np.dtype[np.character] | StringDType,
    bytes | str,
]
"""numpyとPythonの文字列全般の型の型ヒント"""
