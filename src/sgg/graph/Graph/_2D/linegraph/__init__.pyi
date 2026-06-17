from matplotlib.lines import Line2D

from ....typing import *
from .._2gset import _2Gset

__all__ = ["LineGraph"]

class LineGraph(_2Gset):
    def update(
        self,
        x: n_array,
        y: n_array,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
        marker: Type_Marker,
        markersize: int | float,
        linestyle: Type_Solid,
        linewidth: int | float,
    ) -> None:
        """折線グラフを再表示させる"""

    def get(self) -> list[Line2D]:
        """`Line2D`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
