from tkinter import Label

from PIL.ImageTk import PhotoImage

from sgg.widget.base import Element

__all__ = ["Imagelink"]

class Imagelink(Element):
    @property
    def widget(self) -> Label: ...
    imgs: PhotoImage
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def show(self, title) -> None:
        """画像を表示させる"""
