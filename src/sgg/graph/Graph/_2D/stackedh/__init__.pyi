from matplotlib.container import BarContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Stackedh"]

class Stackedh(_2Gset):
    def update(
        self,
        data: TypeArraysLikeNumber,
        dataname: TypeArrayLikeNS,
        height: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
        label: str | list[str] | None,
    ) -> None:
        """積み上げ横向き棒グラフを再表示させる"""

    def get(self) -> list[BarContainer]:
        """`matplotlib.container.BarContainer`の配列を返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
