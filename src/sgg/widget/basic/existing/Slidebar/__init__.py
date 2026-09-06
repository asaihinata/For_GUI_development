from tkinter import DoubleVar, IntVar, Scale

from sgg.dev import bols, listchose, num0s, nums
from sgg.widget.base import Element

__all__ = ["Slidebar"]


class Slidebar(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        minval = kw.get("min", 0)
        maxval = kw.get("max", 100)
        if not isinstance(minval, int | float):
            minval = 0
        if not isinstance(maxval, int | float):
            minval = 100
        if maxval < minval:
            self.maxval = minval
            self.minval = maxval
        else:
            self.maxval = maxval
            self.minval = minval
        value = kw.get("value", 0)
        if not isinstance(value, int | float):
            value = 0
        if value < self.minval:
            value = self.minval
        elif self.maxval < value:
            value = self.maxval
        if isinstance(value, int):
            self.value = IntVar(self.master, value)
        else:
            self.value = DoubleVar(self.master, value)
        sliderlength = kw.get("sliderlength", 30)
        if isinstance(sliderlength, int | float) and 0 <= sliderlength:
            self.sliderlength = sliderlength
        else:
            self.sliderlength = 30
        label = kw.get("label", None)
        if label is not None and not isinstance(label, str):
            raise TypeError
        self.label = label
        self.orientation = listchose(kw.get("orientation"), ["horizontal", "vertical"])
        self.resolution = num0s(kw.get("resolution"), 1)
        self.showvalue = bols(kw.get("showvalue"), True)
        self.digits = kw.get("digits", 0)
        if not isinstance(self.digits, int):
            self.digits = 0
        self.length = num0s(kw.get("length"), 200)
        self.borderwidth = num0s(kw.get("borderwidth"), 1)
        self.widget = Scale(
            self.master,
            takefocus=self.takefocus,
            variable=self.value,
            label=self.label,
            sliderlength=self.sliderlength,
            relief=self.relief,
            cursor=self.cursor,
            fg=self.fg,
            bg=self.bg,
            font=self.font,
            from_=self.minval,
            to=self.maxval,
            orient=self.orientation,
            showvalue=self.showvalue,
            resolution=self.resolution,
            digits=self.digits,
            length=self.length,
            borderwidth=self.borderwidth,
        )

    def set(self, val):
        if nums(val):
            self.widget.set(val)

    def _get(self):
        return self.widget.get()

    def delta(self):
        self.widget.destroy()
