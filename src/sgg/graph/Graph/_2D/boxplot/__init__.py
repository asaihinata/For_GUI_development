from ...dev import *

__all__ = ["Boxplot"]


class Boxplot(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        self.legends = bols(kw.get("legend"), False)
        if self.label:
            self.label = getLabel([f"box{i}" for i in range(self.__data.ndim)])
        else:
            self.label = self.label.loop(self.__data.ndim)
        self.width = range_num(num0s(kw.get("width"), 0.15), 0, 1, 0.15)
        self.whis = self._boxplot_whis(kw.get("whis"))
        self.fill = bols(kw.get("fill"), False)
        self.notch = bols(kw.get("notch"), False)
        self.showfliers = bols(kw.get("showfliers"))
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.__plot(
            self.__data,
            label=self.label,
            width=self.width,
            legend=self.legends,
            whis=self.whis,
            fill=self.fill,
            showfliers=self.showfliers,
            notch=self.notch,
            orientation=self.orientation,
            alpha=self.alpha,
        )

    def __plot(
        self,
        data,
        label,
        width,
        whis,
        fill,
        legend,
        showfliers,
        notch,
        orientation,
        alpha,
    ):
        self.clear()
        boxplot = self.ax.boxplot(
            data,
            showfliers=showfliers,
            label=list(label),
            widths=width,
            whis=whis,
            patch_artist=fill,
            notch=notch,
            orientation=orientation,
        )
        for i in range(data.ndim):
            boxplot["boxes"][i].set_alpha(alpha)
        if orientation == "vertical":
            self.ax.set_xticklabels(label)
        else:
            self.ax.set_yticklabels(label)
        self.graphdata = [boxplot]
        self._apply_labels(self.xlabel, self.ylabel)
        if legend:
            self.legend()
        self._adjustment()

    def update(self, data=None, **kw):
        self._updates(**kw)
        if change_array_like(data):
            self.__data = NPNumber(data)
        self.legends = bols(kw.get("legend"), self.legends)
        self.fill = bols(kw.get("fill"), self.fill)
        self.notch = bols(kw.get("notch"), self.notch)
        self.showfliers = bols(kw.get("showfliers"), self.showfliers)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        self.width = range_num(num0s(kw.get("width"), self.width), 0, 1, self.width)
        self.whis = self._boxplot_whis(kw.get("whis", self.whis))
        self.__plot(
            self.__data,
            label=self.label,
            width=self.width,
            legend=self.legends,
            whis=self.whis,
            fill=self.fill,
            showfliers=self.showfliers,
            notch=self.notch,
            orientation=self.orientation,
            alpha=self.alpha,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()

    def _boxplot_whis(self, data):
        if isinstance(data, list | tuple):
            if all(isinstance(i, int | float) for i in data):
                x, y = data[0], data[1]
                if y < x:
                    x, y = y, x
                if not 0 <= x <= 100:
                    x = 0
                if not 0 <= y <= 100:
                    y = 100
                return (float(x), float(y))
        elif isinstance(data, int | float):
            return float(data)
        return 1.5
