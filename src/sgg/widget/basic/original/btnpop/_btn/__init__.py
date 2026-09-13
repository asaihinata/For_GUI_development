from tkinter import Button, Variable

from sgg._list import ANCHOR_LIST
from sgg.dev import listchose, num0, parsecolor
from sgg.widget.base import Element


class Btn(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.anchor = listchose(kw.get("anchor"), ANCHOR_LIST, "center")
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.wraplength = num0(kw.get("wraplength"))
        self._widget: Button

    def dgettitle(self):
        return self.title

    def dsettitle(self, titles):
        self.title = titles

    def delta(self):
        self._widget.destroy()

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, txt):
        self.textvariable.set(txt)
        self._widget.config(textvariable=self.textvariable)

    def _textvariable(self, txt):
        self.textvariable = Variable(value=txt)
