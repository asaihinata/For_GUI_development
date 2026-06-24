from tkinter import Misc

from matplotlib.projections.polar import PolarAxes
from numpy import ndarray

from ....nparray import NPNumber
from ...style import getLabel
from ...typing import *
from ..graph import GElement

__all__ = ["RadarElement"]

class RadarElement(GElement):
    label: getLabel
    ax: PolarAxes
    theta: ndarray[float64, dtype[float64]]
    frametype: Literal["circle", "polygon"] = "circle"
    def __init__(self, master: Misc, kw: dict) -> None:
        self._data: NPNumber

    def _updates(
        self,
        data: TypeArrayLikeNumber,
        fg: ColorType,
        bg: ColorType,
        graph_grid: ColorType,
        title: str,
        alpha: int | float,
    ) -> None:
        """グラフの値を更新する"""

    def _adjustment(self) -> None:
        """グラフの調整を行う"""

    def clear(self) -> None:
        """グラフ内のグラフをクリアする"""

    def invert(self) -> None:
        """x軸,y軸を反転させる"""

    def invert_x(self) -> None:
        """x軸を反転させる"""

    def invert_y(self) -> None:
        """y軸を反転させる"""

    def getbound(self) -> tuple[tuple[float64, float64], tuple[float64, float64]]:
        """x軸,y軸の下限値と上限値を昇順で返す"""

    def getxbound(self) -> tuple[float64, float64]:
        """x軸の下限値と上限値を昇順で返す"""

    def getybound(self) -> tuple[float64, float64]:
        """y軸の下限値と上限値を昇順で返す"""

    def getticks(self) -> tuple[ndarray, ndarray]:
        """x軸,y軸の目盛りの位置を座標で返します"""

    def getxticks(self) -> ndarray:
        """x軸の目盛りの位置を座標で返します"""

    def getyticks(self) -> ndarray:
        """y軸の目盛りの位置を座標で返します"""
