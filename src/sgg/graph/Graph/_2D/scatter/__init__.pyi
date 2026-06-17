from matplotlib.collections import PathCollection

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Scatter"]

class Scatter(_2Gset):
    def update(
        self,
        x: n_array,
        y: n_array,
        marker: Type_Marker,
        markersize: int | float,
        regression_bool: bool,
        linestyle: Type_Solid,
        linewidth: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """散布図を再表示させる"""

    def get(self) -> list[PathCollection]:
        """`PathCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""

    def getcoordinate(self) -> ndarray[NDArray[float64], NDArray[float64]]:
        """散布図の点の座標を取得する"""
