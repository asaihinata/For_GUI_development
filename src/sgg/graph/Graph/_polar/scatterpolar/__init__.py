from ...dev import *

__all__ = ["Scatterpolar"]


class Scatterpolar(polarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x, self.__y = self._xyd(kw.get("x"), kw.get("y"), kw.get("data"))
        self.marker = Marker(kw.get("marker", "o"))
        self.s = num1s(kw.get("markersize"), 10)
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            linewidth=self.linewidth,
            alpha=self.alpha,
            s=self.s,
        )

    def __plot(self, x, y, marker, linewidth, alpha, s):
        self.clear()
        self.graphdata = [
            self.ax.scatter(
                x, y, marker=marker.marker, s=s, alpha=alpha, linewidth=linewidth
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
        self.marker = Marker(kw.get("marker", self.marker))
        self.s = num1s(kw.get("markersize"), self.s)
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            linewidth=self.linewidth,
            alpha=self.alpha,
            s=self.s,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()

    def getcoordinate(self):
        coords = []
        for i in self.graphdata:
            offsets = np.array(i.get_offsets())
            if len(coords) == 0:
                coords = offsets
            else:
                coords = np.vstack([coords, offsets])
        return coords
