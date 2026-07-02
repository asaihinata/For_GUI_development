from typing import TypeAlias, TypeAliasType, TypeVar

import numpy as np
from numpy._typing import _CharLike_co, _FloatLike_co, _IntLike_co, _UIntLike_co

_ShapeT = TypeVar("_ShapeT", bound=np._Shape, default=np._AnyShape, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype, default=np.dtype, covariant=True)

TypeNumber: TypeAlias = _FloatLike_co | _IntLike_co | _UIntLike_co
_NumberT = TypeAliasType("_NumberT", TypeNumber)
TypeStr: TypeAlias = _CharLike_co | np.character
_StrT = TypeAliasType("_StrT", TypeStr)
