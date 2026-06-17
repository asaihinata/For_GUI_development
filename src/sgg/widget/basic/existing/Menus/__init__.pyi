from tkinter import Menu

from .....typing import ColorType
from ....base import _Element

__all__ = ["Menus"]

class Menus(_Element):
    widget: Menu
    def get(self) -> list:
        """
        Menusウィジェットで表示されている配列を取得する

        :return: Menusウィジェットで表示されている配列を返す
        :rtype: list
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

    def clear(self) -> None:
        """Menusウィジェットのlistを空にしMenusウィジェットを非表示にする"""

    def addmenu(self, label: str, submenu_lists: list) -> None:
        """
        Menusウィジェットに新しくメニューを追加する

        :param label: メニューの表示文字を指定する
        :type label: str
        :param submenu_lists: メニューに追加させるドロップダウンを指定する
        :type submenu_lists: list
        """
