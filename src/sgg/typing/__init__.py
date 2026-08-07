"""フレームワーク全体で使用する型を設定しているモジュール"""

from typing import Any

from numpy.random import SeedSequence,Generator

from ._array_date_unit import *
from ._array_dtype import *
from ._arraylike import *
from ._kwarg import *
from ._scalar import *
from ._widget import *

type Incomplete = Any
type _Seed = int | SeedSequence | Generator | None
__all__ = (
    ["Incomplete", "_Seed"]
    + getattr(_array_date_unit, "__all__", [])
    + getattr(_array_dtype, "__all__", [])
    + getattr(_arraylike, "__all__", [])
    + getattr(_kwarg, "__all__", [])
    + getattr(_scalar, "__all__", [])
    + getattr(_widget, "__all__", [])
)
