from matplotlib.collections import FillBetweenPolyCollection

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Stack"]

class Stack(_2Gset):
    def update(
        self,
        x: TypeArrayLikeNS,
        y: TypeArraysLikeNumber,
        hatch: str,
        baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
        label: str | list[str] | None,
    ) -> None:
        """積み上げエリアチャートを再表示させる"""

    def get(self) -> list[FillBetweenPolyCollection]:
        """`matplotlib.collections.FillBetweenPolyCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
