from matplotlib.collections import FillBetweenPolyCollection
from matplotlib.lines import Line2D

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Linefill"]

class Linefill(_2Gset):
    def update(
        self,
        x: o_array,
        ymin: n_array,
        ymax: n_array,
        centerlinewidth: int | float,
        xlabel: str,
        ylabel: str,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """2つの水平曲線の間の領域を埋めるグラフを再表示させる"""

    def get(self) -> list[FillBetweenPolyCollection, Line2D]:
        """`PathCollection`と`Line2D`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def getymin(self) -> Typeget_data:
        """`ymin`のデータを取得する"""

    def getymax(self) -> Typeget_data:
        """`ymax`のデータを取得する"""
