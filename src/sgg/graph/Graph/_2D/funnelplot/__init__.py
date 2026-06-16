from matplotlib.ticker import MaxNLocator

from ...dev import *

__all__ = ["Funne"]


class Funne(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"), depth_limit=1)
        self.height = range_num(num0s(kw.get("height"), 1), 0, 1, 1)
        xmajormaxbins = intsmin(kw.get("xmajormaxbins"), 3, 11)
        if not isinstance(xmajormaxbins, int):
            raise TypeError("xmajormaxbinsに整数を指定してください")
        elif xmajormaxbins % 2 == 0:
            raise ValueError("xmajormaxbinsは2n+1の整数で指定してください")
        else:
            self.xmajormaxbins = xmajormaxbins
        self.ax.xaxis.set_major_locator(
            MaxNLocator(nbins=self.xmajormaxbins, integer=self.xmajorint)
        )
        self.__plot(self.__data, height=self.height, alpha=self.alpha)

    def __plot(self, data, height, alpha):
        self.clear()
        self.graphdata = [self._funne(data, height, alpha)]
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def _funne(self, data: np.ndarray, height=1, alpha=1):
        data_max = data.max()
        self.ax.set_xlim([0, data_max])
        lists1 = np.delete(np.linspace(0, data_max, 6, dtype=np.int_), 0)
        self.ax.set_xticks(np.linspace(0, data_max, 11, dtype=np.float64))
        self.ax.set_xticklabels(np.append(np.append(lists1[::-1], [0]), lists1))
        bars = self.ax.barh(
            np.arange(len(data)),
            data,
            left=(data_max - data) / 2,
            height=height,
            alpha=alpha,
        )
        for i in bars:
            i.set_alpha(alpha)
        return bars

    def update(self, data=None, **kw):
        self._updates(**kw)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data, depth_limit=1)
        self.height = range_num(num0s(kw.get("height"), self.height), 0, 1, self.height)
        xmajormaxbins = intsmin(kw.get("xmajormaxbins"), 3, self.xmajormaxbins)
        if not isinstance(xmajormaxbins, int):
            raise TypeError("xmajormaxbinsに整数を指定してください")
        elif xmajormaxbins % 2 == 0:
            raise ValueError("xmajormaxbinsは2n+1の整数で指定してください")
        else:
            self.xmajormaxbins = xmajormaxbins
        self.ax.xaxis.set_major_locator(
            MaxNLocator(nbins=self.xmajormaxbins, integer=self.xmajorint)
        )
        self.__plot(self.__data, height=self.height)
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
