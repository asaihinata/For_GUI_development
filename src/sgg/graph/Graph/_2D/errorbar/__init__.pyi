from matplotlib.container import ErrorbarContainer

from sgg.typing import *

from .._2gset import _2Gset

__all__ = ["Errorbar"]

class Errorbar(_2Gset):
    def update(
        self,
        x: TypeArraysLikeNumber,
        y: TypeArraysLikeNumber,
        err: TypeArraysLikeNumber,
        xerr: TypeArraysLikeNumber,
        yerr: TypeArraysLikeNumber,
        xuplims: bool,
        xlolims: bool,
        yuplims: bool,
        ylolims: bool,
        barsabove: bool,
        linewidth: int | float,
        capthick: int | float,
        capsize: int | float,
        errorevery: int | list[int] | tuple[int],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        decimalpoint: int | float,
        graph_grid: ColorType,
        title: str,
        label: str | list[str] | None,
    ) -> None:
        """エラーグラフを再表示させる"""

    def get(self) -> list[ErrorbarContainer]:
        """`matplotlib.container.ErrorbarContainer`の配列を返す"""

    def getx(self) -> GetList:
        """`x`のデータを取得する"""

    def gety(self) -> GetList:
        """`y`のデータを取得する"""
