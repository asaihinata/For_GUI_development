from re import findall
from tkinter import Misc

from cycler import cycler
from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import rcParams
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np

from ....dev import bols, listchose, num0s, num1s, parsecolor, range_num
from ...style import getLabel

__all__ = ["GElement"]
graph_color = [
    "#4477aa",
    "#ee7733",
    "#111211",
    "#aa66cc",
    "#77aadd",
    "#ffa94d",
    "#55aa55",
    "#cc3311",
    "#cc99ff",
    "#ff8888",
    "#444444",
    "#888888",
    "#332288",
    "#88ccee",
    "#44aa99",
    "#117733",
    "#999933",
    "#ddcc77",
    "#cc6677",
    "#882255",
    "#aa4499",
    "#dddddd",
]
rcParams["font.family"] = "Meiryo"
rcParams["axes.prop_cycle"] = cycler(color=graph_color)


class GElement:
    ax: Axes3D | Axes

    def __init__(self, master: Misc, kw):
        self.master = master
        self.widget = None
        self.graph = True
        self.graphdata = []
        self.widget = None
        self.max_depth = 1
        # グラフの基盤
        self.fg = parsecolor(kw.get("fg"), "#000000")
        self.graph_bg = parsecolor(kw.get("bg"), "#ffffff")
        self.graph_grid = parsecolor(kw.get("graph_grid"), "#b7b7b7")
        color = kw.get("color", graph_color)
        relist = graph_color
        if isinstance(color, str):
            relist = [parsecolor(color, graph_color[0])]
        elif isinstance(color, list | tuple):
            set_arr, judge = [], False
            for i in color:
                c = parsecolor(i)
                if c is not None:
                    judge = True
                    set_arr.append(c)
                if judge:
                    relist = set_arr
        self.color = relist
        rcParams["axes.prop_cycle"] = cycler(color=self.color)
        self.alpha = range_num(num0s(kw.get("alpha"), 1), 0, 1, 1)
        self.dpi = num1s(kw.get("dpi"), 100)
        self.width, self.height = self._size(kw.get("size"))
        # グラフの表示
        self.fig = Figure(
            figsize=(self.width / self.dpi, self.height / self.dpi),
            dpi=self.dpi,
            facecolor=self.graph_bg,
        )
        self.label = getLabel(kw.get("label", None))
        self.titles = kw.get("title")
        # 目盛り
        self.ticksshow = bols(kw.get("ticksshow"), False)
        self.tight_layout = bols(kw.get("tight_layout"))

    def set_title(self, title):
        return self.ax.set_title(title)

    def winsize(self):
        root = self.master
        return root.winfo_width(), root.winfo_height()

    def winwidth(self):
        return self.master.winfo_width()

    def winheight(self):
        return self.master.winfo_height()

    def winxy(self):
        root = self.master
        return root.winfo_x(), root.winfo_y()

    def winx(self):
        return self.master.winfo_x()

    def winy(self):
        return self.master.winfo_y()

    def geometry(self):
        return [float(i) for i in findall(r"\d+", self.master.winfo_geometry())]

    def rootxy(self):
        root = self.master
        return root.winfo_rootx(), root.winfo_rooty()

    def rootx(self):
        return self.master.winfo_rootx()

    def rooty(self):
        return self.master.winfo_rooty()

    def visual(self):
        return self.master.winfo_visual()

    def screen(self):
        return self.master.winfo_screen()

    def reqsize(self):
        root = self.master
        return root.winfo_reqwidth(), root.winfo_reqheight()

    def reqwidth(self):
        return self.master.winfo_reqwidth()

    def reqheight(self):
        return self.master.winfo_reqheight()

    def id(self):
        return self.master.winfo_id()

    def name(self):
        return self.master.winfo_name()

    def _pack(self):
        self.widget = FigureCanvasTkAgg(self.fig, master=self.master)
        self.widget.get_tk_widget().pack(side="left", padx=5, pady=5)

    def _redraw(self):
        if self.widget is not None:
            self.widget.draw()

    def _size(self, sizes=(500, 400)):
        if isinstance(sizes, list | tuple) and len(list(sizes)) == 2:
            if (isinstance(i, int | float) for i in sizes):
                return tuple(sizes)
            else:
                if not isinstance(sizes[0], int | float):
                    sizes[0] = 500
                if not isinstance(sizes[1], int | float):
                    sizes[1] = 400
                return sizes
        else:
            return (500, 400)

    def legend(self):
        if not self.label:
            self.ax.legend()

    def _anchor(self, val, other=None):
        if (
            isinstance(val, list | tuple)
            and (len(val) == 2 or len(val) == 4)
            and all(isinstance(i, int | float) for i in val)
        ):
            return val
        return other

    def _getlegendplace(self, place, other="upper right"):
        labelplacelist = [
            "upper right",
            "upper left",
            "lower left",
            "lower right",
            "right",
            "center left",
            "center right",
            "lower center",
            "upper center",
            "center",
            "best",
        ]
        if isinstance(place, int) and 0 <= place <= 10:
            return labelplacelist[place]
        elif place in labelplacelist:
            return place
        return listchose(other, labelplacelist)

    def _list_loop(self, lin, num):
        if not isinstance(lin, np.ndarray | list | tuple):
            lin = np.array([lin])
        if not isinstance(num, int):
            num = 0
        return np.tile(lin, int(np.ceil(num / len(lin))))[:num]
