from tkinter import Label

from PIL.ImageTk import PhotoImage
from qrcode import make

from ...common import *

__all__ = ["QRImage"]


class QRImage(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.text = kw.get("text")
        self.img = make(self.text)
        self.image = PhotoImage(self.img)
        self.widget = Label(master, image=self.image, takefocus=self.takefocus)
        self.widget.image = self.image

    def delta(self):
        self.widget.destroy()

    def show(self):
        self.img.show()
