"""popup用の型ヒントのモジュール"""

from typing import Literal as L, TypeAlias

__all__ = ["Type_icon", "L"]
Type_icon: TypeAlias = L["error", "info", "question", "warning"]
