from matplotlib.lines import Line2D

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Linepolar"]

class Linepolar(_polarset):
    @overload
    def update(
        self,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNS,
        linestyle: Type_Solid,
        marker: Type_Marker,
        linewidth: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸折線グラフを再表示させる"""

    @overload
    def update(
        self,
        data: TypeArrayLikeNS,
        linestyle: Type_Solid,
        marker: Type_Marker,
        linewidth: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸折線グラフを再表示させる"""

    def get(self) -> list[Line2D]:
        """`matplotlib.lines.Line2D`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
