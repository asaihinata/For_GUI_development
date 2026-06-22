from tkinter import Scale

from .....typing import ColorType
from ....base import _Element

__all__ = ["Slidebar"]

class Slidebar(_Element):
    widget: Scale
    def get(self) -> int | float:
        """
        Slidebarウィジェットの現在の値を取得する

        :return: Slidebarウィジェットの現在の値を返す
        :rtype: int | float
        """

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

    def set(self, val: int | float) -> None:
        """
        Slidebarウィジェットの変更後の数値を設定する

        :param val: 変更後の数値を指定する
        :type val: int | float
        """
