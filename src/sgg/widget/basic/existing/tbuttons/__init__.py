from tkinter import Variable
from tkinter.ttk import Button, Style

from sgg.dev import listchose, num0, parsecolor
from sgg.widget.base import Element

__all__ = ["TButtons"]


class TButtons(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.text = kw.get("text")
        self.textvariable = Variable(master, self.text)
        self.funcs = kw.get("function")
        self.wraplength = num0(kw.get("wraplength"))
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.shiftrelief = kw.get("shiftrelief")
        self.state = listchose(kw.get("anchor"), ["normal", "disabled"])
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
        self.stylename = f"Custom{kw.get("count")}.TButton"
        self.style = Style()
        self.style.configure(
            self.stylename,
            background=self.bg,
            foreground=self.fg,
            font=self.font,
            state=self.state,
        )
        self.widget = Button(
            self.master,
            command=lambda: self._exec_funcs(self.funcs),
            cursor=self.cursor,
            takefocus=self.takefocus,
            textvariable=self.textvariable,
            style=self.stylename,
        )

    def delta(self):
        self.widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.textvariable = Variable(self.master, self.text)
        self.widget.config(textvariable=self.textvariable)
