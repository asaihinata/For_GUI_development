from tkinter.ttk import Notebook, Style

from sgg.dev import parsecolor
from sgg.widget.base import TElement

__all__ = ["Tab"]


class Tab(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.style = Style()
        self.stylename = f"Custom{kw.get("count")}.TNotebook"
        self.styletabname = f"{self.stylename}.Tab"
        self.style_list = [self.stylename, self.styletabname]
        self.style.theme_use("default")
        self.style.configure(self.stylename, background=self.back_bg)
        self.style.configure(
            self.styletabname,
            background=self.bg,
            foreground=self.fg,
            font=self.font,
        )
        self.style.map(self.styletabname, background=[("selected", ("#cccccc"))])
        self.frames = []
        self._widget = Notebook(
            self.master, takefocus=self.takefocus, style=self.stylename
        )
        self._widget.pack(side="left", padx=5, pady=5)

    def _add_tab(self, frame, title):
        self._widget.add(frame, text=title)
        self.frames.append(frame)

    def delta(self):
        self._widget.destroy()

    def set_fg(self, fg):
        self.fg = parsecolor(fg, self.fg)
        self.style.configure(
            self.styletabname,
            foreground=self.fg,
        )

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.style.configure(self.stylename, background=self.back_bg)
        self.style.configure(self.styletabname, background=self.bg)
