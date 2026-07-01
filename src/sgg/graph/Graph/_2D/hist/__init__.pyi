from matplotlib.container import BarContainer
from matplotlib.patches import Polygon

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Hist"]

class Hist(_2Gset):
    def update(
        self,
        data: TypeArrayLikeNumber,
        bins: (
            int
            | list
            | range
            | tuple
            | np.ndarray
            | Literal[
                "auto", "fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"
            ]
        ),
        min: int | float,
        max: int | float,
        bottom: int | float,
        orientation: Literal["horizontal", "vertical"],
        width: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """ヒストグラムを再表示させる"""

    def get(
        self,
    ) -> list[
        np.ndarray | list[np.ndarray],
        np.ndarray,
        BarContainer | Polygon | list[BarContainer | Polygon],
    ]:
        """matplotlib.axes.Axes.hist`の戻り値を配列で返す"""

    def getdata(self) -> Typeget_Array_Number:
        """`data`のデータを取得する"""
