from tkinter.ttk import Combobox, Style

from sgg.dev import listchose
from sgg.widget.base import TElement

__all__ = ["TCombobox"]


class TCombobox(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.values = self._to_flat_list(kw.get("values"))
        self.text = kw.get("text")
        self.states = listchose(kw.get("state"), ["normal", "readonly", "disabled"])
        self.style = Style()
        self.stylename = f"Custom{kw.get("count")}.TCombobox"
        self.style_list = [self.stylename]
        self.style.configure(
            self.stylename,
            foreground=self.fg,
            background=self.bg,
            fieldbackground=self.bg,
            font=self.font,
        )
        self._widget = Combobox(
            master,
            takefocus=self.takefocus,
            cursor=self.cursor,
            values=self.values,
            state=self.states,
            font=self.font,
            style=self.stylename,
        )
        if self.text:
            self._widget.set(self.text)

    def get_text(self):
        return self._widget.get()

    def set_text(self, text):
        self._widget.set(text)

    def clear(self):
        self._widget.set("")

    def delta(self):
        self._widget.destroy()
