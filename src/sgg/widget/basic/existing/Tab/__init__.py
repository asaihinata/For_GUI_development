from tkinter.ttk import Notebook, Style

from ...common import *

__all__ = ["Tab"]


class Tab(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        style = Style()
        self.stylename = f"Custom{kw.get('count')}.TNotebook"
        style.theme_use("default")
        style.configure(self.stylename, background=self.back_bg)
        style.configure(
            f"{self.stylename}.Tab",
            background=self.bg,
            foreground=self.fg,
            font=self.font,
        )
        style.map(f"{self.stylename}.Tab", background=[("selected", ("#cccccc"))])
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
