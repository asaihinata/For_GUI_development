"""popup用の型ヒントのモジュール"""

from typing import Literal, TypeAlias

__all__ = ["Type_icon", "Literal"]
Type_icon: TypeAlias = Literal["error", "info", "question", "warning"]
