"""フレームワーク全体で使用する型を設定しているモジュール"""

from typing import Any

from ._array_date_unit import *
from ._array_dtype import *
from ._arraylike import *
from ._scalar import *
from ._widget_all import *
from ._widget_graph import *

type Incomplete = Any
__all__ = (
    ["Incomplete"]
    + getattr(_array_date_unit, "__all__", [])
    + getattr(_array_dtype, "__all__", [])
    + getattr(_arraylike, "__all__", [])
    + getattr(_scalar, "__all__", [])
    + getattr(_widget_all, "__all__", [])
    + getattr(_widget_graph, "__all__", [])
)
