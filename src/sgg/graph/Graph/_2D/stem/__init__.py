from ...dev import *

__all__ = ["Stem"]


class Stem(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"))
        self.__y = NPNumber(kw.get("y"))
        self.linefmt = kw.get("linefmt", None)
        self.markerfmt = kw.get("markerfmt", None)
        self.basefmt = kw.get("basefmt", None)
        self.bottom = num0s(kw.get("bottom"))
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.__plot(
            self.__x,
            self.__y,
            bottom=self.bottom,
            orientation=self.orientation,
            label=self.label,
            linefmt=self.linefmt,
            markerfmt=self.markerfmt,
            basefmt=self.basefmt,
            alpha=self.alpha,
        )

    def __plot(
        self,
        x,
        y,
        bottom,
        orientation,
        label,
        linefmt,
        markerfmt,
        basefmt,
        alpha,
    ):
        self.clear()
        for i, (xs, ys) in enumerate(TwoArray(x, y)):
            stem = self.ax.stem(
                xs,
                ys,
                linefmt=linefmt,
                markerfmt=markerfmt,
                basefmt=basefmt,
                bottom=bottom,
                orientation=orientation,
                label=label[i],
            )
            for j in stem.get_children():
                j.set_alpha(alpha)
            self.graphdata.append(stem)
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x)
        if change_array_like(y):
            self.__y = NPNumber(y)
        self.linefmt = kw.get("linefmt", self.linefmt)
        self.markerfmt = kw.get("markerfmt", self.markerfmt)
        self.basefmt = kw.get("basefmt", self.basefmt)
        self.bottom = num0s(kw.get("bottom"), self.bottom)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        self.__plot(
            self.__x,
            self.__y,
            bottom=self.bottom,
            orientation=self.orientation,
            label=self.label,
            alpha=self.alpha,
            basefmt=self.basefmt,
            markerfmt=self.markerfmt,
            linefmt=self.linefmt,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()
