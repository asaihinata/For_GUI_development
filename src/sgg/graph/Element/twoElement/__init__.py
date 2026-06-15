from matplotlib.axes._axes import Axes
from matplotlib.pyplot import rcParams

from ....dev import bols, list2num, listchose, num0s, parsecolor, range_num
from ...style import getLabel
from ..graph import GElement

__all__ = ["twoElement"]


class twoElement(GElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        # ラベル
        self.xlabel = kw.get("xlabel")
        self.ylabel = kw.get("ylabel")
        # グリッド線
        self.grid_xy = bols(kw.get("grid_xy"))
        self.grid_x = bols(kw.get("grid_x"), False)
        self.grid_y = bols(kw.get("grid_y"), False)
        # グラフの基盤
        self.ax: Axes = self.fig.add_subplot(111)
        self.title = self.set_title(self.titles)
        # 目盛り
        self.xmajorint = bols(kw.get("xmajorint"))
        self.ymajorint = bols(kw.get("ymajorint"))
        self.xticksshow = bols(kw.get("xticksshow"), False)
        self.yticksshow = bols(kw.get("yticksshow"), False)
        self.xticksdirection = listchose(
            kw.get("xticksdirection"), ["out", "in", "inout"]
        )
        self.yticksdirection = listchose(
            kw.get("yticksdirection"), ["out", "in", "inout"]
        )
        xticksrange = kw.get("xticksrange", 0)
        yticksrange = kw.get("yticksrange", 0)
        if isinstance(xticksrange, int | float):
            xticksrange = abs(xticksrange)
            self.xticksrange = (xticksrange * -1, xticksrange)
        elif list2num(xticksrange):
            self.xticksrange = xticksrange
        else:
            self.xticksrange = (0, 0)
        if isinstance(yticksrange, int | float):
            yticksrange = abs(yticksrange)
            self.yticksrange = (yticksrange * -1, yticksrange)
        elif list2num(yticksrange):
            self.yticksrange = yticksrange
        else:
            self.yticksrange = (0, 0)

    def _apply_theme_colors(self):
        self.ax.set_facecolor(self.graph_bg)
        self.ax.tick_params(colors=self.fg)
        self.set_title(self.titles)
        self.ax.xaxis.label.set_color(self.fg)
        self.ax.yaxis.label.set_color(self.fg)
        if self.grid_xy:
            self.ax.grid(
                True, color=self.graph_grid, linestyle="--", alpha=0.6, which="both"
            )
        else:
            self.ax.grid(False)
            if self.grid_x:
                self.ax.xaxis.grid(
                    True, color=self.graph_grid, linestyle="--", alpha=0.6
                )
            if self.grid_y:
                self.ax.yaxis.grid(
                    True, color=self.graph_grid, linestyle="--", alpha=0.6
                )

    def _apply_labels(self, xlabel=None, ylabel=None):
        if xlabel is not None:
            self.ax.set_xlabel(xlabel)
        if ylabel is not None:
            self.ax.set_ylabel(ylabel)

    def _updates(self, **kw):
        label = kw.get("label", None)
        self.label = self.label if label == None else getLabel(label)
        self.fg = parsecolor(kw.get("fg"), self.fg)
        self.graph_bg = parsecolor(kw.get("bg"), self.graph_bg)
        self.graph_grid = parsecolor(kw.get("graph_grid"), self.graph_grid)
        self.title = kw.get("title", self.titles)
        self.xlabel = kw.get("xlabel", self.xlabel)
        self.ylabel = kw.get("ylabel", self.ylabel)
        self.alpha = range_num(num0s(kw.get("alpha"), self.alpha), 0, 1, self.alpha)

    def _ticks(self):
        if self.ticksshow:
            self.ax.set_xticks([])
            self.ax.set_yticks([])
        else:
            if self.xticksshow:
                self.ax.set_xticks([])
            if self.yticksshow:
                self.ax.set_yticks([])
        rcParams["xtick.direction"] = self.xticksdirection
        rcParams["ytick.direction"] = self.yticksdirection

    def _adjustment(self):
        xlimmins, xlimmaxs = self.xticksrange
        xlimmin, xlimmax = self.ax.get_xlim()
        ylimmins, ylimmaxs = self.yticksrange
        ylimmin, ylimmax = self.ax.get_ylim()
        self.ax.set_xlim(xlimmin + xlimmins, xlimmax + xlimmaxs)
        self.ax.set_ylim(ylimmin + ylimmins, ylimmax + ylimmaxs)
        if self.tight_layout:
            self.fig.tight_layout()

    def clear(self):
        self.graphdata = []
        self.ax.clear()
        self._ticks()
        self._apply_theme_colors()

    def invert(self):
        self.invert_y()
        self.invert_x()

    def invert_x(self):
        self.ax.invert_xaxis()

    def invert_y(self):
        self.ax.invert_yaxis()

    def getbound(self):
        return (self.ax.get_xbound(), self.ax.get_ybound())

    def getxbound(self):
        return self.ax.get_xbound()

    def getybound(self):
        return self.ax.get_ybound()

    def getticks(self):
        return (self.ax.get_xticks(), self.ax.get_yticks())

    def getxticks(self):
        return self.ax.get_xticks()

    def getyticks(self):
        return self.ax.get_yticks()

    def set_xticks(self, ticks, labels=None, minor=False):
        return self.ax.set_xticks(ticks, labels=labels, minor=minor)

    def set_yticks(self, ticks, labels=None, minor=False):
        return self.ax.set_yticks(ticks, labels=labels, minor=minor)
