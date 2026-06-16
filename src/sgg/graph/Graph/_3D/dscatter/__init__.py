from itertools import product

from ...dev import *

__all__ = ["DScatter"]


class DScatter(threeElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPArray(kw.get("x"))
        self.__y = NPArray(kw.get("y"))
        self.__z = NPArray(kw.get("z"))
        self.marker = MarkerList(kw.get("marker", "o"))
        self.s = num1s(kw.get("markersize"), 10)
        self.__plot(
            self.__x,
            self.__y,
            self.__z,
            marker=self.marker,
            alpha=self.alpha,
            label=self.label,
        )

    def __plot(self, x, y, z, label, marker, alpha):
        self.clear()
        self.graphdata = [
            self.ax.scatter(xs, ys, zs, label=label[i], marker=marker[i], alpha=alpha)
            for i, (xs, ys, zs) in enumerate(product(x, y, z))
        ]
        self._apply_labels(self.xlabel, self.ylabel, self.zlabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, z=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPArray(x)
        if isinstance(y, nListlike):
            self.__y = NPArray(y)
        if isinstance(z, nListlike):
            self.__z = NPArray(z)
        markers = kw.get("marker", None)
        if markers != None:
            self.marker = MarkerList(markers)
        self.s = num1s(kw.get("markersize"), self.s)
        self.__plot(
            self.__x,
            self.__y,
            self.__z,
            marker=self.marker,
            alpha=self.alpha,
            label=self.label,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()

    def getz(self):
        return self.__z.tonp()

    def getcoordinate(self):
        coords = []
        for i in self.graphdata:
            offsets = np.array(i._offsets3d).T
            if len(coords) == 0:
                coords = offsets
            else:
                coords = np.vstack([coords, offsets])
        return coords
