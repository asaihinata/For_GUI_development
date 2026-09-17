from tkinter import DoubleVar, IntVar, Scale

from sgg.widget.base import Element

__all__ = ["Slidebar"]


class Slidebar(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        value = kw.get("value", 0)
        minval = kw.get("min", 0)
        maxval = kw.get("max", 100)
        if not self._is_real(value):
            value = 0
        if self._is_int(value):
            self.variable = IntVar(value=value)
        else:
            self.variable = DoubleVar(value=value)
        self.minval = minval if self._is_real(minval) else 0
        self.maxval = maxval if self._is_real(maxval) else 100
        sliderlength = kw.get("sliderlength", 30)
        self.sliderlength = (
            sliderlength if self._is_real(sliderlength) and 0 <= sliderlength else 30
        )
        label = kw.get("label", None)
        if label is None or isinstance(label, str):
            self.label = label
        else:
            raise TypeError
        self.orientation = self.listchose(
            kw.get("orientation"), ["vertical", "horizontal"]
        )
        self.resolution = self._up0s(kw.get("step"), 1)
        bigincrement = kw.get("bigincrement")
        self.bigincrement = bigincrement if self._is_real(bigincrement) else 0
        self.showvalue = self._bols(kw.get("showvalue"))
        self.digits = kw.get("digits", 0)
        if not self._is_int(self.digits):
            self.digits = 0
        self.length = self._up0s(kw.get("length"), 100)
        self.borderwidth = self._up0s(kw.get("borderwidth"), 1)
        self._widget = Scale(
            self.master,
            bg=self.bg,
            bigincrement=self.bigincrement,
            borderwidth=self.borderwidth,
            cursor=self.cursor,
            digits=self.digits,
            fg=self.fg,
            font=self.font,
            from_=self.minval,
            label=self.label,
            length=self.length,
            orient=self.orientation,
            relief=self.relief,
            resolution=self.resolution,
            showvalue=self.showvalue,
            sliderlength=self.sliderlength,
            takefocus=self.takefocus,
            to=self.maxval,
            variable=self.variable,
        )

    def set(self, val):
        if self._is_int(val):
            self.variable = IntVar(value=val)
        elif self._is_float(val):
            self.variable = DoubleVar(value=val)

    def get(self):
        return self.variable.get()

    def delta(self):
        self._widget.destroy()

    def __int__(self):
        return int(self.variable.get())

    def __float__(self):
        return float(self.variable.get())
