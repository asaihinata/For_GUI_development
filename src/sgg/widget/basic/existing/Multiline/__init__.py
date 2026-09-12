from tkinter import INSERT, Text

import numpy as np
import numpy.strings as nps

from sgg.dev import _flatten, _is_real, bols, listchose, num0, parsecolor
from sgg.widget.base import Element

__all__ = ["Multiline"]


class Multiline(Element):
    __Marksetlist = np.array([], np.str_)

    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.width = self._dwh(kw.get("width"), 20)
        self.height = self._dwh(kw.get("height"), 5)
        txt = kw.get("text")
        self.cursorshow = bols(kw.get("cursorshow"), True)
        self.borderwidth = num0(kw.get("borderwidth"), 1)
        self.state = listchose(kw.get("state"), ["normal", "disabled"])
        self.wrap = listchose(kw.get("wrap"), ["none", "word", "char"])
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
        self._widget = Text(
            self.master,
            takefocus=self.takefocus,
            selectforeground=self.selectforeground,
            selectbackground=self.selectbackground,
            selectborderwidth=self.selectborderwidth,
            insertwidth=self.insertwidth,
            insertontime=self.insertontime,
            insertofftime=self.insertofftime,
            insertbackground=self.insertbackground,
            insertborderwidth=self.insertborderwidth,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            cursor=self.cursor,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            state=self.state,
            wrap=self.wrap,
            borderwidth=self.borderwidth,
        )
        if self.cursorshow:
            self._widget.focus_set()
        self.__insert_txt(self._to_flat_list(txt))

    def __insert_txt(self, txt):
        if isinstance(txt, str):
            self.inserts(txt, place="end")
        elif isinstance(txt, list | tuple | range):
            arr, self.__count = _flatten(txt), 0

            def _func(txt, lens):
                if lens == self.__count:
                    self.inserts(f"{txt}", place="end")
                else:
                    self.inserts(f"{txt}\n", place="end")
                self.__count += 1

            np.vectorize(_func, otypes=[None])(arr, len(arr) - 1)
        elif isinstance(txt, np.ndarray):
            return self.__insert_txt(txt.tolist())

    def inserts(self, txt, place="end"):
        self._widget.insert(place, txt)

    def get_txt(self):
        return self._widget.get(1.0, "end-1c")

    def all_delta(self):
        self._widget.delete(1.0, "end")

    @property
    def mark_list(self):
        return self.__Marksetlist.tolist()

    def mark_set(self, index, name=INSERT):
        if not isinstance(name, str) or not isinstance(index, str):
            raise TypeError
        self.__Marksetlist = np.append(self.__Marksetlist, name)
        self._widget.mark_set(name, index)

    def index(self, name):
        if not isinstance(name, str) or nps.find(self.__Marksetlist, name) == -1:
            return None
        return self._widget.index(name)

    def focus_set(self):
        self._widget.focus_set()

    def delta(self):
        self._widget.destroy()
