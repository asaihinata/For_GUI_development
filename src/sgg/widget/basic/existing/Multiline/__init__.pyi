from tkinter import INSERT, Text
from typing import Literal

from sgg._typing import ColorType, RStr_
from sgg.widget.base import _Element

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

    def mark_set(self, index: str, name: str = INSERT) -> None:
        """
        `index`の位置に`name`というマーカー名を追加する

        :param index: 追加する位置を`行.文字数`という形式で指定する
        :type index: str
        :param name: マーカー名を指定する
        :type name: str
        :raises TypeError: `index`もしくは`name`に文字列で指定しない場合に発生させる
        """

    def index(self, name: str) -> str | None:
        """`mark_set`で指定した`name`の`index`の位置を取得する"""

    @property
    def mark_list(self) -> list[str]:
        """`mark_set`で指定した`name`の配列を返す"""

    def focus_set(self):
        """`Multiline`ウィジェットにカーソルを表示させる"""
