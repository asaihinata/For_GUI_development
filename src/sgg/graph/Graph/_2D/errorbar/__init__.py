from sgg.graph.graph.dev import *

__all__ = ["Errorbar"]


class Errorbar(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = tonparray(kw.get("x"))
        self.__y = tonparray(kw.get("y"))
        err = kw.get("err")
        xerr = kw.get("xerr")
        yerr = kw.get("yerr")
        self.xerr = None
        self.yerr = None
        if err is not None:
            self.yerr = self.xerr = self.err = tonparray(err)
        if xerr is not None:
            self.xerr = tonparray(xerr)
        if yerr is not None:
            self.yerr = tonparray(yerr)
        self.xuplims = bols(kw.get("xuplims"), False)
        self.xlolims = bols(kw.get("xlolims"), False)
        self.yuplims = bols(kw.get("yuplims"), False)
        self.ylolims = bols(kw.get("ylolims"), False)
        self.barsabove = bols(kw.get("barsabove"), False)
        self.linewidth = num0(kw.get("linewidth"), 1.5)
        self.capthick = nums(kw.get("capthick"), 10)
        self.capsize = nums(kw.get("capsize"), 0)
        errorevery = kw.get("errorevery")
        if isinstance(errorevery, int) or (
            change_array_like(errorevery) and tonparray(errorevery).shape == ((1, 2))
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
                xerr=xerr,
                yerr=yerr,
                label=label[i],
                elinewidth=linewidth,
                fmt="none",
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
            for i, (xs, ys) in enumerate(TwoArray(x, y, ydtype=np.float64))
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, err=None, xerr=None, yerr=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = tonparray(x)
        if change_array_like(y):
            self.__y = tonparray(y)
        if change_array_like(err):
            self.yerr = self.xerr = self.err = tonparray(err)
        if change_array_like(xerr):
            self.xerr = tonparray(xerr)
        if change_array_like(yerr):
            self.yerr = tonparray(yerr)
        self.xuplims = bols(kw.get("xuplims"), self.xuplims)
        self.xlolims = bols(kw.get("xlolims"), self.xlolims)
        self.yuplims = bols(kw.get("yuplims"), self.yuplims)
        self.ylolims = bols(kw.get("ylolims"), self.ylolims)
        self.barsabove = bols(kw.get("barsabove"), self.barsabove)
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.capthick = nums(kw.get("capthick"), self.capthick)
        self.capsize = nums(kw.get("capsize"), self.capsize)
        errorevery = kw.get("errorevery", self.errorevery)
        if isinstance(errorevery, int) or (
            change_array_like(errorevery) and tonparray(errorevery).shape == ((1, 2))
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
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
