from tkinter import Label, Variable

from sgg.dev import num0
from sgg.widget.element import Element

__all__ = ["Texts"]


class Texts(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.textvariable = Variable(value=kw.get("text"))
        self.wraplength = num0(kw.get("wraplength"))
        self._widget = Label(
            self.master,
            takefocus=self.takefocus,
            borderwidth=self.borderwidth,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            textvariable=self.textvariable,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            justify=self.justify,
        )

    def delta(self):
        self._widget.destroy()

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, txt):
        self.textvariable.set(value=txt)
        self._widget.config(textvariable=self.textvariable)
