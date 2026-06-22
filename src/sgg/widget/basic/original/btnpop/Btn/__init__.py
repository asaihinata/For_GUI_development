from tkinter import Button

from ......dialogs import *
from ....common import *


class Btn(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.anchor = listchose(
            kw.get("anchor"), ["center", "w", "n", "s", "e", "nw", "ne", "se", "sw"]
        )
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.wraplength = num0(kw.get("wraplength"))
        self.widget: Button

    def dgettitle(self):
        return self.title

    def dsettitle(self, titles):
        self.title = titles

    def delta(self):
        self.widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.widget.config(text=txt)

    def set_fg(self, fg):
        self.fg = parsecolor(fg, self.fg)
        self.widget.config(fg=self.fg)

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.widget.config(bg=self.bg)

    def get_fg(self):
        return self.fg

    def get_bg(self):
        return self.bg
