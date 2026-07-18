from typing import Any

import numpy as np
from numpy._typing import _NestedSequence, _SupportsArray, _SupportsDType
from numpy.dtypes import StringDType

__all__ = ["_ArrayLikeAnyString_co", "_NumericDTypeLike"]
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
type _NumericDTypeLike = (
    type[bool]
    | type[int]
    | type[float]
    | type[complex]
    | np.dtype[np.bool_ | np.number[Any]]
    | _SupportsDType[np.dtype[np.bool_ | np.number[Any]]]
    | str
)
type _ArrayLikeAnyString_co = _DualArrayLike[
    np.dtype[np.character] | StringDType,
    bytes | str,
]
"""numpyとPythonの文字列全般の型の型ヒント"""
