from matplotlib.lines import Line2D

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Ecdf"]

class Ecdf(_2Gset):
    def update(
        complementary: bool,
        compress: bool,
        orientation: Literal["horizontal", "vertical"],
        linestyle: Type_Solid,
        linewidth: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        aylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """経験的累積分布関数を再描画させる"""

    def get(self) -> list[Line2D]:
        """`Line2D`の配列を返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
