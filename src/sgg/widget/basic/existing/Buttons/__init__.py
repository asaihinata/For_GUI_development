from tkinter import Button

from sgg.dev import listchose, num0, parsecolor
from sgg.widget.base import Element

__all__ = ["Buttons"]


class Buttons(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.text = kw.get("text")
        self.funcs = kw.get("function")
        self.wraplength = num0(kw.get("wraplength"))
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.anchor = listchose(
            kw.get("anchor"),
            [
                "center",
                "w",
                "n",
                "s",
                "e",
                "nw",
                "ne",
                "se",
                "sw",
            ],
        )
        self.widget = Button(
            self.master,
            anchor=self.anchor,
            bg=self.bg,
            borderwidth=self.borderwidth,
            command=lambda: self._exec_funcs(self.funcs),
            cursor=self.cursor,
            fg=self.fg,
            font=self.font,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            takefocus=self.takefocus,
            text=self.text,
            width=self.width,
            wraplength=self.wraplength,
        )

    def delta(self):
        self.widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.widget.config(text=txt)
