from tkinter import Variable
from tkinter.ttk import Combobox, Style

from sgg.dev import listchose
from sgg.widget.element import TElement

__all__ = ["TCombobox"]


class TCombobox(TElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self._set_font(kw)
        self.height = self._dwh_int(kw.get("height"), 10)
        self.width = self._dwh_int(kw.get("width"), 20)
        self.values = self._to_flat_list(kw.get("values"))
        self.textvariable = Variable(value=kw.get("text"))
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
            height=self.height,
            takefocus=self.takefocus,
            cursor=self.cursor,
            values=self.values,
            state=self.states,
            font=self.font,
            style=self.stylename,
            textvariable=self.textvariable,
        )

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, text):
        self.textvariable.set(text)
        self._widget.config(textvariable=self.textvariable)

    def clear(self):
        self._widget.set("")

    def delta(self):
        self._widget.destroy()
