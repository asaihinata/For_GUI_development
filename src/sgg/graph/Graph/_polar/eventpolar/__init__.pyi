from matplotlib.collections import EventCollection

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Eventpolar"]

class Eventpolar(_polarset):
    def update(
        self,
        data: o_array,
        orientation: Literal["vertical", "horizontal"],
        linewidth: int | float,
        linelength: int | float,
        linestyle: Type_Solid,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸イベントグラフを再表示させる"""

    def get(self) -> list[EventCollection]:
        """`EventCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
