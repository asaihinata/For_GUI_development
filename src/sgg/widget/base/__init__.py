from re import findall
from types import FunctionType

from ...dev import bols, listchose, num0s, parsecolor
from ...font import TKFont
from ...readfile import Getfont

__all__ = ["Element"]


class Element:
    def __init__(self, master, kw):
        self.widget = None
        self.master = master
        self.graph = False
        self.cursor = kw.get("cursor")
        self.back_bg = kw.get("back_bg")
        self.justify = listchose(kw.get("justify"), ["left", "right", "center"])
        self.padx = num0s(kw.get("padx"), 1)
        self.pady = num0s(kw.get("pady"), 1)
        self.relief = listchose(
            kw.get("relief"), ["flat", "raised", "sunken", "ridge", "solid", "groove"]
        )
        self.fg = parsecolor(kw.get("fg"), "#000000")
        self.bg = parsecolor(
            kw.get("bg"), "#64778d" if self.back_bg == None else self.back_bg
        )
        self.borderwidth = num0s(kw.get("borderwidth"))
        self.takefocus = bols(kw.get("takefocus"))
        font = kw.get("font", None)
        self.family = kw.get("family")
        self.font_size = kw.get("font_size")
        self.weight = kw.get("weight")
        self.slant = kw.get("slant")
        self.underline = kw.get("underline")
        self.overstrike = kw.get("overstrike")
        if isinstance(font, Getfont):
            self.font = TKFont(
                font=font,
                root=self.master,
            )
        else:
            self.font = TKFont(
                self.family,
                self.font_size,
                self.weight,
                self.slant,
                self.underline,
                self.overstrike,
                root=self.master,
            )
        self.anchor = listchose(
            kw.get("anchor"), ["w", "n", "s", "e", "nw", "ne", "se", "sw", "center"]
        )
        self.width = self._dwh(kw.get("width"))
        self.height = self._dwh(kw.get("height"))

    def _dwh(self, val, other=None):
        if isinstance(val, int | float) and 0 < val:
            return val
        return other

    def _exec_funcs(self, funcs=None):
        if isinstance(funcs, FunctionType):
            try:
                funcs()
            except NameError as e:
                raise NameError(f"{e}という関数は見つかりません")
        elif isinstance(funcs, list | tuple):
            for f in funcs:
                if isinstance(f, FunctionType):
                    try:
                        f()
                    except NameError as e:
                        raise NameError(f"{e}という関数は見つかりません")
                else:
                    raise NameError(f"{f}という関数は見つかりません")
        else:
            return None

    def winsize(self):
        root = self.master
        return root.winfo_width(), root.winfo_height()

    def winwidth(self):
        return self.master.winfo_width()

    def winheight(self):
        return self.master.winfo_height()

    def winxy(self):
        root = self.master
        return root.winfo_x(), root.winfo_y()

    def winx(self):
        return self.master.winfo_x()

    def winy(self):
        return self.master.winfo_y()

    def geometry(self):
        return [float(i) for i in findall(r"\d+", self.master.winfo_geometry())]

    def rootxy(self):
        root = self.master
        return root.winfo_rootx(), root.winfo_rooty()

    def rootx(self):
        return self.master.winfo_rootx()

    def rooty(self):
        return self.master.winfo_rooty()

    def visual(self):
        return self.master.winfo_visual()

    def screen(self):
        return self.master.winfo_screen()

    def reqsize(self):
        root = self.master
        return root.winfo_reqwidth(), root.winfo_reqheight()

    def reqwidth(self):
        return self.master.winfo_reqwidth()

    def reqheight(self):
        return self.master.winfo_reqheight()

    def id(self):
        return self.master.winfo_id()

    def name(self):
        return self.master.winfo_name()
