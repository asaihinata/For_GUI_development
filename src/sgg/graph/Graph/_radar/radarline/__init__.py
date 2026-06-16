from ...dev import *

__all__ = ["RadarLine"]


class RadarLine(RadarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.markersize = num0(kw.get("markersize"), 10)
        self.marker = Marker(kw.get("marker", ""))
        self.line = Solid(kw.get("linestyle", "-"))
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self._data,
            marker=self.marker,
            linewidth=self.linewidth,
            linestyle=self.line,
            markersize=self.markersize,
            alpha=self.alpha,
        )

    def __plot(self, data, marker, linewidth, linestyle, markersize, alpha):
        self.clear()
        self.graphdata = [
            self.ax.plot(
                self.theta,
                d,
                marker=marker.marker,
                linewidth=linewidth,
                markersize=markersize,
                linestyle=linestyle.solid,
                alpha=alpha,
            )
            for d in data
        ]
        self._adjustment()

    def update(self, **kw):
        self._updates(**kw)
        self.markersize = num0(kw.get("markersize"), self.markersize)
        marker = kw.get("marker")
        if marker is not None:
            self.marker = Marker(marker)
        line = kw.get("linestyle")
        if line is not None:
            self.line = Solid(line)
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.__plot(
            self._data,
            marker=self.marker,
            linewidth=self.linewidth,
            linestyle=self.line,
            markersize=self.markersize,
            alpha=self.alpha,
        )
        self._redraw()

    def getdata(self):
        return self._data.tonp()

    def get(self):
        return self.graphdata
