from matplotlib.container import ErrorbarContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Errorbar"]

class Errorbar(_2Gset):
    def update(
        self,
        x: TypeArraysLikeNumber,
        y: TypeArraysLikeNumber,
        err: TypeArrayLikeNumber,
        xerr: TypeArrayLikeNumber,
        yerr: TypeArrayLikeNumber,
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

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
