from ...dev import *

__all__ = ["Eventpolar"]


class Eventpolar(polarElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"))
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.linewidth = num0(kw.get("linewidth"), 1)
        self.linelength = num0(kw.get("linelength"), 1)
        self.linestyle = Solid(kw.get("linestyle", "-"))
        self.__plot(
            self.__data,
            orientation=self.orientation,
            linewidth=self.linewidth,
            linelength=self.linelength,
            alpha=self.alpha,
            linestyle=self.linestyle,
        )

    def __plot(
        self,
        data,
        orientation,
        linewidth,
        linelength,
        alpha,
        linestyle,
    ):
        self.clear()
        self.graphdata = [
            self.ax.eventplot(
                ds,
                lineoffsets=self._places(data.ndim + 1)[i],
                alpha=alpha,
                linelengths=linelength,
                linewidths=linewidth,
                orientation=orientation,
                linestyles=linestyle.solid,
            )
            for i, ds in enumerate(data)
        ]
        self._adjustment()

    def update(self, data=None, **kw):
        self._updates(**kw)
        if isinstance(data, nListlike):
            self.__data = NPNumber(data)
        self.orientation = listchose(
            kw.get("orientation"), ["vertical", "horizontal"], self.orientation
        )
        self.linewidth = num0(kw.get("linewidth"), self.linewidth)
        self.linelength = num0(kw.get("linelength"), self.linelength)
        self.linestyle = Solid(kw.get("linestyle", self.linestyle))
        self.__plot(
            self.__data,
            orientation=self.orientation,
            linewidth=self.linewidth,
            linelength=self.linelength,
            alpha=self.alpha,
            linestyle=self.linestyle,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
