from ...dev import *

__all__ = ["Hist2d"]


class Hist2d(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"), depth_limit=1)
        self.__y = NPNumber(kw.get("y"), depth_limit=1)
        self.max, self.min = nums(kw.get("max")), nums(kw.get("min"))
        if (
            isinstance(self.max, int | float)
            and isinstance(self.min, int | float)
            and self.max < self.min
        ):
            self.max, self.min = self.min, self.max
        self.xmax = self._powsmax(nums(kw.get("xmax")), self.__x)
        self.xmin = self._powsmin(nums(kw.get("xmin")), self.__x)
        self.ymax = self._powsmax(nums(kw.get("ymax")), self.__y)
        self.ymin = self._powsmin(nums(kw.get("ymin")), self.__y)
        if self.xmax < self.xmin:
            self.xmin, self.xmax = self.xmax, self.xmin
        if self.ymax < self.ymin:
            self.ymin, self.ymax = self.ymax, self.ymin
        self.range = ((self.xmin, self.xmax), (self.ymin, self.ymax))
        self.bins = self._bins(kw.get("bins", 10))
        self.density = bols(kw.get("density"), False)
        self.__plot(
            self.__x,
            self.__y,
            bins=self.bins,
            alpha=self.alpha,
            density=self.density,
            range=self.range,
            max=self.max,
            min=self.min,
        )

    def __plot(self, x, y, bins, alpha, density, range, min, max):
        self.clear()
        self.graphdata = [
            self.ax.hist2d(
                x,
                y,
                bins=bins,
                alpha=alpha,
                density=density,
                range=range,
                cmax=max,
                cmin=min,
            )
        ]
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def update(self, x=None, y=None, **kw):
        self._updates(**kw)
        if change_array_like(x):
            self.__x = NPNumber(x, depth_limit=1)
        if change_array_like(y):
            self.__y = NPNumber(y, depth_limit=1)
        self.max = nums(kw.get("max"), self.max)
        self.min = nums(kw.get("min"), self.min)
        if (
            isinstance(self.max, int | float)
            and isinstance(self.min, int | float)
            and self.max < self.min
        ):
            self.max, self.min = self.min, self.max
        self.xmax = self._powsmax(nums(kw.get("xmax"), self.xmax), self.__x)
        self.xmin = self._powsmin(nums(kw.get("xmin"), self.xmin), self.__x)
        self.ymax = self._powsmax(nums(kw.get("ymax"), self.ymax), self.__y)
        self.ymin = self._powsmin(nums(kw.get("ymin"), self.ymin), self.__y)
        if self.xmax < self.xmin:
            self.xmin, self.xmax = self.xmax, self.xmin
        if self.ymax < self.ymin:
            self.ymin, self.ymax = self.ymax, self.ymin
        self.range = ((self.xmin, self.xmax), (self.ymin, self.ymax))
        self.bins = self._bins(kw.get("bins", self.bins))
        self.density = bols(kw.get("density"), self.density)
        self.alpha = range_num(num0s(kw.get("alpha"), self.alpha), 0, 1, self.alpha)
        self.__plot(
            self.__x,
            self.__y,
            bins=self.bins,
            alpha=self.alpha,
            density=self.density,
            range=self.range,
            max=self.max,
            min=self.min,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()

    def _powsmax(self, val, range):
        if val == None:
            maxs = range.max()
            if maxs < 0:
                return np.pow(10, np.ceil(np.log10(np.abs(maxs))) - 1) * -1
            return np.pow(10, np.ceil(np.log10(maxs)))
        return val

    def _powsmin(self, val, range):
        if val == None:
            mins = range.min()
            if mins < 0:
                return np.pow(10, np.ceil(np.log10(np.abs(mins)))) * -1
            return np.pow(10, np.ceil(np.log10(mins)) - 1)
        return val

    def _bins(self, val):
        if (
            isinstance(val, int)
            or (
                isinstance(val, np.ndarray)
                and len(val.shape) == 1
                and 2 <= val.shape[0]
            )
            or (
                isinstance(val, list | tuple)
                and (
                    (
                        len(val) == 2
                        and all(isinstance(val[i], list | tuple) for i in range(2))
                    )
                    or (1 <= len(val) and all(isinstance(i, int) for i in val))
                )
            )
        ):
            return val
        return 10
