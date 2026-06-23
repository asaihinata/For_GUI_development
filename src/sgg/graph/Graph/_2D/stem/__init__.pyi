from matplotlib.container import StemContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Stem"]

class Stem(_2Gset):
    def update(
        self,
        x: n_array,
        y: n_array,
        linefmt: str | None,
        markerfmt: str | None,
        basefmt: str | None,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
        bottom: int | float,
        orientation: Literal["horizontal", "vertical"],
    ) -> None:
        """幹図を再表示させる"""

    def get(self) -> list[StemContainer]:
        """`matplotlib.container.StemContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
