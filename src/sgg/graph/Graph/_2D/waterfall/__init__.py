from ...dev import *

__all__ = ["Waterfall"]


class Waterfall(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPArray(kw.get("x"), depth_limit=1)
        self.__y = NPNumber(kw.get("y"), depth_limit=1)
        self.bottom = np.cumsum(np.append(0, self.__y)[0 : self.__y.size])
        self.ucolor = parsecolor(kw.get("ucolor"), "#156082")
        self.dcolor = parsecolor(kw.get("dcolor"), "#e97132")
        self.width = range_num(num0s(kw.get("width"), 1), 0, 1, 1)
        self.sums = bols(kw.get("sums"), False)
        self.sumstext = kw.get("sumstext", "sum")
        self.colorline = parsecolor(kw.get("colorline"), "#4477aa")
        self.linestyle = Solid(kw.get("linestyle", "-")).solid
        self.__plot(
            self.__x,
            self.__y,
            alpha=self.alpha,
            width=self.width,
            sums=self.sums,
            sumstext=self.sumstext,
            bottom=self.bottom,
            color=self.colorline,
            linestyle=self.linestyle,
            ucolor=self.ucolor,
            dcolor=self.dcolor,
        )

    def __plot(
        self,
        x,
        y,
        alpha,
        width,
        sums,
        sumstext,
        bottom,
        color,
        linestyle,
        ucolor,
        dcolor,
    ):
        self.clear()
        x, y = x.tonp(), y.tonp()
        if sums:
            x = np.append(x, sumstext)
            y = np.append(y, np.sum(y))
            bottom = np.append(bottom, 0)
        self.color = np.where(y <= 0, dcolor, ucolor)
        self.graphdata = [
            self.ax.bar(
                x,
                y,
                color=self.color,
                alpha=alpha,
                width=width,
                align="center",
                bottom=bottom,
            )
        ]
        self.ax.set_xticks(np.arange(len(x)), labels=x.tolist())
        yticks = self.ax.get_yticks()
        self.ax.set_ylim(yticks.min(), yticks.max())
        if width != 1:
            self._horiline(np.cumsum(y), width, color, linestyle)
        self._apply_labels(self.xlabel, self.ylabel)

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPArray(x, depth_limit=1)
        if change_array_like(y):
            self.__y = NPNumber(y, depth_limit=1)
        self.sums = bols(kw.get("sums"), self.sums)
        self.sumstext = kw.get("sumstext", self.sumstext)
        self.bottom = np.cumsum(np.append(0, self.__y)[0 : self.__y.size])
        self.ucolor = parsecolor(kw.get("ucolor"), self.ucolor)
        self.dcolor = parsecolor(kw.get("dcolor"), self.dcolor)
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.colorline = parsecolor(kw.get("colorline"), self.colorline)
        self.linestyle = Solid(kw.get("linestyle", self.linestyle)).solid
        self.__plot(
            self.__x,
            self.__y,
            alpha=self.alpha,
            width=self.width,
            sums=self.sums,
            sumstext=self.sumstext,
            bottom=self.bottom,
            color=self.colorline,
            linestyle=self.linestyle,
            ucolor=self.ucolor,
            dcolor=self.dcolor,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()

    def _horiline(self, lin, width=1, color=None, linestyle="-"):
        lens, width, xmaxs, xmins = len(lin) - 1, width / 2, [], []
        for i in range(lens):
            if lin[i] == lin[i + 1]:
                ma, mi = i + width, i + 1.5
            else:
                ma, mi = i + 1 - width, i + width
            xmaxs.append(ma)
            xmins.append(mi)
        self.ax.hlines(
            y=lin,
            xmin=xmins + [0],
            xmax=xmaxs + [0],
            colors=color,
            linestyles=linestyle,
        )
