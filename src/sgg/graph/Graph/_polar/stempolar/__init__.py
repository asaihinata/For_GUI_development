from ...dev import *

__all__ = ["Stempolar"]


class Stempolar(polarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x, self.__y = self._xyd(kw.get("x"), kw.get("y"), kw.get("data"))
        self.linefmt = kw.get("linefmt")
        self.markerfmt = kw.get("markerfmt")
        self.basefmt = kw.get("basefmt")
        self.bottom = nums(kw.get("bottom"), 0)
        self.__plot(
            self.__x,
            self.__y,
            bottom=self.bottom,
            linefmt=self.linefmt,
            markerfmt=self.markerfmt,
            basefmt=self.basefmt,
            alpha=self.alpha,
        )

    def _func(self, stem, alpha=1):
        [i.set_alpha(alpha) for i in stem.get_children()]

    def __plot(self, x, y, bottom, linefmt, markerfmt, basefmt, alpha):
        self.clear()
        self.graphdata = [
            self.ax.stem(
                x.tonp(),
                y.tonp(),
                bottom=bottom,
                linefmt=linefmt,
                markerfmt=markerfmt,
                basefmt=basefmt,
            )
        ]
        np.vectorize(self._func)(self.graphdata[0], alpha)
        self._adjustment()

    def update(self, x=None, y=None, data=None, **kw):
        self._updates(**kw)
        if not isinstance(x, nListlike):
            x = self.__x
        if not isinstance(y, nListlike):
            y = self.__y
        self.__x, self.__y = self._xyd(x, y, data)
        self.linefmt = kw.get("linefmt", self.linefmt)
        self.markerfmt = kw.get("markerfmt", self.markerfmt)
        self.basefmt = kw.get("basefmt", self.basefmt)
        self.bottom = nums(kw.get("bottom"), self.bottom)
        self.__plot(
            self.__x,
            self.__y,
            bottom=self.bottom,
            linefmt=self.linefmt,
            markerfmt=self.markerfmt,
            basefmt=self.basefmt,
            alpha=self.alpha,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
