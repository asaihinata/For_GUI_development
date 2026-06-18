from os import getcwd

from ..btn import *

__all__ = ["FolderLoad"]


class FolderLoad(Btn):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__path = None
        self.title = kw.get("title", "select Folder")
        self.text = kw.get("text", "select Folder")
        self.widget = Button(
            master,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            command=self._choosefolder,
            borderwidth=self.borderwidth,
        )

    def __fspath__(self):
        return self.path

    @property
    def path(self):
        return self.__path

    def get_path(self):
        return self.__path

    def _choosefolder(self):
        self.__path = askdirectory(title=self.title, initialdir=getcwd())
        if self.__path == "":
            self.__path = None
        return self.__path
