from matplotlib.container import PieContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Pie"]

class Pie(_2Gset):
    def update(
        self,
        data: o_array,
        labeldistance: int | float,
        startangletype: bool,
        explode: tuple[int, float] | int | float,
        startangle: int | float,
        shadow: bool,
        counterclock: bool,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """円グラフを再表示させる"""

    def get(self) -> list[PieContainer]:
        """`matplotlib.container.PieContainer`の配列で返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
