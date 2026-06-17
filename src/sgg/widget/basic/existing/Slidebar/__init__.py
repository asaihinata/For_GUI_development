from tkinter import Scale

from ...common import *

__all__ = ["Slidebar"]


class Slidebar(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.value = num0(kw.get("value"))
        self.minval = num0(kw.get("min"))
        maxval = kw.get("max", 100)
        self.maxval = self.value if maxval < self.value else maxval
        self.orientation = listchose(kw.get("orientation"), ["horizontal", "vertical"])
        self.resolution = num0(kw.get("resolution"), 1)
        self.digits = num0(kw.get("digits"))
        self.length = num0(kw.get("length"), 200)
        self.borderwidth = num0(kw.get("bd"), 1)
        self.widget = Scale(
            self.master,
            takefocus=self.takefocus,
            relief=self.relief,
            cursor=self.cursor,
            fg=self.fg,
            bg=self.bg,
            font=self.font,
            from_=self.minval,
            to=self.maxval,
            orient=self.orientation,
            resolution=self.resolution,
            digits=self.digits,
            length=self.length,
            borderwidth=self.borderwidth,
        )
        self.set(self.value)

    def set(self, val):
        if nums(val):
            self.widget.set(val)

    def _get(self):
        return self.widget.get()

    def delta(self):
        self.widget.destroy()

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
