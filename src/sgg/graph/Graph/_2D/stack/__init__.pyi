from matplotlib.collections import FillBetweenPolyCollection

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Stack"]

class Stack(_2Gset):
    def update(
        self,
        x: n_array,
        y: n_array,
        hatch: str,
        baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """積み上げエリアチャートを再表示させる"""

    def get(self) -> list[FillBetweenPolyCollection]:
        """`FillBetweenPolyCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
