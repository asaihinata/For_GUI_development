from tkinter import Entry

from .....typing import ColorType, Literal
from ....base import _Element

__all__ = ["Input"]

class Input(_Element):
    widget: Entry
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def get_text(self) -> str:
        """
        Inputウィジェットに記入されている文字を取得する

        :return: Inputウィジェットに記入されている文字を返す
        :rtype: str
        """

    def set_text(self, txt: str) -> None:
        """ウィジェットが表示している文字を変更する"""

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
        挿入する位置を指定し,Inputウィジェットにその指定した場所のテキストを挿入する

        :param text: 挿入する文字を指定する
        :type text: str
        :param place: 文字を挿入する場所を指定する
        :type place: int | Literal["end"]
        """

    def select_judge(self) -> bool:
        """
        Inputウィジェット内の文字が現在選択状態かを返す

        :return: Inputウィジェット内の文字が現在選択状態かを返す
        :rtype: bool
        """

    def select_cansel(self) -> None:
        """Inputウィジェット内の選択状態を解除する"""

    def all_delta(self) -> None:
        """Inputウィジェット内の文字を全て削除する"""
