from tkinter import IntVar, Spinbox

from sgg.dev import _is_real, bols, num0, nums, parsecolor
from sgg.widget.base import Element

__all__ = ["InputNumber"]


class InputNumber(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.min = nums(kw.get("min"), 0)
        self.max = nums(kw.get("max"), 100)
        self.increment = num0(kw.get("step"), 1)
        self.wrap = bols(kw.get("wrap"), False)
        self.width = self._dwh(kw.get("width"), 20)
        self.selectforeground = parsecolor(kw.get("selectfg"))
        self.selectbackground = parsecolor(kw.get("selectbg"))
        selectborderwidth = kw.get("selectborderwidth", 0)
        if _is_real(selectborderwidth) and 0 <= selectborderwidth:
            self.selectborderwidth = selectborderwidth
        else:
            self.selectborderwidth = 0
        self.insertbackground = parsecolor(kw.get("insertbg"), "#000000")
        self.insertwidth = num0(kw.get("insertwidth"), 2)
        self.insertontime = num0(kw.get("insertontime"), 600)
        self.insertofftime = num0(kw.get("insertofftime"), 300)
        insertborderwidth = kw.get("insertborderwidth", 0)
        if _is_real(insertborderwidth) and 0 <= insertborderwidth:
            self.insertborderwidth = insertborderwidth
        else:
            self.insertborderwidth = 0
        self.insertbackground = parsecolor(kw.get("insertbg"), "#000000")
        self.insertwidth = num0(kw.get("insertwidth"), 2)
        self.values = nums(kw.get("values"), 0)
        self.intval = IntVar(value=self.values)
        self.widget = Spinbox(
            self.master,
            bg=self.bg,
            borderwidth=self.borderwidth,
            cursor=self.cursor,
            fg=self.fg,
            font=self.font,
            from_=self.min,
            increment=self.increment,
            insertbackground=self.insertbackground,
            insertborderwidth=self.insertborderwidth,
            insertofftime=self.insertofftime,
            insertontime=self.insertontime,
            insertwidth=self.insertwidth,
            justify=self.justify,
            relief=self.relief,
            selectbackground=self.selectbackground,
            selectborderwidth=self.selectborderwidth,
            selectforeground=self.selectforeground,
            takefocus=self.takefocus,
            textvariable=self.intval,
            to=self.max,
            width=self.width,
            wrap=self.wrap,
        )

    def get_number(self):
        return self.widget.get()

    def delta(self):
        self.widget.destroy()
