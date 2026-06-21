from pathlib import Path, PosixPath, WindowsPath
from tkinter import Label

from PIL.ImageTk import PhotoImage

from ...common import *
from ...dev import Img_path

__all__ = ["Images"]


class Images(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        path = kw.get("path")
        if isinstance(path, WindowsPath | PosixPath | Path):
            self.path = path
        elif isinstance(path, str):
            self.path = Path(path)
            if not self.path.exists():
                raise FileNotFoundError("ファイルが存在しません")
        else:
            raise TypeError(
                "pathには以下の型を指定してください\nstr,WindowsPath,PosixPath,Path"
            )
        self.__img = Img_path(self.path)
        self.__img = self.__img.asresize().image
        self.imgs = PhotoImage(image=self.__img)
        self.widget = Label(
            master, text=None, image=self.imgs, takefocus=self.takefocus
        )
        self.widget.image = self.imgs

    def delta(self):
        self.widget.destroy()

    def show(self, title=None):
        self.__img.show(title)
