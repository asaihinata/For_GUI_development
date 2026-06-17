from tkinter import Spinbox

from .....typing import ColorType
from ....base import _Element

__all__ = ["InputNumber"]

class InputNumber(_Element):
    widget: Spinbox
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

    def get_number(self) -> int | float:
        """
        InputNumberウィジェットに入力されている数値を取得する

        :return: InputNumberウィジェットに入力されている数値を返す
        :rtype: int|float
        """
