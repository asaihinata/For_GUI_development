from ...dev import *

__all__ = ["Linefill"]


class Linefill(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"), depth_limit=1)
        self.ymax = NPNumber(kw.get("ymax"), depth_limit=1)
        self.ymin = NPNumber(kw.get("ymin"), depth_limit=1)
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
        fill = self.ax.fill_between(x, ymax, ymin, alpha=alpha, label=list(self.label))
        plot = self.ax.plot(
            x, (ymax + ymin) / 2, linewidth=centerlinewidth, solid_capstyle="butt"
        )
        self.graphdata.append([fill, plot[0]])
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, ymax=None, ymin=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x, depth_limit=1)
        if change_array_like(ymax):
            self.ymax = NPNumber(ymax, depth_limit=1)
        if change_array_like(ymin):
            self.ymin = NPNumber(ymin, depth_limit=1)
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
        return self.__x.tonp()

    def getymin(self):
        return self.ymin.tonp()

    def getymax(self):
        return self.ymax.tonp()
