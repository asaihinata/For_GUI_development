from matplotlib.collections import EventCollection

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Eventplot"]

class Eventplot(_2Gset):
    def update(
        self,
        data: TypeArraysLikeNumber,
        linewidth: int | float,
        linelength: int | float,
        orientation: Literal["vertical", "horizontal"],
        linestyle: Literal[
            "dashdot", "dashed", "dotted", "solid", "-", "--", "-.", ":"
        ],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
        label: str | list[str] | None,
    ) -> None:
        """イベントグラフを再表示させる"""

    def get(self) -> list[EventCollection]:
        """`matplotlib.collections.EventCollection`の配列を返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
