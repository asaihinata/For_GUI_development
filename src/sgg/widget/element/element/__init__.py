from re import findall, search
from types import FunctionType

import numpy as np

from sgg._list import ANCHOR_LIST, CURSOR_LIST, RELIEF_LIST
from sgg.dev import _SET_OBJ, num0s, parsecolor
from sgg.font import Getfont, TKFont

__all__ = ["Element"]


class Element(_SET_OBJ):
    def __init__(self, master, kw):
        self._widget = None
        self.master = master
        self.cursor = self._list_cursor(kw.get("cursor"), "")
        self.back_bg = kw.get("back_bg")
        self.justify = self.listchose(kw.get("justify"), ["left", "right", "center"])
        self.padx = num0s(kw.get("padx"), 1)
        self.pady = num0s(kw.get("pady"), 1)
        self.relief = self.listchose(kw.get("relief"), RELIEF_LIST, "flat")
        self.fg = parsecolor(kw.get("fg"), "#000000")
        self.bg = parsecolor(
            kw.get("bg"), "#64778d" if self.back_bg == None else self.back_bg
        )
        self.borderwidth = num0s(kw.get("borderwidth"))
        self.takefocus = self._bols(kw.get("takefocus"))
        font = kw.get("font", None)
        self.family = kw.get("family")
        self.font_size = kw.get("font_size")
        self.weight = kw.get("weight")
        self.slant = kw.get("slant")
        self.underline = kw.get("underline")
        self.overstrike = kw.get("overstrike")
        if isinstance(font, Getfont):
            self.font = TKFont(
                self.master,
                font=font,
            )
        else:
            self.font = TKFont(
                self.master,
                self.family,
                self.font_size,
                self.weight,
                self.slant,
                self.underline,
                self.overstrike,
            )
        self.anchor = self.listchose(kw.get("anchor"), ANCHOR_LIST)
        self.width = self._dwh(kw.get("width"))
        self.height = self._dwh(kw.get("height"))

    def __str__(self):
        return str(self._widget)

    def __repr__(self):
        return repr(self._widget)

    def __static_attributes__(self):
        return type(self).__static_attributes__

    def __firstlineno__(self):
        return type(self).__firstlineno__

    def _list_cursor(self, name, other=None):
        if name in CURSOR_LIST:
            return name
        return other

    def _dwh(self, val, other=None):
        if isinstance(val, int | float) and 0 < val:
            return val
        return other

    def _dwh_int(self, val, other=None):
        if self._is_int(val) and 0 < val:
            return val
        return other

    def _exec_funcs(self, funcs=None):
        if isinstance(funcs, FunctionType):
            funcs()
        elif isinstance(funcs, list | tuple):
            funcs = self._flatten(funcs)
            for f in funcs:
                if isinstance(f, FunctionType):
                    f()
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

    def set_fg(self, fg):
        if hasattr(self, "fg"):
            self.fg = parsecolor(fg, self.fg)
            self._widget.config(fg=self.fg)
        else:
            raise ValueError

    def set_bg(self, bg):
        if hasattr(self, "bg"):
            self.bg = parsecolor(bg, self.bg)
            self._widget.config(bg=self.bg)
        else:
            raise ValueError

    def get_fg(self):
        if hasattr(self, "fg"):
            return self.fg
        else:
            raise ValueError

    def get_bg(self):
        if hasattr(self, "bg"):
            return self.bg
        else:
            raise ValueError

    def focus_set(self):
        if hasattr(self._widget, "focus_set"):
            self._widget.focus_set()

    def focus_displayof(self):
        if hasattr(self._widget, "focus_displayof"):
            self._widget.focus_displayof()

    def focus_get(self):
        if hasattr(self._widget, "focus_get"):
            return self._widget.focus_get()

    def keys(self):
        return self._widget.keys()

    def cget(self, key):
        widget = self._widget
        if key in widget.keys():
            return widget.cget(key)
        else:
            raise ValueError

    __getitem__ = cget

    def info(self, keys=None):
        infodict = self._widget.info()
        return infodict.get(keys, infodict)

    def _unit_point(self, val):
        if self._is_real(val):
            return val
        elif isinstance(val, np.str_):
            return self._unit_point(str(val))
        elif isinstance(val, str):
            if val[len(val) - 1] in ["c", "m", "i", "p"]:
                return val
            else:
                try:
                    float(val)
                except:
                    raise ValueError
                else:
                    return val
        raise ValueError

    def _numpointnum(self, strs):
        try:
            strs = search(r"\d+\.\d+", strs).group()
        except AttributeError as e:
            raise AttributeError(e)
        return strs

    # property
    @property
    def widget(self):
        return self._widget

    @property
    def graph(self):
        return False

    @property
    def __name__(self):
        return type(self).__name__

    @property
    def __bases__(self):
        return type(self).__bases__

    @property
    def __base__(self):
        return type(self).__base__

    @property
    def __mro__(self):
        return list(type(self).__mro__)

    @property
    def __module__(self):
        return type(self).__module__

    @property
    def __dictoffset__(self):
        return type(self).__dictoffset__

    @property
    def __flags__(self):
        return type(self).__flags__

    @property
    def __itemsize__(self):
        return type(self).__itemsize__
