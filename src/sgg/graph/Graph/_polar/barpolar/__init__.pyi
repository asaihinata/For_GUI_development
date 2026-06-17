from matplotlib.container import BarContainer

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Barpolar"]

class Barpolar(_polarset):
    @overload
    def update(
        self,
        x: o_array,
        y: o_array,
        logs: bool,
        align: Literal["center", "edge"],
        width: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸棒グラフを再表示させる"""

    @overload
    def update(
        self,
        data: o_array,
        logs: bool,
        align: Literal["center", "edge"],
        width: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸棒グラフを再表示させる"""

    def get(self) -> list[BarContainer]:
        """`BarContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
