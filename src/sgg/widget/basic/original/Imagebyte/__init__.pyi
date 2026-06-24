from tkinter import Label

from PIL.ImageTk import PhotoImage

from .....typing import *
from ....base import _Element

__all__ = ["Imagebyte"]

class Imagebyte(_Element):
    imgs: PhotoImage
    widget: Label
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def show(self, title: str | None = None) -> None:
        """
        画像を表示させる

        :param title: タイトルを指定する
        :type title: str | None
        """
