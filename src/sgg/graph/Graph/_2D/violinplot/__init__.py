from types import FunctionType

from ...dev import *

__all__ = ["Violinplot"]


class Violinplot(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        self.__x = NPNumber(kw.get("x", []), depth_limit=1)
        self.__y = NPNumber(kw.get("y", []), depth_limit=1)
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.width = range_num(num0s(kw.get("width"), 1), 0, 1, 1)
        self.showextrema = bols(kw.get("showextrema"))
        self.showmeans = bols(kw.get("showmeans"), False)
        self.showmedians = bols(kw.get("showmedians"), False)
        self.points = num1s(kw.get("points"), 100)
        bwmethod = kw.get("bw_method", "scott")
        if bwmethod in ["scott", "silverman"]:
            self.bwmethod = bwmethod
        elif isinstance(bwmethod, int | float | FunctionType):
            self.bwmethod = bwmethod
        else:
            self.bwmethod = "scott"
        self.side = listchose(kw.get("side"), ["both", "low", "high"])
        self.__plot(
            self.__data,
            self.__x,
            self.__y,
            alpha=self.alpha,
            width=self.width,
            points=self.points,
            showextrema=self.showextrema,
            showmeans=self.showmeans,
            showmedians=self.showmedians,
            side=self.side,
            orientation=self.orientation,
            bwmethod=self.bwmethod,
        )

    def __plot(
        self,
        data,
        x,
        y,
        alpha,
        width,
        points,
        showextrema,
        showmeans,
        showmedians,
        side,
        orientation,
        bwmethod,
    ):
        self.clear()
        if orientation == "vertical" and x.size != 0:
            positions = x.tonp()
        elif orientation == "horizontal" and y.size != 0:
            positions = y.tonp()
        else:
            positions = np.arange(1, data.shape[1] + 1)
        self.graphdata = [
            self.ax.violinplot(
                data.tonp(),
                positions=positions,
                widths=width,
                points=points,
                showextrema=showextrema,
                showmedians=showmedians,
                showmeans=showmeans,
                side=side,
                orientation=orientation,
                bw_method=bwmethod,
            )
        ]
        for i in self.graphdata[0]["bodies"]:
            i.set_alpha(alpha)
        self._adjustment()

    def update(self, data=None, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(data):
            self.__data = NPNumber(data)
        if change_array_like(x):
            self.__x = NPNumber(x, depth_limit=1)
        if change_array_like(y):
            self.__y = NPNumber(y, depth_limit=1)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.showextrema = bols(kw.get("showextrema"), self.showextrema)
        self.showmeans = bols(kw.get("showmeans"), self.showmeans)
        self.showmedians = bols(kw.get("showmedians"), self.showmedians)
        self.points = num1s(kw.get("points"), self.points)
        bwmethod = kw.get("bw_method")
        if bwmethod in ["scott", "silverman"] or isinstance(
            bwmethod, int | float | FunctionType
        ):
            self.bwmethod = bwmethod
        self.side = listchose(kw.get("side"), ["both", "low", "high"], self.side)
        self.__plot(
            self.__data,
            self.__x,
            self.__y,
            alpha=self.alpha,
            width=self.width,
            points=self.points,
            showextrema=self.showextrema,
            showmeans=self.showmeans,
            showmedians=self.showmedians,
            side=self.side,
            orientation=self.orientation,
            bwmethod=self.bwmethod,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
