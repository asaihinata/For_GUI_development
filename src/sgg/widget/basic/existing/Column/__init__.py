from tkinter import Frame

from sgg.widget.base import Element

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
