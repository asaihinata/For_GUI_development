from tkinter import Button

from ...common import *

__all__ = ["Buttons"]


class Buttons(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.funcs = kw.get("function")
        self.text = kw.get("text")
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
            takefocus=self.takefocus,
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
            command=lambda: self._exec_funcs(self.funcs),
            width=self.width,
            height=self.height,
            borderwidth=self.borderwidth,
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
