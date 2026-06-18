from itertools import product

from ...dev import *

__all__ = ["Errorbar"]


class Errorbar(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"))
        self.__y = NPNumber(kw.get("y"))
        err = kw.get("err")
        xerr = kw.get("xerr")
        yerr = kw.get("yerr")
        self.xerr = None
        self.yerr = None
        if err is not None:
            self.yerr = self.xerr = self.err = NPNumber(err)
        if xerr is not None:
            self.xerr = NPNumber(xerr)
        if yerr is not None:
            self.yerr = NPNumber(yerr)
        self.xuplims = bols(kw.get("xuplims"), False)
        self.xlolims = bols(kw.get("xlolims"), False)
        self.yuplims = bols(kw.get("yuplims"), False)
        self.ylolims = bols(kw.get("ylolims"), False)
        self.barsabove = bols(kw.get("barsabove"), False)
        self.line = kw.get("linestyle")
        self.marker = kw.get("marker", "o")
        self.fmt = FMT(self.marker, self.line).txt
        self.linewidth = num0(kw.get("linewidth"), 1.5)
        self.capthick = nums(kw.get("capthick"), 10)
        self.capsize = nums(kw.get("capsize"), 0)
        errorevery = kw.get("errorevery")
        if isinstance(errorevery, int) or (
            change_array_like(errorevery) and NPNumber(errorevery).shapesize((1, 2))
        ):
            self.errorevery = errorevery
        else:
            self.errorevery = 1
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            xerr=self.xerr,
            yerr=self.yerr,
            fmt=self.fmt,
            linewidth=self.linewidth,
            capsize=self.capsize,
            barsabove=self.barsabove,
            capthick=self.capthick,
            xuplims=self.xuplims,
            xlolims=self.xlolims,
            yuplims=self.yuplims,
            ylolims=self.ylolims,
            errorevery=self.errorevery,
            alpha=self.alpha,
        )

    def __plot(
        self,
        x,
        y,
        label,
        xerr,
        yerr,
        fmt,
        linewidth,
        capsize,
        barsabove,
        capthick,
        xuplims,
        xlolims,
        yuplims,
        ylolims,
        errorevery,
        alpha,
    ):
        self.clear()
        self.graphdata = [
            self.ax.errorbar(
                xs,
                ys,
                fmt=fmt,
                xerr=xerr,
                yerr=yerr,
                label=label[i],
                elinewidth=linewidth,
                capthick=capthick,
                capsize=capsize,
                barsabove=barsabove,
                xuplims=xuplims,
                xlolims=xlolims,
                uplims=yuplims,
                lolims=ylolims,
                errorevery=errorevery,
                alpha=alpha,
            )
            for i, (xs, ys) in enumerate(product(x, y))
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, err=None, xerr=None, yerr=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPNumber(x)
        if isinstance(y, nListlike):
            self.__y = NPNumber(y)
        if isinstance(err, nListlike):
            self.yerr = self.xerr = self.err = NPNumber(err)
        if isinstance(xerr, nListlike):
            self.xerr = NPNumber(xerr)
        if isinstance(yerr, nListlike):
            self.yerr = NPNumber(yerr)
        self.xuplims = bols(kw.get("xuplims"), self.xuplims)
        self.xlolims = bols(kw.get("xlolims"), self.xlolims)
        self.yuplims = bols(kw.get("yuplims"), self.yuplims)
        self.ylolims = bols(kw.get("ylolims"), self.ylolims)
        self.barsabove = bols(kw.get("barsabove"), self.barsabove)
        self.line = kw.get("linestyle", self.line)
        self.marker = kw.get("marker", self.marker)
        self.fmt = FMT(self.marker, self.line).txt
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.capthick = nums(kw.get("capthick"), self.capthick)
        self.capsize = nums(kw.get("capsize"), self.capsize)
        errorevery = kw.get("errorevery", self.errorevery)
        self.errorevery = (
            errorevery
            if (
                isinstance(errorevery, list | tuple)
                and len(errorevery) == 2
                and all(isinstance(i, int) for i in errorevery)
            )
            or isinstance(errorevery, int)
            else 1
        )
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            xerr=self.xerr,
            yerr=self.yerr,
            fmt=self.fmt,
            linewidth=self.linewidth,
            capsize=self.capsize,
            barsabove=self.barsabove,
            capthick=self.capthick,
            xuplims=self.xuplims,
            xlolims=self.xlolims,
            yuplims=self.yuplims,
            ylolims=self.ylolims,
            errorevery=self.errorevery,
            alpha=self.alpha
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
