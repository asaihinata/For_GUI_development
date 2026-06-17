from matplotlib.collections import PathCollection

from ....typing import *
from .._Polarset import _polarset

__all__ = ["Scatterpolar"]

class Scatterpolar(_polarset):
    @overload
    def update(
        self,
        x: o_array,
        y: o_array,
        marker: Type_Marker,
        markersize: int | float,
        linewidth: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸散布図を再表示させる"""

    @overload
    def update(
        self,
        data: o_array,
        marker: Type_Marker,
        markersize: int | float,
        linewidth: int | float,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """極軸散布図を再表示させる"""

    def get(self) -> list[PathCollection]:
        """`PathCollection`の配列を返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""

    def getcoordinate(self) -> ndarray[NDArray[float64], NDArray[float64]]:
        """極軸散布図の点の座標を取得する"""
