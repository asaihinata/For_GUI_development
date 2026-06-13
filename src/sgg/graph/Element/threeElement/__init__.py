from matplotlib.pyplot import rcParams
from mpl_toolkits.mplot3d.axes3d import Axes3D

from ....dev import bols, list2num, listchose, num0s, nums, parsecolor, range_num
from ..graph import GElement

__all__ = ["threeElement"]


class threeElement(GElement):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        # グラフの基盤
        self.elev = nums(kw.get("elev"), 30)
        self.azim = nums(kw.get("azim"), 45)
        self.ax: Axes3D = self.fig.add_subplot(111, projection="3d")
        self.title = self.set_title(self.titles)
        # ラベル
        self.xlabel = kw.get("xlabel")
        self.ylabel = kw.get("ylabel")
        self.zlabel = kw.get("zlabel")
        # グリッド線
        self.grid_xyz = bols(kw.get("grid_xyz"))
        self.grid_x = bols(kw.get("grid_x"), False)
        self.grid_y = bols(kw.get("grid_y"), False)
        self.grid_z = bols(kw.get("grid_z"), False)
        # 目盛り
        self.xmajorint = bols(kw.get("xmajorint"))
        self.ymajorint = bols(kw.get("ymajorint"))
        self.zmajorint = bols(kw.get("zmajorint"))
        self.xticksshow = bols(kw.get("xticksshow"), False)
        self.yticksshow = bols(kw.get("yticksshow"), False)
        self.zticksshow = bols(kw.get("zticksshow"), False)
        self.xticksdirection = listchose(
            kw.get("xticksdirection"), ["out", "in", "inout"]
        )
        self.yticksdirection = listchose(
            kw.get("yticksdirection"), ["out", "in", "inout"]
        )
        xticksrange = kw.get("xticksrange", 0)
        yticksrange = kw.get("yticksrange", 0)
        zticksrange = kw.get("zticksrange", 0)
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
        if isinstance(zticksrange, int | float):
            zticksrange = abs(zticksrange)
            negnum = zticksrange * -1
            self.zticksrange = (negnum, zticksrange)
        elif list2num(zticksrange):
            self.zticksrange = zticksrange
        else:
            self.zticksrange = (0, 0)
        # その他
        if bols(kw.get("mouse_rotation")):
            self.ax.disable_mouse_rotation()
        self.ax.view_init(self.elev, self.azim)
        self._apply_theme_colors()

    def _updates(self, **kw):
        self.fg = parsecolor(kw.get("fg"), self.fg)
        self.graph_bg = parsecolor(kw.get("bg"), self.graph_bg)
        self.graph_grid = parsecolor(kw.get("graph_grid"), self.graph_grid)
        self.title = self.set_title(kw.get("title", self.titles))
        self.elev = nums(kw.get("elev"), self.elev)
        self.azim = nums(kw.get("azim"), self.azim)
        self.xlabel = kw.get("xlabel", self.xlabel)
        self.ylabel = kw.get("ylabel", self.ylabel)
        self.zlabel = kw.get("zlabel", self.zlabel)
        self.alpha = range_num(num0s(kw.get("alpha"), self.alpha), 0, 1, self.alpha)

    def _apply_theme_colors(self):
        self.ax.set_facecolor(self.graph_bg)
        self.ax.tick_params(colors=self.fg)
        self.set_title(self.titles)
        self.ax.xaxis.label.set_color(self.fg)
        self.ax.yaxis.label.set_color(self.fg)
        self.ax.zaxis.label.set_color(self.fg)
        self._apply_grid()

    def _apply_grid(self):
        if self.grid_xyz:
            self.ax.grid(True, color=self.graph_grid, linestyle="--", alpha=0.6)
        else:
            if self.grid_x:
                self.ax.xaxis.grid(
                    True, color=self.graph_grid, linestyle="--", alpha=0.6
                )
            if self.grid_y:
                self.ax.yaxis.grid(
                    True, color=self.graph_grid, linestyle="--", alpha=0.6
                )
            if self.grid_z:
                self.ax.zaxis.grid(
                    True, color=self.graph_grid, linestyle="--", alpha=0.6
                )

    def _apply_labels(self, xlabel=None, ylabel=None, zlabel=None):
        if xlabel is not None:
            self.ax.set_xlabel(xlabel)
        if ylabel is not None:
            self.ax.set_ylabel(ylabel)
        if zlabel is not None:
            self.ax.set_zlabel(zlabel)
        self._apply_grid()

    def _adjustment(self):
        xlimmins, xlimmaxs = self.xticksrange
        xlimmin, xlimmax = self.ax.get_xlim()
        ylimmins, ylimmaxs = self.yticksrange
        ylimmin, ylimmax = self.ax.get_ylim()
        zlimmins, zlimmaxs = self.zticksrange
        zlimmin, zlimmax = self.ax.get_zlim()
        self.ax.set_xlim(xlimmin + xlimmins, xlimmax + xlimmaxs)
        self.ax.set_ylim(ylimmin + ylimmins, ylimmax + ylimmaxs)
        self.ax.set_zlim(zlimmin + zlimmins, zlimmax + zlimmaxs)
        if self.tight_layout:
            self.fig.tight_layout()

    def clear(self):
        self.graphdata = []
        self.ax.clear()
        self._ticks()
        self._apply_theme_colors()

    def _ticks(self):
        if self.ticksshow:
            self.ax.set_xticks([])
            self.ax.set_yticks([])
            self.ax.set_zticks([])
        else:
            if self.xticksshow:
                self.ax.set_xticks([])
            if self.yticksshow:
                self.ax.set_yticks([])
            if self.zticksshow:
                self.ax.set_zticks([])
        rcParams["xtick.direction"] = self.xticksdirection
        rcParams["ytick.direction"] = self.yticksdirection

    def invert(self):
        self.ax.invert_xaxis()
        self.ax.invert_yaxis()
        self.ax.invert_zaxis()

    def invert_x(self):
        self.ax.invert_xaxis()

    def invert_y(self):
        self.ax.invert_yaxis()

    def invert_z(self):
        self.ax.invert_zaxis()

    def getbound(self):
        return (self.ax.get_xbound(), self.ax.get_ybound(), self.ax.get_zbound())

    def getxbound(self):
        return self.ax.get_xbound()

    def getybound(self):
        return self.ax.get_ybound()

    def getzbound(self):
        return self.ax.get_zbound()

    def getticks(self):
        return (self.ax.get_xticks(), self.ax.get_yticks(), self.ax.get_zticks())

    def getxticks(self):
        return self.ax.get_xticks()

    def getyticks(self):
        return self.ax.get_yticks()

    def getzticks(self):
        return self.ax.get_zticks()

    def set_xticks(self, ticks, labels=None, minor=False):
        return self.ax.set_xticks(ticks, labels=labels, minor=minor)

    def set_yticks(self, ticks, labels=None, minor=False):
        return self.ax.set_yticks(ticks, labels=labels, minor=minor)

    def set_zticks(self, ticks, labels=None, minor=False):
        return self.ax.set_zticks(ticks, labels=labels, minor=minor)
