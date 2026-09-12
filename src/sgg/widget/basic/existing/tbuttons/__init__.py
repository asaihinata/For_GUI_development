from tkinter import Variable
from tkinter.ttk import Button, Style

from sgg._list import ANCHOR_LIST
from sgg.dev import listchose, num0, parsecolor
from sgg.widget.base import TElement

__all__ = ["TButtons"]


class TButtons(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.text = kw.get("text")
        self.textvariable = Variable(master, self.text)
        self.funcs = kw.get("function")
        self.wraplength = num0(kw.get("wraplength"))
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.shiftrelief = kw.get("shiftrelief")
        self.state = listchose(kw.get("state"), ["normal", "disabled"])
        self.anchor = listchose(kw.get("anchor"), ANCHOR_LIST, "center")
        self.stylename = f"Custom{kw.get("count")}.TButton"
        self.style_list = [self.stylename]
        self.style = Style()
        self.style.configure(
            self.stylename,
            background=self.bg,
            foreground=self.fg,
            font=self.font,
            state=self.state,
        )
        self._widget = Button(
            self.master,
            command=lambda: self._exec_funcs(self.funcs),
            cursor=self.cursor,
            takefocus=self.takefocus,
            textvariable=self.textvariable,
            style=self.stylename,
        )

    def delta(self):
        self._widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.textvariable = Variable(self.master, self.text)
        self._widget.config(textvariable=self.textvariable)
