import numpy as np
from matplotlib.collections import PathCollection
from numpy.typing import NDArray

from sgg.typing import *

from .._2gset import _2Gset

__all__ = ["Scatter"]

class Scatter(_2Gset):
    def update(
        self,
        x: TypeArraysLikeNS,
        y: TypeArraysLikeNS,
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
        label: str | list[str] | None,
    ) -> None:
        """散布図を再表示させる"""

    def get(self) -> list[PathCollection]:
        """`matplotlib.collections.PathCollection`の配列を返す"""

    def getx(self) -> GetList:
        """`x`のデータを取得する"""

    def gety(self) -> GetList:
        """`y`のデータを取得する"""

    def getcoordinate(self) -> np.ndarray[NDArray[np.float64], NDArray[np.float64]]:
        """散布図の点の座標を取得する"""
