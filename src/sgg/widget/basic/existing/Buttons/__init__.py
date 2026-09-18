from tkinter import Button, Variable

from sgg._list import ANCHOR_LIST
from sgg.dev import listchose, num0, parsecolor
from sgg.widget.element import Element

__all__ = ["Buttons"]


class Buttons(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.textvariable = Variable(value=kw.get("text"))
        self.funcs = kw.get("function")
        self.default = listchose(kw.get("default"), ["normal", "active", "disabled"])
        self.wraplength = num0(kw.get("wraplength"))
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.anchor = listchose(kw.get("anchor"), ANCHOR_LIST, "center")
        self._widget = Button(
            self.master,
            anchor=self.anchor,
            bg=self.bg,
            borderwidth=self.borderwidth,
            command=lambda: self._exec_funcs(self.funcs),
            cursor=self.cursor,
            default=self.default,
            fg=self.fg,
            font=self.font,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            takefocus=self.takefocus,
            textvariable=self.textvariable,
            width=self.width,
            wraplength=self.wraplength,
        )

    def delta(self):
        self._widget.destroy()

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, text):
        self.textvariable.set(text)
        self._widget.config(textvariable=self.textvariable)
