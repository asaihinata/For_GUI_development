from tkinter import Variable
from tkinter.ttk import Entry, Style

from sgg.dev import _is_real, listchose, num0, parsecolor
from sgg.widget.base import TElement

__all__ = ["TInput"]


class TInput(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.width = num0(kw.get("width"), 20)
        self.text = kw.get("text")
        self.textvariable = Variable(value=self.text)
        self.show = kw.get("show")
        self.state = listchose(kw.get("state"), ["normal", "disabled", "readonly"])
        self.disabledbg = parsecolor(kw.get("disabledbg"))
        self.disabledfg = parsecolor(kw.get("disabledfg"))
        self.selectforeground = parsecolor(kw.get("selectfg"))
        self.selectbackground = parsecolor(kw.get("selectbg"))
        selectborderwidth = kw.get("selectborderwidth", 0)
        self.selectborderwidth = (
            selectborderwidth
            if _is_real(selectborderwidth) and 0 <= selectborderwidth
            else 0
        )
        self.insertwidth = num0(kw.get("insertwidth"), 2)
        self.insertontime = num0(kw.get("insertontime"), 600)
        self.insertofftime = num0(kw.get("insertofftime"), 300)
        insertborderwidth = kw.get("insertborderwidth", 0)
        self.insertborderwidth = (
            insertborderwidth
            if _is_real(insertborderwidth) and 0 <= insertborderwidth
            else 0
        )
        self.style = Style()
        self.stylename = f"Custom{kw.get("count")}.TEntry"
        self.style_list = [self.stylename]
        self.style.configure(
            self.stylename,
            background=self.bg,
            foreground=self.fg,
            font=self.font,
            selectbackground=self.selectbackground,
            selectborderwidth=self.selectborderwidth,
            selectforeground=self.selectforeground,
            insertwidth=self.insertwidth,
        )
        self._widget = Entry(
            self.master,
            state=self.state,
            takefocus=self.takefocus,
            cursor=self.cursor,
            textvariable=self.textvariable,
            font=self.font,
            width=self.width,
            justify=self.justify,
            show=self.show,
        )

    def inserts(self, text="", place="end"):
        self._widget.insert(place, text)

    def get_text(self):
        return self._widget.get()

    def select_judge(self):
        return self._widget.select_present()

    def select_cansel(self):
        self._widget.select_clear()

    def all_delta(self):
        self._widget.delete(0, "end")

    def delta(self):
        self._widget.destroy()

    def set_text(self, txt):
        self.text = txt
        self.all_delta()
        self.inserts(self.text)
