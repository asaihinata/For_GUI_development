from tkinter import *

from sgg._typing import ColorType
from sgg.widget.element import Element

class Btn(Element):
    @property
    def widget(self) -> Button: ...
    wraplength: float | int
    textvariable: Variable
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def get_text(self) -> str:
        """ウィジェットが表示している文字を取得する"""

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

    def dgettitle(self) -> str:
        """
        ダイアログに表示されるタイトルを取得する

        :return: ダイアログで表示されるタイトルを返す
        :rtype: str
        """

    def dsettitle(self, titles: str) -> None:
        """ダイアログに表示されるタイトルを変更する"""

    def _textvariable(self, txt: str) -> None: ...
