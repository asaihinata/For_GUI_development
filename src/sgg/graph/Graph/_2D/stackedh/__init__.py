from matplotlib.ticker import PercentFormatter

from ...dev import *

__all__ = ["Stackedh"]


class Stackedh(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        self.dataname = NPArray(kw.get("dataname"), depth_limit=1)
        if self.__data.shape[0] != self.dataname.shape[0]:
            raise ValueError("配列のエラー")
        self.height = range_num(num0s(kw.get("height"), 0.8), 0, 1, 0.8)
        self.__plot(self.__data, self.dataname, label=self.label, height=self.height)
        self._getlegendplace((1, 0.85), "center left")

    def __plot(self, data, dataname, label, height):
        self.clear()
        self.ax.invert_yaxis()
        self.graphdata = [self._survey(data, dataname, label, height=height)]
        self.legend()
        self.ax.set_xlim(0, 100)
        self.ax.xaxis.set_major_formatter(PercentFormatter(xmax=100))
        self._apply_labels(self.xlabel, self.ylabel)
        self._adjustment()

    def _survey(self, data, dataname, label=None, height=0.8):
        data = data.T
        lisarr = []
        data_percent = data / np.sum(data, axis=0) * 100
        left = np.zeros(len(dataname))
        for i, ds in enumerate(data_percent):
            lisarr = self.ax.barh(
                dataname, ds, left=left, label=label[i], height=height
            )
            left += ds
        return lisarr

    def update(self, data=None, dataname=None, **kw):
        self._updates(**kw)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data)
        if isinstance(dataname, nListlike):
            self.dataname = NPArray(dataname, depth_limit=1)
        if self.__data.shape[0] != self.dataname.shape[0]:
            raise ValueError("配列のエラー")
        self.height = range_num(num0s(kw.get("height"), self.height), 0, 1, self.height)
        self.__plot(self.__data, self.dataname, label=self.label, height=self.height)
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
