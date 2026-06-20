from tkinter.ttk import Progressbar, Style

from ...common import *

__all__ = ["TProgressbar"]


class TProgressbar(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.value = num0(kw.get("value"))
        self.maximum = num0(kw.get("max"), 100)
        self.length = num0(kw.get("length"), 200)
        self.mode = listchose(kw.get("mode"), ["determinate", "indeterminate"])
        self.orient = listchose(kw.get("orient"), ["horizontal", "vertical"])
        style = Style()
        self.style_name = (
            f"Custom{kw.get('count')}.Horizontal.TProgressbar"
            if self.orient == "horizontal"
            else f"Custom{kw.get('count')}.Vertical.TProgressbar"
        )
        style.theme_use("default")
        style.layout(
            self.style_name,
            style.layout(
                "Horizontal.TProgressbar"
                if self.orient == "horizontal"
                else "Vertical.TProgressbar"
            ),
        )
        style.configure(
            self.style_name, background=self.fg, troughcolor=self.bg, thickness=20
        )
        self.widget = Progressbar(
            master,
            takefocus=self.takefocus,
            cursor=self.cursor,
            orient=self.orient,
            length=self.length,
            mode=self.mode,
            style=self.style_name,
            maximum=self.maximum,
        )
        self._set(self.value)

    def _set(self, val):
        try:
            self.widget["value"] = val
        except:
            self.widget["value"] = 0

    def get(self):
        return self.widget["value"]

    def start(self):
        self.widget.start()

    def stop(self):
        self.widget.stop()

    def delta(self):
        self.widget.destroy()
