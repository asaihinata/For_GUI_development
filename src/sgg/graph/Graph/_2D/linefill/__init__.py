from ...dev import *

__all__ = ["Linefill"]


class Linefill(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"), max_ndim=1)
        self.ymax = NPNumber(kw.get("ymax"), max_ndim=1)
        self.ymin = NPNumber(kw.get("ymin"), max_ndim=1)
        self.centerlinewidth = num0(kw.get("centerlinewidth"), 2)
        self.alpha = range_num(num0s(kw.get("alpha"), 0.5), 0, 1, 0.5)
        self.__plot(
            self.__x,
            self.ymax,
            self.ymin,
            alpha=self.alpha,
            centerlinewidth=self.centerlinewidth,
        )

    def __plot(self, x, ymax, ymin, alpha, centerlinewidth):
        self.clear()
        x,y1,y2=x.data,ymax.data,ymin.data
        fill = self.ax.fill_between(x, y1, y2, alpha=alpha, label=list(self.label))
        plot = self.ax.plot(
            x, (y1 + y2) / 2, linewidth=centerlinewidth, solid_capstyle="butt"
        )
        self.graphdata = [fill, plot[0]]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, ymax=None, ymin=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x, max_ndim=1)
        if change_array_like(ymax):
            self.ymax = NPNumber(ymax, max_ndim=1)
        if change_array_like(ymin):
            self.ymin = NPNumber(ymin, max_ndim=1)
        self.centerlinewidth = num0(kw.get("centerlinewidth"), self.centerlinewidth)
        self.__plot(
            self.__x,
            self.ymax,
            self.ymin,
            alpha=self.alpha,
            centerlinewidth=self.centerlinewidth,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x

    def getymin(self):
        return self.ymin

    def getymax(self):
        return self.ymax
