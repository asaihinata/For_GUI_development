from tkinter import Label

from ....base import _Element

__all__ = ["Images"]

class Images(_Element):
    widget: Label
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def show(self, title: str | None = None) -> None:
        """
        画像を表示させる

        :param title: タイトルを指定する
        :type title: str|None
        """
