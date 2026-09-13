from tkinter import Label

from PIL.ImageTk import PhotoImage

from sgg.widget.base import Element
from sgg.widget.basic.dev import Img_byte

__all__ = ["Imagebytes"]


class Imagebytes(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__img = Img_byte(kw.get("bytes"))
        self.imgs = PhotoImage(image=self.__img.image)
        self._widget = Label(
            master, text=None, image=self.imgs, takefocus=self.takefocus
        )
        self._widget.image = self.imgs

    def delta(self):
        self._widget.destroy()

    def show(self):
        self.__img.image.show()

    def bytesdate(self):
        return self.__img.byte

    def __bytes__(self):
        return self.__img.byte