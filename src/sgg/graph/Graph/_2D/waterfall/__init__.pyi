from matplotlib.container import BarContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Waterfall"]

class Waterfall(_2Gset):
    def update(
        self,
        x: o_array,
        y: o_array,
        colorline: ColorType,
        linestyle: Literal[
            "solid",
            "-",
            "dashed",
            "--",
            "dash-dot",
            "-.",
            "dotted",
            ":",
            "none",
            None,
            " ",
            "",
        ],
        ucolor: ColorType,
        dcolor: ColorType,
        width: int | float,
        align: Literal["center", "edge"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """滝グラフを再表示させる"""

    def get(self) -> list[BarContainer]:
        """`BarContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
