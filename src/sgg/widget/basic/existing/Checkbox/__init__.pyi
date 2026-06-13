from tkinter import Checkbutton

from .....typing import ColorType
from ....base import _Element

__all__ = ["Checkbox"]

class Checkbox(_Element):
    widget: Checkbutton
    def delta(self):
        """ウィジェットを削除する。"""

    def get_text(self) -> str:
        """ウィジェットが表示している文字を取得する。"""

    def set_text(self, txt: str):
        """ウィジェットが表示している文字を変更する。"""

    def get_fg(self) -> ColorType:
        """ウィジェットが表示している文字色を取得する。"""

    def set_fg(self, fg: ColorType):
        """ウィジェットが表示している文字色を変更する。"""

    def get_bg(self) -> ColorType:
        """ウィジェットが表示している背景色を取得する。"""

    def set_bg(self, bg: ColorType):
        """ウィジェットが表示している背景色を変更する。"""

    def get_value(self) -> bool:
        """Checkboxウィジェットにチェックされているか判定する。未チェックの場合Falseを返す。

        :return: Checkboxウィジェットにチェックされているか判定する。
        :rtype: bool"""

    def set_value(self, value: bool):
        """Checkboxウィジェットのチェック状態を変更する。valueにbool型以外を指定した場合,Checkboxウィジェットのチェック状態の逆の状態を設置させる。

        :param value: チェック状態を指定する。チェック状態にする場合Trueを,未チェック状態にする場合Falseを指定する。
        :type value: bool"""
