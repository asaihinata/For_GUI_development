from tkinter import DoubleVar, IntVar
from tkinter.ttk import Progressbar, Style

from sgg.dev import _is_real, listchose, parsecolor
from sgg.widget.base import Element

__all__ = ["TProgressbar"]


class TProgressbar(Element):
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
        self.style_name = (
            f"Custom{kw.get("count")}.Horizontal.TProgressbar"
            if self.orient == "horizontal"
            else f"Custom{kw.get("count")}.Vertical.TProgressbar"
        )
        self.style.theme_use("default")
        self.style.layout(
            self.style_name,
            self.style.layout(
                "Horizontal.TProgressbar"
                if self.orient == "horizontal"
                else "Vertical.TProgressbar"
            ),
        )
        self.style.configure(
            self.style_name, background=self.fg, troughcolor=self.bg, thickness=20
        )
        self.widget = Progressbar(
            master,
            variable=self.variable,
            takefocus=self.takefocus,
            cursor=self.cursor,
            orient=self.orient,
            length=self.length,
            mode=self.mode,
            style=self.style_name,
            maximum=self.maximum,
        )

    def get(self):
        return self.widget["value"]

    def set(self, value):
        if not _is_real(value):
            raise TypeError
        self.value = value
        self._variable(value)
        self.widget.config(variable=self.variable)

    def start(self, interval=None):
        if interval is not None and not _is_real(interval):
            raise TypeError
        self.widget.start(interval)

    def step(self, amount=None):
        if amount is not None and not _is_real(amount):
            raise TypeError
        self.widget.step(amount)

    def stop(self):
        self.widget.stop()

    def delta(self):
        self.widget.destroy()

    def set_fg(self, fg):
        self.fg = parsecolor(fg, self.fg)
        self.style.configure(self.style_name, background=self.fg, thickness=20)

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.style.configure(self.style_name, troughcolor=self.bg, thickness=20)

    def _variable(self, value):
        if isinstance(value, int):
            self.variable = IntVar(self.master, int(value))
        else:
            self.variable = DoubleVar(self.master, float(value))
