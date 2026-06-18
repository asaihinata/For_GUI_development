from tkinter import Label

from ...common import *

__all__ = ["Texts"]


class Texts(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.text = kw.get("text")
        self.wraplength = num0(kw.get("wraplength"))
        self.widget = Label(
            self.master,
            takefocus=self.takefocus,
            borderwidth=self.borderwidth,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            justify=self.justify,
        )

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
