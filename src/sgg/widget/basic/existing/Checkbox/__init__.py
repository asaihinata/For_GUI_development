from tkinter import BooleanVar, Checkbutton

from sgg.dev import bols, num0, parsecolor
from sgg.widget.base import Element

__all__ = ["Checkbox"]


class Checkbox(Element):
    _groups = {}

    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.wraplength = num0(kw.get("wraplength"))
        self.text = kw.get("text")
        self.check = bols(kw.get("check"), False)
        group = kw.get("group", "default")
        self.group = group if isinstance(group, str) else "default"
        self.selectcolor = parsecolor(kw.get("selectcolor", "white"), "white")
        self.activebg = parsecolor(kw.get("activebg"))
        self.activefg = parsecolor(kw.get("activefg"))
        self.variable = BooleanVar(value=self.check)
        self.widget = Checkbutton(
            self.master,
            activebackground=self.activebg,
            activeforeground=self.activefg,
            selectcolor=self.selectcolor,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            text=self.text,
            variable=self.variable,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            borderwidth=self.borderwidth,
        )
        if self.group not in self._groups:
            self._groups[self.group] = [self.widget]
        else:
            self._groups[self.group].append(self.widget)

    def delta(self):
        self.widget.destroy()

    def get_value(self):
        return self.variable.get()

    def set_value(self, value=None):
        if isinstance(value, bool):
            self.variable.set(value)

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.widget.config(text=txt)
