from tkinter import DoubleVar
from tkinter.ttk import Scale, Style

from sgg.dev import listchose, num0s
from sgg.widget.base import TElement

__all__ = ["TSlidebar"]


class TSlidebar(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        minval = kw.get("min", 0)
        maxval = kw.get("max", 1)
        if not self._is_real(minval):
            minval = 0
        if not self._is_real(maxval):
            maxval = 1
        if maxval <= minval:
            self.maxval, self.minval = minval, maxval
        else:
            self.maxval, self.minval = maxval, minval
        self._value(kw.get("value", 0))
        sliderlength = kw.get("sliderlength", 30)
        if isinstance(sliderlength, int | float) and 0 <= sliderlength:
            self.sliderlength = sliderlength
        else:
            self.sliderlength = 30
        self.orientation = listchose(kw.get("orientation"), ["horizontal", "vertical"])
        self.length = num0s(kw.get("length"), 200)
        self.style = Style()
        if self.orientation == "horizontal":
            self.stylename = f"Custom{kw.get("count")}.Horizontal.TScale"
        else:
            self.stylename = f"Custom{kw.get("count")}.Vertical.TScale"
        self.style_list = [self.stylename]
        self.style.configure(
            self.stylename,
            foreground=self.fg,
            background=self.bg,
            fieldbackground=self.bg,
            font=self.font,
            sliderlength=self.sliderlength,
        )
        self._widget = Scale(
            self.master,
            style=self.stylename,
            takefocus=self.takefocus,
            variable=self.variable,
            cursor=self.cursor,
            from_=self.minval,
            to=self.maxval,
            orient=self.orientation,
            length=self.length,
        )

    def set(self, val):
        if self._is_real(val):
            self._value(val)
            self._widget.config(variable=self.variable)

    def get(self):
        return self.variable.get()

    def delta(self):
        self._widget.destroy()

    def _value(self, val):
        if not self._is_real(val):
            val = 0
        if val < self.minval:
            val = self.minval
        if self.maxval < val:
            val = self.maxval
        self.variable = DoubleVar(value=float(val))
