from tkinter import Frame

from ...common import *

__all__ = ["Column"]


class Column(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.widget = Frame(
            self.master,
            takefocus=self.takefocus,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            cursor=self.cursor,
            bg=self.bg,
            borderwidth=self.borderwidth,
        )

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
