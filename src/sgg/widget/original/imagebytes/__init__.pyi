from tkinter import Label

from PIL.ImageTk import PhotoImage

from sgg._typing import *
from sgg.widget.element import Element

__all__ = ["Imagebytes"]

class Imagebytes(Element):
    @property
    def widget(self) -> Label: ...
    imgs: PhotoImage
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def show(self) -> None:
        """画像を表示させる"""

    def bytesdate(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
