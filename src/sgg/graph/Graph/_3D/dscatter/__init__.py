from sgg.graph.graph.dev import *

__all__ = ["DScatter"]


class DScatter(threeElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"))
        self.__y = NPNumber(kw.get("y"))
        self.__z = NPNumber(kw.get("z"))
        self.marker = MarkerList(kw.get("marker", "o"))
        self.s = num1s(kw.get("markersize"), 10)
        self.__plot(
            self.__x,
            self.__y,
            self.__z,
            marker=self.marker,
            alpha=self.alpha,
            label=self.label,
            s=self.s,
        )

    def __plot(self, x, y, z, label, marker, alpha, s):
        self.clear()
        self.graphdata = [
            self.ax.scatter(
                xs, ys, zs, label=label[i], marker=marker[i], alpha=alpha, s=s
            )
            for i, (xs, ys, zs) in enumerate(ThreeArray(x, y, z))
        ]
        self._apply_labels(self.xlabel, self.ylabel, self.zlabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, z=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x)
        if change_array_like(y):
            self.__y = NPNumber(y)
        if change_array_like(z):
            self.__z = NPNumber(z)
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
            s=self.s,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonumpy()

    def gety(self):
        return self.__y.tonumpy()

    def getz(self):
        return self.__z.tonumpy()

    def getcoordinate(self):
        coords = []
        for i in self.graphdata:
            offsets = np.array(i._offsets3d).T
            if len(coords) == 0:
                coords = offsets
            else:
                coords = np.vstack([coords, offsets])
        return coords
