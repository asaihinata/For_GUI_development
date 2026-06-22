from tkinter import Text

from .....typing import ColorType, Literal
from ....base import _Element

__all__ = ["Multiline"]

class Multiline(_Element):
    widget: Text
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

    def inserts(self, text: str = "", place: int | Literal["end"] = "end") -> None:
        """
        挿入する位置を指定し,Multilineウィジェットにその指定した場所のテキストを挿入する

        :param text: 挿入する文字を指定する
        :type text: str
        :param place: 文字を挿入する場所を指定する
        :type place: int | Literal["end"]
        """

    def get_text(self) -> str:
        """
        Multilineウィジェットに記入されている文字を取得する

        :return: Multilineウィジェットに記入されている文字を返す
        :rtype: str
        """

    def all_delta(self) -> None:
        """Multilineウィジェット内の文字を全て削除する"""
