from ...dev import *

__all__ = ["Scatter"]


class Scatter(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPArray(kw.get("x"))
        self.__y = NPArray(kw.get("y"))
        self.marker = MarkerList(kw.get("marker", "o"))
        self.s = num1s(kw.get("markersize"), 10)
        self.regression_bool = bols(kw.get("regression_bool"), False)
        self.line = Solid(kw.get("linestyle", "-"))
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            alpha=self.alpha,
            label=self.label,
            s=self.s,
            regression_bool=self.regression_bool,
            line=self.line,
            linewidth=self.linewidth,
        )

    def __plot(
        self,
        x,
        y,
        marker,
        alpha,
        label,
        s,
        regression_bool,
        line,
        linewidth,
    ):
        self.clear()
        for i, (xs, ys) in enumerate(TwoArray(x, y)):
            scatter = self.ax.scatter(
                xs,
                ys,
                marker=marker[i],
                s=s,
                alpha=alpha,
                label=label[i],
            )
            if regression_bool:
                offsets = np.array(scatter.get_offsets())
                xs, ys = offsets[:, 0], offsets[:, 1]
                xssort = np.sort(np.unique(xs))
                regressionline = NPStatisticsds(xs, ys).chebysheveve(xssort)
                self.ax.plot(
                    xssort, regressionline, linestyle=line.solid, linewidth=linewidth
                )
            self.graphdata.append(scatter)

        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPArray(x)
        if isinstance(y, nListlike):
            self.__y = NPArray(y)
        markers = kw.get("marker", "none")
        if markers != "none":
            self.marker = MarkerList(markers)
        self.s = num1s(kw.get("markersize"), self.s)
        self.alpha = range_num(num0s(kw.get("alpha"), self.alpha), 0, 1, self.alpha)
        self.regression_bool = bols(kw.get("regression_bool"), self.regression_bool)
        self.line = Solid(kw.get("linestyle", self.line))
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.__plot(
            self.__x,
            self.__y,
            marker=self.marker,
            alpha=self.alpha,
            label=self.label,
            regression_bool=self.regression_bool,
            line=self.line,
            linewidth=self.linewidth,
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
