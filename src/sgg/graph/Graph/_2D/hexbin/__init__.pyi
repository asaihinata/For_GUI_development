from matplotlib.collections import PolyCollection

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Hexbin"]

class Hexbin(_2Gset):
    def update(
        self,
        x: TypeArraysLikeNumber,
        y: TypeArraysLikeNumber,
        c: TypeArraysLikeNumber | None,
        gridsize: int | tuple[int, int],
        extent: tuple[int | float, int | float, int | float, int | float] | None,
        xscale: Literal["linear", "log"],
        yscale: Literal["linear", "log"],
        mincnt: int,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        decimalpoint: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """2次元六角形ビニンググラフを再表示させる"""

    def get(self) -> list[PolyCollection]:
        """`matplotlib.collections.PolyCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
