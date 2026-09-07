from tkinter import Entry

from sgg.dev import _is_real, listchose, num0, parsecolor
from sgg.widget.base import Element

__all__ = ["Input"]


class Input(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.width = num0(kw.get("width"), 20)
        self.text = kw.get("text")
        self.show = kw.get("show")
        self.state = listchose(kw.get("state"), ["normal", "disabled", "readonly"])
        self.disabledbg = parsecolor(kw.get("disabledbg"))
        self.disabledfg = parsecolor(kw.get("disabledfg"))
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
        self.widget = Entry(
            self.master,
            selectforeground=self.selectforeground,
            selectbackground=self.selectbackground,
            selectborderwidth=self.selectborderwidth,
            insertwidth=self.insertwidth,
            insertontime=self.insertontime,
            insertofftime=self.insertofftime,
            insertbackground=self.insertbackground,
            insertborderwidth=self.insertborderwidth,
            disabledforeground=self.disabledfg,
            disabledbackground=self.disabledbg,
            state=self.state,
            takefocus=self.takefocus,
            relief=self.relief,
            cursor=self.cursor,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            justify=self.justify,
            show=self.show,
            borderwidth=self.borderwidth,
        )
        if self.text != None:
            self.inserts(self.text)

    def inserts(self, text="", place="end"):
        self.widget.insert(place, text)

    def get_text(self):
        return self.widget.get()

    def select_judge(self):
        return self.widget.select_present()

    def select_cansel(self):
        self.widget.select_clear()

    def all_delta(self):
        self.widget.delete(0, "end")

    def delta(self):
        self.widget.destroy()

    def set_text(self, txt):
        self.text = txt
        self.all_delta()
        self.inserts(self.text)
