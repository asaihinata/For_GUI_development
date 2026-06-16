from ...dev import *

__all__ = ["RadarFill"]


class RadarFill(RadarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__plot(self._data, alpha=self.alpha)

    def __plot(self, data, alpha):
        self.clear()
        self.graphdata = [self.ax.fill(self.theta, d, alpha=alpha) for d in data][0]
        self._adjustment()

    def update(self, **kw):
        self._updates(**kw)
        self.__plot(self._data, alpha=self.alpha)
        self._redraw()

    def getdata(self):
        return self._data.tonp()

    def get(self):
        return self.graphdata
