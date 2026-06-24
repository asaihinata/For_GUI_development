from matplotlib.container import ErrorbarContainer

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Errorpolar"]

class Errorpolar(_polarset):
    @overload
    def update(
        self,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNS,
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
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸エラーグラフを再表示させる"""

    @overload
    def update(
        self,
        data: TypeArrayLikeNS,
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
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸エラーグラフを再表示させる"""

    def get(self) -> list[ErrorbarContainer]:
        """`matplotlib.container.ErrorbarContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
