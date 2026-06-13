from io import BytesIO
from tkinter import Label

from PIL.ImageTk import PhotoImage
from barcode import get_class
from barcode.writer import ImageWriter

from ...common import *
from ...dev import Img_byte

__all__ = ["Barcode"]
support_barcode = [
    "codabar",
    "code128",
    "code39",
    "ean",
    "ean13",
    "ean13-guard",
    "ean14",
    "ean8",
    "ean8-guard",
    "gs1",
    "gs1_128",
    "gtin",
    "isbn",
    "isbn10",
    "isbn13",
    "issn",
    "itf",
    "jan",
    "nw-7",
    "pzn",
    "upc",
    "upca",
]


class Barcode(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.master = master
        self.data = kw.get("data", "")
        self.format = kw.get("format", "code39")
        self.barcode = barcode_data(self.data, self.format)
        self.__img = Img_byte(self.barcode.bytedata).imgs
        self.imgs = PhotoImage(image=self.__img)
        self.widget = Label(
            master, text=None, image=self.imgs, takefocus=self.takefocus
        )
        self.widget.image = self.imgs

    def delta(self):
        self.widget.destroy()

    def show(self, title=None):
        self.__img.show(title)


class barcode_data:
    byte_buffer = BytesIO()

    def __init__(self, value, format="code39"):
        self.format = format if format in support_barcode else "code39"
        self.classbarcode = get_class(self.format)
        self.barcodes = self.classbarcode(value, writer=ImageWriter())
        self.barcodes.write(self.byte_buffer)
        self.byte_buffer.seek(0)
        self.bytedata = self.byte_buffer.read()

    def get_type(self):
        return self.classbarcode.name
