from itertools import product

from sgg.graph.graph.dev import *

__all__ = ["LineGraph"]


class LineGraph(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = np.array(kw.get("x"))
        self.__y = np.array(kw.get("y"))
        self.marker = MarkerList(kw.get("marker", "none"))
        self.markersize = num0(kw.get("markersize"), 10)
        self.line = Solidlist(kw.get("linestyle", "-"))
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            linewidth=self.linewidth,
            linestyle=self.line,
            markersize=self.markersize,
            alpha=self.alpha,
            label=self.label,
        )

    def __plot(
        self,
        x,
        y,
        marker,
        linewidth,
        linestyle,
        markersize,
        alpha,
        label,
    ):
        self.clear()
        self.graphdata = [
            self.ax.plot(
                xs,
                ys,
                linestyle=linestyle[i],
                linewidth=linewidth,
                marker=marker[i],
                markersize=markersize,
                alpha=alpha,
                label=label[i],
            )
            for i, (xs, ys) in enumerate(TwoArray(x, y, ydtype=np.float64))
        ][0]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = np.array(x)
        if change_array_like(y):
            self.__y = np.array(y)
        markers = kw.get("marker")
        if markers is not None:
            self.marker = MarkerList(markers)
        self.markersize = num0(kw.get("markersize"), self.markersize)
        lines = kw.get("linestyle")
        if lines is not None:
            self.line = Solidlist(lines)
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            linewidth=self.linewidth,
            linestyle=self.line,
            markersize=self.markersize,
            alpha=self.alpha,
            label=self.label,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
