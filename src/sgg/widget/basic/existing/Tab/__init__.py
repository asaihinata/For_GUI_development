from tkinter.ttk import Notebook, Style

from sgg.dev import parsecolor
from sgg.widget.base import Element

__all__ = ["Tab"]


class Tab(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.style = Style()
        self.stylename = f"Custom{kw.get("count")}.TNotebook"
        self.style.theme_use("default")
        self.style.configure(self.stylename, background=self.back_bg)
        self.style.configure(
            f"{self.stylename}.Tab",
            background=self.bg,
            foreground=self.fg,
            font=self.font,
        )
        self.style.map(f"{self.stylename}.Tab", background=[("selected", ("#cccccc"))])
        self.frames = []
        self.widget = Notebook(
            self.master, takefocus=self.takefocus, style=self.stylename
        )
        self.widget.pack(side="left", padx=5, pady=5)

    def _add_tab(self, frame, title):
        self.widget.add(frame, text=title)
        self.frames.append(frame)

    def delta(self):
        self.widget.destroy()

    def set_fg(self, fg):
        self.fg = parsecolor(fg, self.fg)
        self.style.configure(
            f"{self.stylename}.Tab",
            foreground=self.fg,
        )

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.style.configure(self.stylename, background=self.back_bg)
        self.style.configure(f"{self.stylename}.Tab", background=self.bg)
