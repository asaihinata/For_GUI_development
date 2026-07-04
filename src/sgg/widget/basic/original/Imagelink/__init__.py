from tkinter import Label

from PIL.ImageTk import PhotoImage
from requests import get
from requests.exceptions import RequestException
from ...common import *
from ...dev import Img_byte, linkcheck

__all__ = ["Imagelink"]


class Imagelink(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.link = kw.get("link")
        if not isinstance(self.link, str):
            self.widget = Label(master, text="image error", takefocus=self.takefocus)
        elif not linkcheck(self.link):
            self.widget = Label(master, text="image error", takefocus=self.takefocus)
        else:
            self.__img = Img_byte(_get_link_img(self.link)).asresize().image
            self.imgs = PhotoImage(self.__img)
            self.widget = Label(
                master, text=None, image=self.imgs, takefocus=self.takefocus
            )
            self.widget.image = self.imgs

    def delta(self):
        self.widget.destroy()

    def show(self, title=None):
        self.__img.show(title)

def _get_link_img(link):
    try:
        response = get(link)
        response.raise_for_status()
        return response.content
    except RequestException as e:
        raise RequestException(e)