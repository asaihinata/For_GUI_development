from tkinter import BooleanVar, Checkbutton, Variable

from sgg.dev import bols, num0, parsecolor
from sgg.widget.element import Element

__all__ = ["Checkbox"]


class Checkbox(Element):
    _groups = {}

    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.wraplength = num0(kw.get("wraplength"))
        self.textvariable = Variable(value=kw.get("text"))
        self.check = bols(kw.get("check"), False)
        group = kw.get("group", "default")
        self.group = group if isinstance(group, str) else "default"
        self.selectcolor = parsecolor(kw.get("selectcolor", "white"), "white")
        self.activebg = parsecolor(kw.get("activebg"), "#97a4b3")
        self.activefg = parsecolor(kw.get("activefg"), "white")
        self.variable = BooleanVar(value=self.check)
        self._widget = Checkbutton(
            self.master,
            activebackground=self.activebg,
            activeforeground=self.activefg,
            anchor=self.anchor,
            bg=self.bg,
            borderwidth=self.borderwidth,
            cursor=self.cursor,
            fg=self.fg,
            font=self.font,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            selectcolor=self.selectcolor,
            takefocus=self.takefocus,
            textvariable=self.textvariable,
            variable=self.variable,
            wraplength=self.wraplength,
        )
        if self.group not in self._groups:
            self._groups[self.group] = [self._widget]
        else:
            self._groups[self.group].append(self._widget)

    def delta(self):
        self._widget.destroy()

    def get_value(self):
        return self.variable.get()

    def set_value(self, value=None):
        if isinstance(value, bool):
            self.variable.set(value)

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, txt):
        self.textvariable.set(txt)
        self._widget.config(textvariable=self.textvariable)
