from tkinter import Label

from PIL.ImageTk import PhotoImage

from ....base import _Element

__all__ = ["QRImage"]

class QRImage(_Element):
    imgs: PhotoImage
    widget: Label
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def show(self) -> None:
        """QRコードを表示させる"""
