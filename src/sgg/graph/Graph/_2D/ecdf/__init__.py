from ...dev import *

__all__ = ["Ecdf"]


class Ecdf(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"), depth_limit=1)
        self.complementary = bols(kw.get("complementary"), False)
        self.compress = bols(kw.get("compress"), False)
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.line = Solidlist(kw.get("linestyle", "-"))
        self.linewidth = num0(kw.get("linewidth"), 1.5)
        self.__plot(
            self.__data,
            complementary=self.complementary,
            compress=self.compress,
            orientation=self.orientation,
            linewidth=self.linewidth,
            line=self.line,
            alpha=self.alpha,
        )

    def __plot(
        self,
        data,
        complementary,
        compress,
        orientation,
        linewidth,
        line,
        alpha,
    ):
        self.clear()
        self.graphdata = [
            self.ax.ecdf(
                ds,
                compress=compress,
                complementary=complementary,
                orientation=orientation,
                linewidth=linewidth,
                linestyle=line[i],
                alpha=alpha,
            )
            for i, ds in enumerate(data)
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def update(self, data=None, **kw):
        self._updates(**kw)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data, depth_limit=1)
        self.complementary = bols(kw.get("complementary"), self.complementary)
        self.compress = bols(kw.get("compress"), self.compress)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        lines = kw.get("linestyle", None)
        self.line = parameters(lines, self.line, Solidlist(lines))
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.__plot(
            self.__data,
            complementary=self.complementary,
            compress=self.compress,
            orientation=self.orientation,
            linewidth=self.linewidth,
            line=self.line,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
