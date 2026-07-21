from typing import Any

import numpy as np
from numpy._typing import _NestedSequence, _SupportsArray, _SupportsDType
from numpy.dtypes import StringDType

__all__ = [
    "_DTypeLike",
    "_DualArrayLike",
    "_BoolDTypeLike",
    "_NumericDTypeLike",
    "_RealNumericDTypeLike",
    "_IntsNumericDTypeLike",
    "_FloatsNumericDTypeLike",
    "_ComplexDtypeLike",
    "_StringDTypeLike",
]
type _DTypeLike[ScalarT: np.generic] = (
    type[ScalarT] | np.dtype[ScalarT] | _SupportsDType[np.dtype[ScalarT]]
)
type _DualArrayLike[DTypeT: np.dtype, BuiltinT] = (
    _SupportsArray[DTypeT]
    | _NestedSequence[_SupportsArray[DTypeT]]
    | BuiltinT
    | _NestedSequence[BuiltinT]
)
# 真偽型
type _BoolDTypeLike = (
    type[bool]
    | np.dtype[np.bool_ | np.bool]
    | _SupportsDType[np.dtype[np.bool_ | np.bool]]
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
)
"""`実数`全般のdtype"""
type _IntsNumericDTypeLike = (
    type[bool]
    | type[int]
    | np.dtype[np.bool_ | np.integer[Any]]
    | _SupportsDType[np.dtype[np.bool_ | np.integer[Any]]]
    | str
)
"""`整数`全般のdtype"""
type _FloatsNumericDTypeLike = (
    type[float]
    | np.dtype[np.floating[Any]]
    | _SupportsDType[np.dtype[np.floating[Any]]]
    | str
)
"""`浮動小数型`全般のdtype"""
type _ComplexDtypeLike = (
    type[complex] | np.dtype[np.complexfloating] | np._ComplexFloatingCodes
)
"""`複素数`全般のdtype"""
# 文字列
type _StringDTypeLike = (
    type[str]
    | type[bytes]
    | np.dtype[np.flexible[Any] | StringDType]
    | _SupportsDType[np.dtype[np.flexible[Any] | StringDType]]
    | str
)
"""numpyとPythonの文字列全般の型の型ヒント"""
