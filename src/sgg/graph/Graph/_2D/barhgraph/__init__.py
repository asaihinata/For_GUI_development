from ...dev import *

__all__ = ["BarhGraph"]


class BarhGraph(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"))
        self.__y = NPArray(kw.get("y"), depth_limit=1)
        self.logs = bols(kw.get("logs"), False)
        self.height = range_num(num0s(kw.get("height"), 1), 0, 1, 1)
        self.align = listchose(kw.get("align"), ["center", "edge"])
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            alpha=self.alpha,
            height=self.height,
            align=self.align,
            logs=self.logs,
        )

    def __plot(self, x, y, label, alpha, height, align, logs):
        self.clear()
        self.graphdata = [
            self.ax.barh(
                ys,
                xs,
                label=label[i],
                alpha=alpha,
                height=height,
                align=align,
                log=logs,
            )
            for i, (xs, ys) in enumerate(TwoArray(x, y, xdtype=np.float64))
        ]
        self.set_yticks(y.lengtharange(), y.tonp())
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x)
        if change_array_like(y):
            self.__y = NPArray(y, depth_limit=1)
        self.height = range_num(num0s(kw.get("height"), self.height), 0, 1, self.height)
        self.align = listchose(kw.get("align"), ["center", "edge"], self.align)
        self.logs = bols(kw.get("logs"), self.logs)
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            alpha=self.alpha,
            height=self.height,
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
