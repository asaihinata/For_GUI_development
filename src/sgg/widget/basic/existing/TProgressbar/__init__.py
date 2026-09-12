from tkinter import DoubleVar, IntVar
from tkinter.ttk import Progressbar, Style

from sgg.dev import _is_real, listchose, parsecolor
from sgg.widget.base import TElement

__all__ = ["TProgressbar"]


class TProgressbar(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        value = kw.get("value", 0)
        if _is_real(value):
            self.value = value
        else:
            raise TypeError
        self._variable(self.value)
        maximum = kw.get("max")
        if _is_real(maximum):
            self.maximum = maximum
        else:
            self.maximum = 200
        length = kw.get("length")
        if _is_real(length):
            self.length = length
        else:
            self.length = 200
        self.mode = listchose(kw.get("mode"), ["determinate", "indeterminate"])
        self.orient = listchose(kw.get("orient"), ["horizontal", "vertical"])
        self.style = Style()
        if self.orient == "horizontal":
            self.stylename = f"Custom{kw.get("count")}.Horizontal.TProgressbar"
        else:
            self.stylename = f"Custom{kw.get("count")}.Vertical.TProgressbar"
        self.style_list = [self.stylename]
        self.style.theme_use("default")
        self.style.layout(
            self.stylename,
            self.style.layout(
                "Horizontal.TProgressbar"
                if self.orient == "horizontal"
                else "Vertical.TProgressbar"
            ),
        )
        self.style.configure(
            self.stylename, background=self.fg, troughcolor=self.bg, thickness=20
        )
        self._widget = Progressbar(
            master,
            variable=self.variable,
            takefocus=self.takefocus,
            cursor=self.cursor,
            orient=self.orient,
            length=self.length,
            mode=self.mode,
            style=self.stylename,
            maximum=self.maximum,
        )

    def get(self):
        return self._widget["value"]

    def set(self, value):
        if not _is_real(value):
            raise TypeError
        self.value = value
        self._variable(value)
        self._widget.config(variable=self.variable)

    def start(self, interval=None):
        if interval is not None and not _is_real(interval):
            raise TypeError
        self._widget.start(interval)

    def step(self, amount=None):
        if amount is not None and not _is_real(amount):
            raise TypeError
        self._widget.step(amount)

    def stop(self):
        self._widget.stop()

    def delta(self):
        self._widget.destroy()

    def set_fg(self, fg):
        self.fg = parsecolor(fg, self.fg)
        self.style.configure(self.stylename, background=self.fg, thickness=20)

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.style.configure(self.stylename, troughcolor=self.bg, thickness=20)

    def _variable(self, value):
        if isinstance(value, int):
            self.variable = IntVar(self.master, int(value))
        else:
            self.variable = DoubleVar(self.master, float(value))
