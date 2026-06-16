from ...dev import *

__all__ = ["Stem"]
stem_line_list = ["-", "--", "-.", "-."]
stem_mark_list = [
    "o",
    "+",
    "*",
    ".",
    "x",
    "_",
    "|",
    "square",
    "diamond",
    "^",
    "v",
    "<",
    ">",
    "pentagram",
    "hexagram",
]
stem_color_list = ["r", "g", "b", "c", "m", "y", "k", "w"]


class Stem(twoElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__x = NPNumber(kw.get("x"))
        self.__y = NPNumber(kw.get("y"))
        self.colorlist = FMTColorList(kw.get("fcolor"))
        self.line = FMTLineList(kw.get("fline"))
        self.marker = FMTMarkList(kw.get("fmarker"))
        self.bottom = num0s(kw.get("bottom"))
        self.orientation = listchose(kw.get("orientation"), ["vertical", "horizontal"])
        self.__plot(
            self.__x,
            self.__y,
            bottom=self.bottom,
            orientation=self.orientation,
            label=self.label,
            marker=self.marker,
            line=self.line,
            color=self.color,
            alpha=self.alpha,
        )

    def __plot(
        self,
        x,
        y,
        bottom,
        orientation,
        label,
        marker,
        line,
        color,
        alpha,
    ):
        self.clear()
        for i, (xs, ys) in enumerate(TwoArray(x, y)):
            fmt = FMT(marker[i], line[i], color[i]).txt
            stem = self.ax.stem(
                xs,
                ys,
                linefmt=fmt,
                markerfmt=self._markerfmt(marker)[i],
                basefmt=fmt,
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
        if isinstance(x, nListlike):
            self.__x = NPNumber(x)
        if isinstance(y, nListlike):
            self.__y = NPNumber(y)
        color = kw.get("fcolor")
        self.colorlist = parameters(color, self.colorlist, FMTColorList(color))
        line = kw.get("fline")
        self.colorlist = parameters(line, self.line, FMTLineList(line))
        marker = kw.get("fmarker")
        self.marker = parameters(marker, self.marker, FMTMarkList(marker))
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
            marker=self.marker,
            line=self.line,
            color=self.colorlist,
        )
        self._redraw()

    def get(self):
        return self.graphdata

    def getx(self):
        return self.__x.tonp()

    def gety(self):
        return self.__y.tonp()

    def _linefmt(self, line):
        set_arr = []
        if isinstance(line, str):
            set_arr = [listchose(line, stem_line_list)]
        elif isinstance(line, list | tuple):
            set_arr = [i for i in line if i in stem_line_list]
        if len(set_arr) == 0:
            return stem_line_list
        return set_arr

    def _markerfmt(self, marker):
        set_arr = []
        if isinstance(marker, str):
            set_arr = [listchose(marker, stem_mark_list)]
        elif isinstance(marker, list | tuple):
            set_arr = [i for i in marker if i in stem_mark_list]
        if len(set_arr) == 0:
            set_arr = stem_mark_list
        return set_arr

    def _stem_color_check(self, color):
        set_arr, set_color_arr = [], []
        if isinstance(color, list | tuple):
            set_color_arr = [i for i in color if i in stem_color_list]
            if len(set_color_arr) == 0:
                color = stem_color_list
        elif isinstance(color, str):
            color = color
        else:
            color = stem_color_list
        for k, v in {
            "r": ["r", "red"],
            "g": ["g", "green"],
            "b": ["b", "blue"],
            "c": ["c", "cyan"],
            "m": ["m", "magenta"],
            "y": ["y", "yellow"],
            "k": ["k", "black"],
            "w": ["w", "white"],
        }.items():
            if isinstance(color, str) and color in v:
                return [k]
            elif isinstance(color, list | tuple):
                return [k for i in color if i in v]
        return set_arr
