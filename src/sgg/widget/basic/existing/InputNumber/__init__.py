from tkinter import IntVar, Spinbox

from ...common import *

__all__ = ["InputNumber"]


class InputNumber(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.min = nums(kw.get("min"), 0)
        self.max = nums(kw.get("max"), 100)
        self.increment = num0(kw.get("step"), 1)
        self.wrap = bols(kw.get("wrap"), False)
        self.width = self._dwh(kw.get("width"), 20)
        self.insertbackground = parsecolor(kw.get("insertbg"), "#000000")
        self.insertwidth = num0(kw.get("insertwidth"), 2)
        self.values = nums(kw.get("values"), 0)
        self.intval = IntVar(value=self.values)
        self.widget = Spinbox(
            self.master,
            textvariable=self.intval,
            takefocus=self.takefocus,
            insertbackground=self.insertbackground,
            insertwidth=self.insertwidth,
            relief=self.relief,
            cursor=self.cursor,
            from_=self.min,
            to=self.max,
            increment=self.increment,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            justify=self.justify,
            wrap=self.wrap,
            width=self.width,
            borderwidth=self.borderwidth,
        )

    def get_number(self):
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
