from tkinter.ttk import Entry
from typing import Literal

from sgg._typing import ColorType
from sgg.widget.element import TElement

__all__ = ["TInput"]

class TInput(TElement):
    @property
    def widget(self) -> Entry: ...
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
    # select
    def selection_range(
        self, start: str | int, end: str | int | Literal["end"]
    ) -> None:
        """選択範囲の開始位置を指定する"""

    def selection_present(self) -> bool:
        """テキストの選択状態を判定する"""

    def selection_clear(self) -> None:
        """テキストの選択状態を解除する"""

    def focus_set(self) -> None:
        """テキストにフォーカスさせる"""

    def selection_set(self) -> None:
        """テキストにフォーカスさせる"""
