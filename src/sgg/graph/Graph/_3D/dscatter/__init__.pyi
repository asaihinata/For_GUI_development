from matplotlib.collections import PathCollection

from ....typing import *
from .._3gset import _3Gset

__all__ = ["DScatter"]

class DScatter(_3Gset):
    def update(
        self,
        x: o_array,
        y: o_array,
        z: o_array,
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
        """3D散布図を再表示させる"""

    def get(self) -> list[PathCollection]:
        """`PathCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""

    def getz(self) -> Typeget_data:
        """`z`のデータを取得する"""

    def getcoordinate(
        self,
    ) -> ndarray[NDArray[float64], NDArray[float64], NDArray[float64]]:
        """3D散布図の点の座標を取得する"""
