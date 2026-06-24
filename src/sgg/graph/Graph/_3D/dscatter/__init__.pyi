from matplotlib.collections import PathCollection
from numpy.typing import NDArray

from ....typing import *
from .._3gset import _3Gset

__all__ = ["DScatter"]

class DScatter(_3Gset):
    def update(
        self,
        x: TypeArraysLikeNS,
        y: TypeArraysLikeNS,
        z: TypeArraysLikeNS,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
        marker: Type_Marker,
        markersize: int | float,
        linewidth: int | float,
        elev: int | float,
        azim: int | float,
        xlabel: str,
        ylabel: str,
        zlabel: str,
    ) -> None:
        """立体散布図を再表示させる"""

    def get(self) -> list[PathCollection]:
        """`matplotlib.collections.PathCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""

    def getz(self) -> Typeget_data:
        """`z`のデータを取得する"""

    def getcoordinate(
        self,
    ) -> ndarray[NDArray[float64], NDArray[float64], NDArray[float64]]:
        """立体散布図の点の座標を取得する"""
