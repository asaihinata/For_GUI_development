from sgg.graph.graph.dev import *

__all__ = ["Stack"]


class Stack(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = np.array(kw.get("x"), ndmax=1)
        self.__y = np.array(kw.get("y"))
        self.baseline = listchose(
            kw.get("baseline"), ["zero", "sym", "wiggle", "weighted_wiggle"]
        )
        self.hatch = Hatch(kw.get("hatch"))
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            hatch=self.hatch,
            baseline=self.baseline,
            alpha=self.alpha,
        )

    def __plot(self, x, y, label, hatch, baseline, alpha):
        self.clear()
        self.graphdata = [
            self.ax.stackplot(
                xs, ys, labels=label, hatch=hatch[i], baseline=baseline, alpha=alpha
            )
            for i, (xs, ys) in enumerate(
                TwoArray(x, y, xdtype=np.float64, ydtype=np.float64)
            )
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = np.array(x, ndmax=1)
        if change_array_like(y):
            self.__y = np.array(y)
        self.baseline = listchose(
            kw.get("baseline"),
            ["zero", "sym", "wiggle", "weighted_wiggle"],
            self.baseline,
        )
        hatch = kw.get("hatch")
        if hatch is not None:
            self.hatch = Hatch(hatch)
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            hatch=self.hatch,
            baseline=self.baseline,
            alpha=self.alpha,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
