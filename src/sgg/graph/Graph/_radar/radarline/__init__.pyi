from matplotlib.lines import Line2D

from sgg.graph.graph.dev import *
from sgg._typing import (ColorType, GetList, Type_Marker, Type_Solid,
                        TypeArrayLikeNumber)

__all__ = ["RadarLine"]

class RadarLine(RadarElement):
    def update(
        self,
        data: TypeArrayLikeNumber,
        markersize: int | float,
        marker: Type_Marker,
        line: Type_Solid,
        linewidth: int | float,
        alpha: int | float,
        fg: ColorType,
        bg: ColorType,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """折線レーダーチャートを再表示させる"""

    def get(self) -> list[Line2D]:
        """`matplotlib.lines.Line2D`の配列を返す"""

    def getdata(self) -> GetList:
        """`data`のデータを取得する"""
