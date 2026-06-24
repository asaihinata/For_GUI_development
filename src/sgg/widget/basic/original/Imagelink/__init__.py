from tkinter import Label

from PIL.ImageTk import PhotoImage

from ...common import *
from ...dev import Img_byte, linkcheck
from .getdata import get_link_img

__all__ = ["Imagelink"]


class Imagelink(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.link = kw.get("link")
        if not isinstance(self.link, str):
            raise TypeError("linkにはstr型を指定してください")
        if not linkcheck(self.link):
            raise ValueError("サイトが存在しません")
        self.__img = Img_byte(get_link_img(self.link)).asresize().image
        self.imgs = PhotoImage(self.__img)
        self.widget = Label(
            master, text=None, image=self.imgs, takefocus=self.takefocus
        )
        self.widget.image = self.imgs

    def delta(self):
        self.widget.destroy()

    def show(self, title=None):
        self.__img.show(title)
