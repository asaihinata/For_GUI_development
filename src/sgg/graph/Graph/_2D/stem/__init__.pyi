from typing import Literal

from matplotlib.container import StemContainer

from sgg._typing import *

from .._2gset import _2Gset

__all__ = ["Stem"]

class Stem(_2Gset):
    def update(
        self,
        x: TypeArraysLikeNumber,
        y: TypeArraysLikeNumber,
        linefmt: str | None,
        markerfmt: str | None,
        basefmt: str | None,
        bottom: int | float,
        orientation: Literal["horizontal", "vertical"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
        label: str | list[str] | None,
    ) -> None:
        """幹図を再表示させる"""

    def get(self) -> list[StemContainer]:
        """`matplotlib.container.StemContainer`の配列を返す"""

    def getx(self) -> GetList:
        """`x`のデータを取得する"""

    def gety(self) -> GetList:
        """`y`のデータを取得する"""
