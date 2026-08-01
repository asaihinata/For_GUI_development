from typing import Literal

__all__ = ["ColorType", "ColorTypeN", "Type_icon"]
# 色
type ColorType = str
type ColorTypeN = str | None
# dialogのアイコン
type Type_icon = Literal["error", "info", "question", "warning"]
