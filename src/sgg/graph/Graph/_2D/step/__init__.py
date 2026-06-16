from ...dev import *

__all__ = ["Step"]


class Step(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        self.fill = bols(kw.get("fill"), False)
        self.baseline = num0s(kw.get("baseline"))
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.linewidth = num0(kw.get("linewidth"), 2)
        self.__plot(
            self.__data,
            linewidth=self.linewidth,
            fill=self.fill,
            baseline=self.baseline,
            orientation=self.orientation,
            alpha=self.alpha,
        )

    def __plot(self, data, linewidth, fill, baseline, orientation, alpha):
        self.clear()
        self.graphdata = [
            self.ax.stairs(
                d,
                linewidth=linewidth,
                baseline=baseline,
                fill=fill,
                orientation=orientation,
                label=self.label[i],
                alpha=alpha,
            )
            for i, d in enumerate(data)
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, data=None, **kw):
        self._updates(**kw)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data)
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.fill = bols(kw.get("fill"), self.fill)
        self.baseline = num0s(kw.get("baseline"), self.baseline)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        self.__plot(
            self.__data,
            linewidth=self.linewidth,
            fill=self.fill,
            baseline=self.baseline,
            orientation=self.orientation,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
