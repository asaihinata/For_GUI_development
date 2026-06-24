from matplotlib.lines import Line2D

from ...dev import *

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

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""

    def get(self) -> list[Line2D]:
        """`matplotlib.lines.Line2D`の配列を返す"""
