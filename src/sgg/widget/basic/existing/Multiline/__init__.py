from itertools import chain
from tkinter import INSERT, Text

import numpy as np
import numpy.strings as nps

from sgg.dev import bols, listchose, num0, parsecolor
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
        self.insertbackground = parsecolor(kw.get("insertbg"), "#000000")
        self.insertwidth = num0(kw.get("insertwidth"), 2)
        self.widget = Text(
            self.master,
            takefocus=self.takefocus,
            insertbackground=self.insertbackground,
            insertwidth=self.insertwidth,
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
            self.widget.focus_set()
        if isinstance(txt, str | list | tuple | range) or (
            isinstance(txt, np.ndarray) and txt.dtype.kind == "U"
        ):
            self.__insert_txt(txt)
        elif isinstance(txt, np.str_):
            self.__insert_txt(str(txt))
        else:
            raise TypeError

    def __insert_txt(self, txt):
        if isinstance(txt, str):
            self.inserts(txt, place="end")
        elif isinstance(txt, list | tuple | range):
            arr, self.__count = list(chain.from_iterable([txt])), 0

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
        self.widget.insert(place, txt)

    def get_txt(self):
        return self.widget.get(1.0, "end-1c")

    def all_delta(self):
        self.widget.delete(1.0, "end")

    @property
    def mark_list(self):
        return self.__Marksetlist.tolist()

    def mark_set(self, index, name=INSERT):
        if not isinstance(name, str) or not isinstance(index, str):
            raise TypeError
        self.__Marksetlist = np.append(self.__Marksetlist, name)
        self.widget.mark_set(name, index)

    def index(self, name):
        if not isinstance(name, str) or nps.find(self.__Marksetlist, name) == -1:
            return None
        return self.widget.index(name)

    def focus_set(self):
        self.widget.focus_set()

    def delta(self):
        self.widget.destroy()
