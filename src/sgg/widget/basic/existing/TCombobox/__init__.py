from tkinter.ttk import Combobox, Style

from ...common import *

__all__ = ["TCombobox"]


class TCombobox(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.values = kw.get("values", [])
        self.default = kw.get("default")
        self.states = listchose(kw.get("state"), ["normal", "readonly", "disabled"])
        style = Style()
        self.stylename = f"Custom{kw.get('count')}.TCombobox"
        style.configure(
            self.stylename,
            foreground=self.fg,
            background=self.bg,
            fieldbackground=self.bg,
            font=self.font,
        )
        self.widget = Combobox(
            master,
            takefocus=self.takefocus,
            cursor=self.cursor,
            values=self.values,
            state=self.states,
            font=self.font,
            style=self.stylename,
        )
        if self.default:
            self.widget.set(self.default)

    def get_text(self):
        return self.widget.get()

    def set_text(self, text):
        self.widget.set(text)

    def clear(self):
        self.widget.set("")

    def delta(self):
        self.widget.destroy()
