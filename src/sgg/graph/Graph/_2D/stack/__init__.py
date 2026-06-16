from itertools import product

from ...dev import *

__all__ = ["Stack"]


class Stack(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPArray(kw.get("x"), depth_limit=1)
        self.__y = NPNumber(kw.get("y"))
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
            for i, (xs, ys) in enumerate(product(x, y))
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPArray(x, depth_limit=1)
        if isinstance(y, nListlike):
            self.__y = NPNumber(y)
        self.baseline = listchose(
            kw.get("baseline"),
            ["zero", "sym", "wiggle", "weighted_wiggle"],
            self.baseline,
        )
        hatch = kw.get("hatch", None)
        self.hatch = parameters(hatch, self.hatch, Hatch(hatch))
        self.__plot(
            self.__x,
            self.__y,
            label=self.label,
            hatch=self.hatch,
            baseline=self.baseline,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
