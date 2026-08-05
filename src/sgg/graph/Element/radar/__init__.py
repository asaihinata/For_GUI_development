import numpy as np

from sgg.dev import bols, num0s, parsecolor, range_num, tonparray
from sgg.graph.element.graph import GElement

from .custom import radar_factory

__all__ = ["RadarElement"]


class RadarElement(GElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self._data = tonparray(kw.get("data"))
        self.theta = radar_factory(self._data.shape[-1], frame="circle")
        # グリッド線
        self.grid_xy = bols(kw.get("grid_xy"))
        self.grid_x = bols(kw.get("grid_x"), False)
        self.grid_y = bols(kw.get("grid_y"), False)
        # グラフの基盤
        self.ax = self.fig.add_subplot(111, projection="radar")
        self.title = self.set_title(self.titles)
        # 目盛り
        self.xticksshow = bols(kw.get("xticksshow"), False)
        self.yticksshow = bols(kw.get("yticksshow"), False)

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

    def _apply_labels(self, xlabel, ylabel):
        if xlabel is not None:
            self.ax.set_xlabel(xlabel)
        if ylabel is not None:
            self.ax.set_ylabel(ylabel)

    def _updates(self, **kw):
        self._data = tonparray(kw.get("data"))
        self.theta = radar_factory(self._data.shape[-1], frame="circle")
        self.fg = parsecolor(kw.get("fg"), self.fg)
        self.graph_bg = parsecolor(kw.get("bg"), self.graph_bg)
        self.graph_grid = parsecolor(kw.get("graph_grid"), self.graph_grid)
        self.title = kw.get("title", self.titles)
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

    def _adjustment(self):
        self.ax.set_thetagrids(np.degrees(self.theta))
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
