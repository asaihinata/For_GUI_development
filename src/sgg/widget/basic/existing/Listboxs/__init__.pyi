from tkinter import Listbox

from .....typing import Any, ColorType, Literal
from ....base import _Element

__all__ = ["Listboxs"]

class Listboxs(_Element):
    widget: Listbox
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

    def select_set(self, val: int) -> None:
        """
        読み込み時にListboxsウィジェットで選択される項目を指定する

        :param val: 読み込み時にListboxsウィジェットで選択される項目を指定する
        :type val: int
        """

    def apend(self, place: int | Literal["end"] = "end", lists: list = []) -> None:
        """
        Listboxsウィジェットに項目を追加する

        :param lists: Listboxsウィジェットに追加する項目を指定する
        :type lists: list
        :param place: 追加する場所を指定する
        :type place: int|Literal["end"]
        """

    def clear(self) -> None:
        """Listboxsウィジェットの項目を全て削除する"""

    def dele(self, *index: int) -> None:
        """
        Listboxsウィジェットの指定された箇所の項目を削除する

        :param index: Listboxsウィジェットの削除したい項目の箇所を指定する
        :type index: int
        """

    def lens(self) -> int:
        """
        Listboxsウィジェットの項目数を取得する

        :return: Listboxsウィジェットの項目数を取得する
        :rtype: int
        """

    def select(self) -> tuple[int]:
        """
        Listboxsウィジェットで選択された項目をタプルで返す

        :return: Listboxsウィジェットで選択された項目を返す
        :rtype: tuple[int]
        """

    def select_val(self) -> list[Any] | Any:
        """
        Listboxsウィジェットで選択された項目の表記を返す

        :return: Listboxsウィジェットで選択された項目の表記を返す
        :rtype: list[Any]|Any
        """

    def set(self, lists: tuple[str, ...]) -> None:
        """
        Listboxsウィジェットの項目をlitsに置き換える

        :param lists: 新しく表示させたいListboxsウィジェットの項目を指定する
        :type lists: tuple[str,...]
        """
