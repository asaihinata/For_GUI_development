from tkinter import Entry, Variable

from sgg.dev import num0, parsecolor
from sgg.widget.element import Element

__all__ = ["Input"]


class Input(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.cursor = self._list_cursor(kw.get("cursor"), "xterm")
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.width = self._dwh_int(kw.get("width"), 20)
        self.textvariable = Variable(value=kw.get("text"))
        self.show = kw.get("show")
        self.state = self.listchose(kw.get("state"), ["normal", "disabled", "readonly"])
        self.disabledbg = parsecolor(kw.get("disabledbg"))
        self.disabledfg = parsecolor(kw.get("disabledfg"))
        self.selectforeground = parsecolor(kw.get("selectfg"))
        self.selectbackground = parsecolor(kw.get("selectbg"))
        selectborderwidth = kw.get("selectborderwidth", 0)
        if self._is_real(selectborderwidth) and 0 <= selectborderwidth:
            self.selectborderwidth = selectborderwidth
        else:
            self.selectborderwidth = 0
        self.insertbackground = parsecolor(kw.get("insertbg"), "#000000")
        self.insertwidth = num0(kw.get("insertwidth"), 2)
        self.insertontime = num0(kw.get("insertontime"), 600)
        self.insertofftime = num0(kw.get("insertofftime"), 300)
        insertborderwidth = kw.get("insertborderwidth", 0)
        if self._is_real(insertborderwidth) and 0 <= insertborderwidth:
            self.insertborderwidth = insertborderwidth
        else:
            self.insertborderwidth = 0
        self._widget = Entry(
            self.master,
            bg=self.bg,
            borderwidth=self.borderwidth,
            cursor=self.cursor,
            disabledbackground=self.disabledbg,
            disabledforeground=self.disabledfg,
            fg=self.fg,
            font=self.font,
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
            show=self.show,
            state=self.state,
            takefocus=self.takefocus,
            textvariable=self.textvariable,
            width=self.width,
        )

    def inserts(self, text="", place="end"):
        self._widget.insert(place, text)

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, txt):
        self.textvariable.set(txt)
        self._widget.config(textvariable=self.textvariable)

    def select_judge(self):
        return self._widget.select_present()

    def select_cansel(self):
        self._widget.select_clear()

    def all_delta(self):
        self._widget.delete(0, "end")

    def delta(self):
        self._widget.destroy()

    # select
    def selection_range(self, start, end):
        if not (self._is_int(start) or start.isdecimal()):
            raise TypeError
        if not (self._is_int(end) or end.isdecimal() or end == "end"):
            raise TypeError
        self._widget.selection_range(start, end)

    def selection_present(self):
        return self._widget.selection_present()

    def selection_clear(self):
        self._widget.selection_clear()

    def focus_set(self):
        self._widget.focus_set()

    def selection_set(self):
        self._widget.focus_set()
