from matplotlib.container import BarContainer

from sgg.typing import *

from .._2gset import _2Gset

__all__ = ["Hatplot"]

class Hatplot(_2Gset):
    def update(
        self,
        x: TypeArrayLikeNumber,
        data: TypeArrayLikeNumber,
        color: ColorType,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        aylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """ハットグラフを再表示させる"""

    def get(self) -> list[BarContainer]:
        """`matplotlib.container.BarContainer`の配列を返す"""

    def getx(self) -> Typeget_Array_Number:
        """`x`のデータを取得する"""

    def getdata(self) -> Typeget_Array_Number:
        """`data`のデータを取得する"""
