from matplotlib.collections import EventCollection

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Eventpolar"]

class Eventpolar(_polarset):
    def update(
        self,
        data: TypeArraysLikeNumber,
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
        """`matplotlib.collections.EventCollection`の配列を返す"""

    def getdata(self) -> Typeget_Array_NumStr:
        """`data`のデータを取得する"""
