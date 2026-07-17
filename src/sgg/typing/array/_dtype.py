from typing import TypeAliasType, TypeVar

import numpy as np
from numpy._typing import (_CharLike_co, _ComplexLike_co, _FloatLike_co,
                           _IntLike_co, _UIntLike_co)

__all__ = ["_CharType", "_DTypeT", "_NumberT", "_StrT", "TypeNumber", "TypeStr"]
_DTypeT = TypeVar("_DTypeT", bound=np.generic, default=np.dtype, covariant=True)
_CharType = TypeVar(
    "CharType", bound=np.dtype, default=np.dtype[np.str_], covariant=True
)
type TypeNumber = (
    _FloatLike_co | _IntLike_co | _UIntLike_co | np.generic | _ComplexLike_co
)
type TypeStr = _CharLike_co | np.character
_NumberT = TypeAliasType("_NumberT", TypeNumber)
_StrT = TypeAliasType("_StrT", TypeStr)
