from tkinter import Listbox, StringVar

from ...common import *

__all__ = ["Listboxs"]


class Listboxs(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.values = (
            kw.get("values") if isinstance(kw.get("values"), tuple | list) else []
        )
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.selectforeground = parsecolor(kw.get("selectfg"), "#000000")
        self.selectbackground = parsecolor(kw.get("selectbg"), "#1967d2")
        self.exportselection = bols(kw.get("exportselection"), False)
        self.selectmode = listchose(
            kw.get("selectmode"), ["browse", "single", "multiple", "extended"]
        )
        self.width = self._size_width(kw.get("width"), 20)
        self.height = self._size_height(
            kw.get("height"), min(max(len(self.values), 1), 5)
        )
        self.state = listchose(kw.get("state"), ["normal", "disabled"])
        self.widget = Listbox(
            self.master,
            exportselection=self.exportselection,
            selectforeground=self.selectforeground,
            selectbackground=self.selectbackground,
            relief=self.relief,
            cursor=self.cursor,
            listvariable=StringVar(value=self.values),
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            selectmode=self.selectmode,
            width=self.width,
            height=self.height,
            justify=self.justify,
            state=self.state,
            borderwidth=self.borderwidth,
        )
        self.selectval = nums(kw.get("select"), 0)
        self.select_set(self.selectval)

    def select_set(self, val):
        if isinstance(val, int):
            if val < 0:
                val = 0
            elif len(self.values) < val:
                val = len(self.values) - 1
            self.widget.selection_set(val)

    def apend(self, lists=[], place="end"):
        if isinstance(lists, list | tuple):
            for i in lists:
                self.widget.insert(place, i)

    def clear(self):
        self.widget.delete(0, "end")

    def dele(self, *index):
        if isinstance(index, tuple):
            for i in index:
                if isinstance(i, int) and not (i < 0 or self.lens() < i):
                    self.widget.delete(i)

    def lens(self):
        return self.widget.size()

    def select(self):
        return self.widget.curselection()

    def select_val(self):
        val = list(self.widget.curselection())
        if len(val) == 1:
            return self.values[val[0]]
        elif len(val) == 0:
            return None
        else:
            return [self.values[i] for i in val]

    def set(self, lists):
        if isinstance(lists, list | tuple):
            self.clear()
            self.apend(lists, "end")

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
