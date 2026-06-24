from ...dev import *

__all__ = ["Pie"]


class Pie(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__data = NPNumber(kw.get("data"), depth_limit=1)
        self.startangle = nums(kw.get("startangle"), 0)
        self.startangletype = bols(kw.get("startangletype"))
        self.shadow = bols(kw.get("shadow"), False)
        self.counterclock = bols(kw.get("counterclock"), False)
        self.labeldistance = num0(kw.get("labeldistance"), 1.1)
        explode = kw.get("explode")
        if isinstance(explode, list | tuple) and all(
            isinstance(i, int | float) for i in explode
        ):
            self.explode = list(map(float, explode))
        elif isinstance(explode, int | float):
            self.explode = [float(explode) for _ in range(self.__data.size)]
        else:
            self.explode = None
        self.__plot(
            self.__data,
            startangle=self.startangle,
            shadow=self.shadow,
            counterclock=self.counterclock,
            label=self.label,
            labeldistance=self.labeldistance,
            explode=self.explode,
            startangletype=self.startangletype,
            alpha=self.alpha,
        )

    def __plot(
        self,
        data,
        startangle,
        shadow,
        counterclock,
        label,
        labeldistance,
        explode,
        startangletype,
        alpha,
    ):
        self.clear()
        if startangletype == False:
            startangle = np.rad2deg(startangle)
        self.graphdata = [
            self.ax.pie(
                data,
                labels=None if label else list(label),
                startangle=90 - startangle,
                shadow=shadow,
                counterclock=counterclock,
                labeldistance=labeldistance,
                explode=explode,
                wedgeprops={"alpha": alpha},
            )
        ]
        if not self.label:
            self.ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    def update(self, data=None, **kw):
        self._updates(**kw)
        if change_array_like(data):
            self.__data = NPNumber(data, depth_limit=1)
        explode = kw.get("explode", self.explode)
        if isinstance(explode, list | tuple) and all(
            isinstance(i, int | float) for i in explode
        ):
            self.explode = list(map(float, explode))
        elif isinstance(explode, int | float):
            self.explode = [float(explode) for _ in range(self.__data.size)]
        else:
            self.explode = None
        self.startangle = nums(kw.get("startangle"), self.startangle)
        self.startangletype = bols(kw.get("startangletype"), self.startangletype)
        self.shadow = bols(kw.get("shadow"), self.shadow)
        self.counterclock = bols(kw.get("counterclock"), self.counterclock)
        self.labeldistance = num0(kw.get("labeldistance"), self.labeldistance)
        self.__plot(
            self.__data,
            startangle=self.startangle,
            shadow=self.shadow,
            counterclock=self.counterclock,
            label=self.label,
            labeldistance=self.labeldistance,
            explode=self.explode,
            startangletype=self.startangletype,
            alpha=self.alpha,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getdata(self):
        return self.__data.tonp()
