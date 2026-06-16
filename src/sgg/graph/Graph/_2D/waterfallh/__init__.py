from ...dev import *

__all__ = ["Waterfallh"]


class Waterfallh(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPArray(kw.get("x"), depth_limit=1)
        self.__y = NPNumber(kw.get("y"), depth_limit=1)
        self.bottom = np.cumsum(np.append(0, self.__y)[0 : self.__y.size])
        self.ucolor = parsecolor(kw.get("ucolor"), "#156082")
        self.dcolor = parsecolor(kw.get("dcolor"), "#e97132")
        self.height = range_num(num0s(kw.get("height"), 1), 0, 1, 1)
        self.sums = bols(kw.get("sums"), False)
        self.sumstext = kw.get("sumstext", "sum")
        self.colorline = parsecolor(kw.get("colorline"), "#4477aa")
        self.linestyle = Solid(kw.get("linestyle", "-")).solid
        self.__plot(
            self.__x,
            self.__y,
            alpha=self.alpha,
            height=self.height,
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
        height,
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
            self.ax.barh(
                x,
                y,
                color=self.color,
                alpha=alpha,
                height=height,
                align="center",
                left=bottom,
            )
        ]
        if height != 1:
            self._vlines(np.cumsum(y), height, color, linestyle)
        self.ax.set_yticks(np.arange(len(x)), labels=x.tolist())
        xticks = self.ax.get_xticks()
        self.ax.set_xlim(xticks.min(), xticks.max())
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPArray(x, depth_limit=1)
        if isinstance(y, nListlike):
            self.__y = NPNumber(y, depth_limit=1)
        self.bottom = np.cumsum(np.append(0, self.__y)[0 : self.__y.size])
        self.sums = bols(kw.get("sums"), self.sums)
        self.sumstext = kw.get("sumstext", self.sumstext)
        self.ucolor = parsecolor(kw.get("ucolor"), self.ucolor)
        self.dcolor = parsecolor(kw.get("dcolor"), self.dcolor)
        self.height = range_num(num0s(kw.get("height"), self.height), 0, 1, self.height)
        self.colorline = parsecolor(kw.get("colorline"), self.colorline)
        self.linestyle = Solid(kw.get("linestyle", self.linestyle)).solid
        self.__plot(
            self.__x,
            self.__y,
            alpha=self.alpha,
            height=self.height,
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

    def _vlines(self, lin, height=1, color=None, linestyle="-"):
        lens, height, xmaxs, xmins = len(lin) - 1, height / 2, [], []
        for i in range(lens):
            if lin[i] == lin[i + 1]:
                ma, mi = i + height, i + 1.5
            else:
                ma, mi = i + 1 - height, i + height
            xmaxs.append(ma)
            xmins.append(mi)
        self.ax.vlines(
            x=lin,
            ymin=xmins + [0],
            ymax=xmaxs + [0],
            colors=color,
            linestyles=linestyle,
        )
