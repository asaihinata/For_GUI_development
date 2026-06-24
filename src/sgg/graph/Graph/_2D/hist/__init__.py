from ...dev import *

__all__ = ["Hist"]


class Hist(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        bins = kw.get("bins")
        if isinstance(bins, list | range | tuple | np.ndarray) or bins in [
            "auto",
            "fd",
            "doane",
            "scott",
            "stone",
            "rice",
            "sturges",
            "sqrt",
        ]:
            self.bins = bins
        elif isinstance(bins, int):
            self.bins = num1s(bins, round(self.__data.sturgesval))
        else:
            self.bins = round(self.__data.sturgesval)
        self.min = nums(kw.get("min"), self.__data.min())
        self.max = nums(kw.get("max"), self.__data.max())
        self.bottom = num0s(kw.get("bottom"))
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.width = range_num(num0s(kw.get("width"), 1), 0, 1, 1)
        self.__plot(
            self.__data,
            label=self.label,
            bins=self.bins,
            ranges=(self.min, self.max),
            bottom=self.bottom,
            orientation=self.orientation,
            width=self.width,
            alpha=self.alpha,
        )

    def __plot(
        self,
        data,
        label,
        bins,
        ranges,
        bottom,
        orientation,
        width,
        alpha,
    ):
        self.clear()
        hist = self.ax.hist(
            data,
            label=label,
            bins=bins,
            range=ranges,
            bottom=bottom,
            rwidth=width,
            orientation=orientation,
            alpha=alpha,
        )
        tickslist = hist[1]
        tickslists = tickslist.astype(int).tolist()
        self._apply_labels(self.xlabel, self.ylabel)
        if orientation == "vertical":
            self.ax.set_xticks(tickslist, tickslists)
        else:
            self.ax.set_yticks(tickslist, tickslists)
        self.graphdata = [hist]
        self.legend()
        self._adjustment()

    def update(self, data=None, **kw):
        self._updates(**kw)
        if change_array_like(data):
            self.__data = NPNumber(data)
        bins = kw.get("bins")
        if isinstance(bins, list | range | tuple | np.ndarray) or bins in [
            "auto",
            "fd",
            "doane",
            "scott",
            "stone",
            "rice",
            "sturges",
            "sqrt",
        ]:
            self.bins = bins
        elif isinstance(bins, int):
            self.bins = num1s(bins, round(self.__data.sturgesval))
        self.min = nums(kw.get("min"), self.__data.min())
        self.max = nums(kw.get("max"), self.__data.max())
        self.bottom = num0s(kw.get("bottom"), self.bottom)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.__plot(
            self.__data,
            label=self.label,
            bins=self.bins,
            ranges=(self.min, self.max),
            bottom=self.bottom,
            orientation=self.orientation,
            width=self.width,
            alpha=self.alpha,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
