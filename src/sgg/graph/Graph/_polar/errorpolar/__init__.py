from ...dev import *

__all__ = ["Errorpolar"]


class Errorpolar(polarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x, self.__y = self._xyd(kw.get("x"), kw.get("y"), kw.get("data"))
        err = kw.get("err")
        xerr = kw.get("xerr")
        yerr = kw.get("yerr")
        self.xerr = None
        self.yerr = None
        if err is not None:
            self.err = NPNumber(err)
            self.xerr, self.yerr = self.err, self.err
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
        if (
            isinstance(errorevery, list | tuple)
            and len(errorevery) == 2
            and all(isinstance(i, int) for i in errorevery)
        ) or isinstance(errorevery, int):
            self.errorevery = errorevery
        else:
            self.errorevery = 1
        self.__plot(
            self.__x,
            self.__y,
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
        self.graphdata = self.ax.errorbar(
            x,
            y,
            fmt=fmt,
            xerr=xerr,
            yerr=yerr,
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
        self._adjustment()

    def update(self, x=None, y=None, data=None, **kw):
        self._updates(**kw)
        if not isinstance(x, nListlike):
            x = self.__x
        if not isinstance(y, nListlike):
            y = self.__y
        self.__x, self.__y = self._xyd(x, y, data)
        err, xerr, yerr = (
            kw.get("err", self.err),
            kw.get("xerr", self.xerr),
            kw.get("yerr", self.yerr),
        )
        if err is not None:
            self.err = NPNumber(err)
            self.xerr, self.yerr = self.err, self.err
        if xerr is not None:
            self.xerr = NPNumber(xerr)
        if yerr is not None:
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
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
