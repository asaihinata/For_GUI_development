from ...dev import *

__all__ = ["Hexbin"]


class Hexbin(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"))
        self.__y = NPNumber(kw.get("y"))
        c, extent, gridsize = kw.get("c"), kw.get("extent"), kw.get("gridsize", 100)
        self.c = None if c is None else NPNumber(c)
        self.gridsize = (
            gridsize if list2int(gridsize) or isinstance(gridsize, int) else 100
        )
        self.extent = extent if list4float(extent) else None
        self.xscale = listchose(kw.get("xscale"), ["linear", "log"])
        self.yscale = listchose(kw.get("yscale"), ["linear", "log"])
        self.mincnt = int1s(kw.get("mincnt"))
        bins = kw.get("bins")
        self.bins = (
            bins
            if (
                bins == "log"
                or isinstance(bins, int | float)
                or (
                    isinstance(bins, list | tuple)
                    and (isinstance(i, int | float) for i in bins)
                )
            )
            else None
        )
        self.__plot(
            self.__x,
            self.__y,
            self.c,
            gridsize=self.gridsize,
            xscale=self.xscale,
            yscale=self.yscale,
            mincnt=self.mincnt,
            extent=self.extent,
            bins=self.bins,
        )

    def __plot(
        self,
        x,
        y,
        c,
        gridsize,
        xscale,
        yscale,
        mincnt,
        extent,
        bins,
    ):
        self.clear()
        self.graphdata = [
            self.ax.hexbin(
                x,
                y,
                c,
                bins=bins,
                gridsize=gridsize,
                xscale=xscale,
                yscale=yscale,
                mincnt=mincnt,
                extent=extent,
            )
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def update(self, x=None, y=None, c=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x)
        if change_array_like(y):
            self.__y = NPNumber(y)
        if change_array_like(c):
            self.c = NPNumber(c)
        extent, gridsize = kw.get("extent", self.extent), kw.get(
            "gridsize", self.gridsize
        )
        self.gridsize = (
            gridsize if list2int(gridsize) or isinstance(gridsize, int) else 100
        )
        self.extent = extent if list4float(extent) else None
        self.xscale = listchose(kw.get("xscale"), ["linear", "log"], self.xscale)
        self.yscale = listchose(kw.get("yscale"), ["linear", "log"], self.yscale)
        self.mincnt = int1s(kw.get("mincnt", self.mincnt))
        bins = kw.get("bins", self.bins)
        self.bins = (
            bins
            if (
                bins == "log"
                or isinstance(bins, int | float)
                or (
                    isinstance(bins, list | tuple)
                    and (isinstance(i, int | float) for i in bins)
                )
            )
            else None
        )
        self.__plot(
            self.__x,
            self.__y,
            self.c,
            gridsize=self.gridsize,
            xscale=self.xscale,
            yscale=self.yscale,
            mincnt=self.mincnt,
            extent=self.extent,
            bins=self.bins,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
