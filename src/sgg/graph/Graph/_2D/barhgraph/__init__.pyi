from matplotlib.container import BarContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["BarhGraph"]

class BarhGraph(_2Gset):
    def update(
        self,
        x: o_array,
        y: n_array,
        height: int | float,
        align: Literal["center", "edge"],
        logs: bool,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """横軸棒グラフを再表示させる"""

    def get(self) -> list[BarContainer]:
        """`BarContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
