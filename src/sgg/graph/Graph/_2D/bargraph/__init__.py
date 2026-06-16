from ...dev import *

__all__ = ["BarGraph"]


class BarGraph(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPArray(kw.get("x"), depth_limit=1)
        self.__y = NPNumber(kw.get("y"))
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
        self.set_xticks(x.lengtharange(), x.tonp())
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPArray(x, depth_limit=1)
        if isinstance(y, nListlike):
            self.__y = NPNumber(y)
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
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
