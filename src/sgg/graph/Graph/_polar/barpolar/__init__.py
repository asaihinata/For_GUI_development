from ...dev import *

__all__ = ["Barpolar"]


class Barpolar(polarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x, self.__y = self._xyd(kw.get("x"), kw.get("y"), kw.get("data"))
        self.width = range_num(num0s(kw.get("width"), 1), 0, 1, 1)
        self.align = listchose(kw.get("align"), ["center", "edge"])
        self.__plot(
            self.__x.tonp(),
            self.__y.tonp(),
            alpha=self.alpha,
            width=self.width,
            align=self.align,
            color=self.color,
        )

    def __plot(self, x, y, alpha, width, align, color):
        self.clear()
        self.graphdata = [
            self.ax.bar(
                x, y, bottom=0, color=color, alpha=alpha, width=width, align=align
            )
        ]
        self._adjustment()

    def update(self, x=None, y=None, data=None, **kw):
        self._updates(**kw)
        if not isinstance(x, nListlike):
            x = self.__x
        if not isinstance(y, nListlike):
            y = self.__y
        if not isinstance(data, nListlike):
            data = None
        self.__x, self.__y = self._xyd(x, y, data)
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.align = listchose(kw.get("align"), ["center", "edge"], self.align)
        self.__plot(
            self.__x.tonp(),
            self.__y.tonp(),
            alpha=self.alpha,
            width=self.width,
            align=self.align,
            color=self.color,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
