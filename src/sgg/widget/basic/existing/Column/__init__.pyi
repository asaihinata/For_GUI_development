from tkinter import Frame

from .....typing import ColorType
from ....base import _Element

__all__ = ["Column"]

class Column(_Element):
    widget: Frame
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def get_fg(self) -> ColorType:
        """ウィジェットが表示している文字色を取得する"""

    def set_fg(self, fg: ColorType) -> None:
        """ウィジェットが表示している文字色を変更する"""

    def get_bg(self) -> ColorType:
        """ウィジェットが表示している背景色を取得する"""

    def set_bg(self, bg: ColorType) -> None:
        """ウィジェットが表示している背景色を変更する"""
