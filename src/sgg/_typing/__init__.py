"""フレームワーク全体で使用する型を設定しているモジュール"""

from typing import Any, Literal

from numpy._typing import _NestedSequence
from numpy.random import Generator, SeedSequence

from ._array_date_unit import *
from ._array_dtype import *
from ._arraylike import *
from ._kwarg import *
from ._scalar import *
from ._timezone import *
from ._widget import *

type Incomplete = Any
type _Seed = int | SeedSequence | Generator | None
type _orderKACF = Literal["K", "A", "C", "F"] | None
__all__ = (
    ["_NestedSequence", "_Seed", "Incomplete", "_orderKACF"]
    + getattr(_array_date_unit, "__all__", [])
    + getattr(_array_dtype, "__all__", [])
    + getattr(_arraylike, "__all__", [])
    + getattr(_kwarg, "__all__", [])
    + getattr(_scalar, "__all__", [])
    + getattr(_timezone, "__all__", [])
    + getattr(_widget, "__all__", [])
)
