from matplotlib.container import BarContainer

from sgg.graph.typing import *

from .._2gset import _2Gset

__all__ = ["Funne"]

class Funne(_2Gset):
    def update(
        self,
        x: TypeArrayLikeNumber,
        height: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        aylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """じょうごグラフを再表示させる"""

    def get(self) -> list[BarContainer]:
        """`matplotlib.container.BarContainer`の配列を返す"""

    def getdata(self) -> Typeget_Array_Number:
        """`data`のデータを取得する"""
