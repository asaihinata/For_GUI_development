from sgg.dev.graph import *

__all__ = ["BarGraph"]


class BarGraph(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = tonparray(kw.get("x"), ndmax=1)
        self.__y = tonparray(kw.get("y"))
        self.logs = bols(kw.get("logs"), False)
        self.width = range_num(num0s(kw.get("width"), 1), 0, 1, 1)
        self.align = listchose(kw.get("align"), ["center", "edge"])
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            alpha=self.alpha,
            width=self.width,
            align=self.align,
            logs=self.logs,
        )

    def __plot(self, x, y, label, alpha, width, align, logs):
        self.clear()
        self.graphdata = [
            self.ax.bar(
                xs, ys, log=logs, label=label[i], alpha=alpha, width=width, align=align
            )
            for i, (xs, ys) in enumerate(TwoArray(x, y, ydtype=np.float64))
        ]
        xm = lengtharange(x)
        if np.issubdtype(x.dtype, np.number):
            xm = xm + np.min(x)
        self.set_xticks(xm, x)
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = tonparray(x, ndmax=1)
        if change_array_like(y):
            self.__y = tonparray(y)
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.align = listchose(kw.get("align"), ["center", "edge"], self.align)
        self.logs = bols(kw.get("logs"), self.logs)
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            alpha=self.alpha,
            width=self.width,
            align=self.align,
            logs=self.logs,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
