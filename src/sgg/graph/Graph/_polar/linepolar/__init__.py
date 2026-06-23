from ...dev import *

__all__ = ["Linepolar"]


class Linepolar(polarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x, self.__y = self._xyd(kw.get("x"), kw.get("y"), kw.get("data"))
        self.markersize = num0(kw.get("markersize"), 10)
        self.marker = Marker(kw.get("marker", ""))
        self.line = Solid(kw.get("linestyle", "-"))
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            linewidth=self.linewidth,
            linestyle=self.line,
            markersize=self.markersize,
            alpha=self.alpha,
        )

    def __plot(self, x, y, marker, linewidth, linestyle, markersize, alpha):
        self.clear()
        self.graphdata = [
            self.ax.plot(
                x,
                y,
                marker=marker.marker,
                linewidth=linewidth,
                markersize=markersize,
                linestyle=linestyle.solid,
                alpha=alpha,
            )
        ]
        self._adjustment()

    def update(self, x=None, y=None, data=None, **kw):
        self._updates(**kw)
        if not change_array_like(x):
            x = self.__x
        if not change_array_like(y):
            y = self.__y
        self.__x, self.__y = self._xyd(x, y, data)
        self.markersize = num0(kw.get("markersize"), 10)
        self.marker = Marker(kw.get("marker", self.marker))
        self.line = Solid(kw.get("linestyle", self.line))
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            linewidth=self.linewidth,
            linestyle=self.line,
            markersize=self.markersize,
            alpha=self.alpha,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
