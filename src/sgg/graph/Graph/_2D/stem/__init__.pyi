from matplotlib.container import StemContainer

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Stem"]

class Stem(_2Gset):
    def update(
        self,
        x: n_array,
        y: n_array,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
        bottom: int | float,
        orientation: Literal["horizontal", "vertical"],
        marker: Literal[
            "o",
            "+",
            "*",
            ".",
            "x",
            "_",
            "|",
            "square",
            "diamond",
            "^",
            "v",
            "<",
            ">",
            "pentagram",
            "hexagram",
        ] = ...,
        line: Literal["-", "--", "-.", "-."] = ...,
    ) -> None:
        """幹図を再表示させる"""

    def get(self) -> list[StemContainer]:
        """`StemContainer`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
