from matplotlib.container import StemContainer

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Stempolar"]

class Stempolar(_polarset):
    @overload
    def update(
        self,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNS,
        linefmt: str | None,
        markerfmt: str | None,
        basefmt: str | None,
        bottom: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸幹図を再表示させる"""

    @overload
    def update(
        self,
        data: TypeArrayLikeNS,
        linefmt: str | None,
        markerfmt: str | None,
        basefmt: str | None,
        bottom: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸幹図を再表示させる"""

    def get(self) -> list[StemContainer]:
        """`matplotlib.container.StemContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
