from tkinter import BooleanVar
from tkinter.ttk import Checkbutton, Style

from sgg.dev import bols
from sgg.widget.base import Element

__all__ = ["TCheckbox"]


class TCheckbox(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.text = kw.get("text")
        self.default = bols(kw.get("default"), False)
        self.variable = BooleanVar(master, value=self.default)
        self.stylename = f"Custom{kw.get("count")}.TCheckbutton"
        self.style = Style()
        self.style.configure(
            self.stylename,
            background=self.bg,
            foreground=self.fg,
            font=self.font,
        )
        self.widget = Checkbutton(
            self.master,
            takefocus=self.takefocus,
            cursor=self.cursor,
            text=self.text,
            variable=self.variable,
            style=self.stylename,
            takefocus=self.takefocus,
        )

    def get_value(self):
        return self.variable.get()

    def set_value(self, value=None):
        self.variable.set(value if isinstance(value, bool) else self.variable.get())

    def delta(self):
        self.widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.widget.config(text=txt)
