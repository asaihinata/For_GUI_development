from matplotlib.lines import Line2D

from sgg.graph.graph.dev import *
from sgg._typing import ColorType, GetList, TypeArrayLikeNumber

__all__ = ["RadarFill"]

class RadarFill(RadarElement):
    def update(
        self,
        data: TypeArrayLikeNumber,
        alpha: int | float,
        fg: ColorType,
        bg: ColorType,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """塗りつぶしレーダーチャートを再表示させる"""

    def get(self) -> list[Line2D]:
        """`matplotlib.lines.Line2D`の配列を返す"""

    def getdata(self) -> GetList:
        """`data`のデータを取得する"""
