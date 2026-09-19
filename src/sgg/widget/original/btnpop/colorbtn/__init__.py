from sgg import askcolor

from .._btn import Btn, Button, parsecolor

__all__ = ["Colorbtn"]


class Colorbtn(Btn):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.colors = parsecolor(kw.get("color"), "#ffffff")
        self.__color = (self._to_dec(self.colors), self.colors)
        self.title = kw.get("title", "select color")
        self._textvariable(kw.get("text", "select color"))
        self._widget = Button(
            master,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            textvariable=self.textvariable,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            command=self.__select_color,
            borderwidth=self.borderwidth,
        )

    def __select_color(self):
        self.__color = askcolor(color=self.colors, title=self.title)

    def get_color(self):
        return self.__color

    @property
    def color(self):
        return self.__color

    def _to_dec(self, val):
        val = val.lstrip("#")
        return int(val[0:2], 16), int(val[2:4], 16), int(val[4:6], 16)
