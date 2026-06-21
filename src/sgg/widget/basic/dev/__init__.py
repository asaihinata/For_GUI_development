from io import BytesIO
from pathlib import Path, PosixPath, WindowsPath

from PIL import Image

__all__ = ["Img_path", "Img_byte"]


class Img_conversion:
    def __init__(self, data):
        self.__imgs = Image.open(data)

    @property
    def image(self):
        return self.__imgs

    @property
    def width(self):
        return self.__imgs.width

    def get_width(self):
        return self.__imgs.width

    @property
    def height(self):
        return self.__imgs.height

    def get_height(self):
        return self.__imgs.height

    @property
    def size(self):
        return self.__imgs.width, self.__imgs.height

    def get_size(self):
        return self.__imgs.width, self.__imgs.height

    @property
    def format(self):
        return self.__imgs.format

    def get_format(self):
        return self.__imgs.format

    @property
    def mode(self):
        return self.__imgs.mode

    def get_mode(self):
        return self.__imgs.mode

    def show(self, title=None):
        self.__imgs.show(title)

    def resize(self, w, h):
        if not isinstance(w, int):
            raise TypeError("wには整数型を指定してください")
        elif w <= 1:
            raise ValueError("wには1以上の整数を指定してください")
        if not isinstance(h, int):
            raise TypeError("hには整数型を指定してください")
        elif h <= 1:
            raise ValueError("hには1以上の整数を指定してください")
        self.__imgs.resize((w, h))
        return self

    def asresize(self):
        self.__imgs.resize(self.get_size())
        return self


class Img_path(Img_conversion):
    def __init__(self, path):
        if not isinstance(path, Path | PosixPath | WindowsPath):
            raise TypeError("pathにはpathlib.Pathを指定してください")
        self.path = path
        super().__init__(self.path)


class Img_byte(Img_conversion):
    def __init__(self, byte):
        if not isinstance(byte, bytes | BytesIO):
            raise TypeError("byteにはbytes型もしくはBytesIO型で指定してください")
        if isinstance(byte, bytes):
            self.byte = BytesIO(byte)
        else:
            self.byte = byte
        super().__init__(self.byte)
