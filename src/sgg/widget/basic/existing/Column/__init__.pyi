from tkinter import Frame

from sgg._typing import ColorType
from sgg.widget.element import Element

__all__ = ["Column"]

class Column(Element):
    @property
    def widget(self) -> Frame: ...
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
