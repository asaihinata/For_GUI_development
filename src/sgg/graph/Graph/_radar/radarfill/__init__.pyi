from matplotlib.lines import Line2D

from ...dev import *

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

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""

    def get(self) -> list[Line2D]:
        """`matplotlib.lines.Line2D`の配列を返す"""
