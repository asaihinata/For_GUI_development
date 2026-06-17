from ...dev import *

__all__ = ["Hatplot"]


class Hatplot(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"), depth_limit=1)
        self.__data = NPNumber(kw.get("data"), depth_limit=1)
        self.color = parsecolor(kw.get("color"), "#4477aa")
        self.__plot(self.__x, self.__data, color=self.color, alpha=self.alpha)

    def __plot(self, x, data, color, alpha):
        self.clear()
        self.graphdata = self.hat_graph(x, data, color=color, alpha=alpha)
        self._apply_labels(self.xlabel, self.ylabel)
        self.legend()
        self._adjustment()

    def hat_graph(self, x, data, color=None, alpha=1):
        x, data = np.array(x), np.array(data)
        xlen = np.arange(x.shape[0])
        for i, heights in enumerate(np.vstack([x, data])):
            style = {"fill": False} if i == 0 else {"edgecolor": "black"}
            rects = self.ax.bar(
                xlen - 0.15 + i * 0.35,
                heights - x,
                width=0.35,
                bottom=x,
                color=color,
                alpha=alpha,
                **style,
            )
            annotate = [
                self.ax.annotate(
                    f"{height}",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 4),
                    textcoords="offset points",
                    ha="center",
                    va="bottom",
                    alpha=alpha,
                )
                for height, rect in zip(heights, rects)
            ]
        return [rects, annotate]

    def update(self, x=None, data=None, **kw):
        self._updates(**kw)
        if isinstance(x, nListlike):
            self.__x = NPNumber(x, depth_limit=1)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data, depth_limit=1)
        self.color = parsecolor(kw.get("color"), self.color)
        self.__plot(self.__x, self.__data, color=self.color, alpha=self.alpha)
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def getdata(self):
        return self.__data.tonp()
