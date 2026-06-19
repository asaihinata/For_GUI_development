from tkinter import LabelFrame

from ...common import *

__all__ = ["Frames"]


class Frames(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.borderwidth = num0s(kw.get("borderwidth"), 1)
        self.title = kw.get("title")
        self.relief = listchose(
            kw.get("relief"),
            ["solid", "flat", "raised", "sunken", "ridge", "groove"],
        )
        self.labelanchor = listchose(
            kw.get("labelanchor"),
            ["nw", "n", "ne", "en", "e", "es", "se", "s", "sw", "ws", "w", "wn"],
        )
        self.widget = LabelFrame(
            self.master,
            takefocus=self.takefocus,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            cursor=self.cursor,
            labelanchor=self.labelanchor,
            text=self.title,
            font=self.font,
            bg=self.bg,
            fg=self.fg,
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
