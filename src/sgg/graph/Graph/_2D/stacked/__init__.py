from matplotlib.ticker import PercentFormatter

from ...dev import *

__all__ = ["Stacked"]


class Stacked(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        self.dataname = NPArray(kw.get("dataname"), depth_limit=1)
        if self.__data.shape[0] != self.dataname.shape[0]:
            raise ValueError("配列のエラー")
        self.width = range_num(num0s(kw.get("width"), 0.8), 0, 1, 0.8)
        self.__plot(self.__data, self.dataname, label=self.label, width=self.width)
        self._getlegendplace((1.2, 1.2), "center left")

    def __plot(self, data, dataname, label, width):
        self.clear()
        self.graphdata = [self._survey(data, dataname, label=label, width=width)]
        self.ax.set_ylim(0, 100)
        self.ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
        self.legend()
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def _survey(self, data, dataname, label=None, width=0.8):
        data = data.T
        lisarr = []
        data_percent = data / np.sum(data, axis=0) * 100
        bottom = np.zeros(len(dataname))
        for i, ds in enumerate(data_percent):
            lisarr = self.ax.bar(
                dataname, ds, bottom=bottom, label=label[i], width=width
            )
            bottom += ds
        return lisarr

    def update(self, data=None, dataname=None, **kw):
        self._updates(**kw)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data)
        if isinstance(dataname, nListlike):
            self.dataname = NPArray(dataname, depth_limit=1)
        if self.__data.shape[0] != self.dataname.shape[0]:
            raise ValueError("配列のエラー")
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.__plot(self.__data, self.dataname, label=self.label, width=self.width)
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
