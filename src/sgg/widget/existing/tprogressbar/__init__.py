from tkinter import DoubleVar, IntVar
from tkinter.ttk import Progressbar, Style

from sgg.dev import bols, listchose, parsecolor
from sgg.widget.element import TElement

__all__ = ["TProgressbar"]


class TProgressbar(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        value = kw.get("value", 0)
        if self._is_real(value):
            self._variable(value)
        else:
            raise TypeError
        maximum = kw.get("max", 100)
        if self._is_real(maximum):
            self.maximum = maximum
        else:
            self.maximum = 100
        self.length = self._unit_change(kw.get("length", 100))
        self.mode = listchose(kw.get("mode"), ["determinate", "indeterminate"])
        self.orient = listchose(kw.get("orient"), ["horizontal", "vertical"])
        self.autostart = bols(kw.get("autostart", False), False)
        interval = kw.get("interval")
        if interval is None or self._is_real(interval):
            self.interval = interval
        else:
            self.interval = None
        self.style = Style()
        if self.orient == "horizontal":
            self.stylename = f"Custom{kw.get("count")}.Horizontal.TProgressbar"
        else:
            self.stylename = f"Custom{kw.get("count")}.Vertical.TProgressbar"
        self.style_list = [self.stylename]
        self.style.theme_use("default")
        if self.orient == "horizontal":
            self.style.layout(
                self.stylename,
                self.style.layout("Horizontal.TProgressbar"),
            )
        else:
            self.style.layout(
                self.stylename,
                self.style.layout("Vertical.TProgressbar"),
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
        if self.autostart:
            self.start(self.interval)

    def get(self):
        return self.variable.get()

    def set(self, value):
        if not self._is_real(value):
            raise TypeError
        self._variable(value)
        self._widget.config(variable=self.variable)

    def start(self, interval=None):
        if interval is not None and not self._is_real(interval):
            interval = self.interval
        self._widget.start(interval)

    def step(self, amount=None):
        if amount is not None and not self._is_real(amount):
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
            self.variable = IntVar(value=int(value))
        else:
            self.variable = DoubleVar(value=float(value))
