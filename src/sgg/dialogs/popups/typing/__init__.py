"""popup用の型ヒントのモジュール"""

from typing import Literal, TypeAlias

__all__ = ["Literal", "Type_icon"]
Type_icon: TypeAlias = Literal["error", "info", "question", "warning"]
