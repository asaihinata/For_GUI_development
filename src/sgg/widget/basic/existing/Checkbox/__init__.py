from tkinter import BooleanVar, Checkbutton

from ...common import *

__all__ = ["Checkbox"]


class Checkbox(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.wraplength = num0(kw.get("wraplength"))
        self.text = kw.get("text")
        self.default = bols(kw.get("default"), False)
        self.variable = BooleanVar()
        self.widget = Checkbutton(
            self.master,
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
        if self.default:
            self.widget.select()
            self.variable.set(True)
        else:
            self.widget.deselect()
            self.variable.set(False)

    def get_value(self):
        return self.variable.get()

    def set_value(self, value=None):
        self.variable.set(
            value if isinstance(value, bool) else (not self.variable.get())
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
