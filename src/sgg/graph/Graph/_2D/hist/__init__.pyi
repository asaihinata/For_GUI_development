from matplotlib.container import BarContainer
from matplotlib.patches import Polygon

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Hist"]

class Hist(_2Gset):
    def update(
        self,
        data: o_array,
        bins: (
            int
            | list
            | range
            | tuple
            | ndarray
            | Literal[
                "auto", "fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"
            ]
        ),
        min: int | float,
        max: int | float,
        bottom: int | float,
        orientation: Literal["horizontal", "vertical"],
        width: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """ヒストグラムを再表示させる"""

    def get(
        self,
    ) -> list[
        ndarray | list[ndarray],
        ndarray,
        BarContainer | Polygon | list[BarContainer | Polygon],
    ]:
        """matplotlib.axes.Axes.hist`の戻り値を配列で返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
