from ..btn import *

__all__ = ["Colorbtn"]


class Colorbtn(Btn):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__color = (None, None)
        self.colors = parsecolor(kw.get("color"), "#ffffff")
        self.title = kw.get("title", "select color")
        self.text = kw.get("text", "select color")
        self.widget = Button(
            master,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            text=self.text,
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
