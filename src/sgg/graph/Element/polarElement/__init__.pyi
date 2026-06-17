from matplotlib.projections.polar import PolarAxes
import numpy as np

from ....nparray import NPArray, NPNumber
from ...style import getLabel
from ...typing import *
from ..graph import GElement

__all__ = ["polarElement"]

class polarElement(GElement):
    label: getLabel
    ax: PolarAxes
    def _updates(
        self,
        fg: ColorType,
        bg: ColorType,
        graph_grid: ColorType,
        title: str,
        alpha: int | float,
    ) -> None: ...
    def _places(self, num: int) -> ndarray:
        """
        `np.linspace(0,2*np.pi,num,endpoint=False)`と同じ結果同じ結果を求める

        :param num: 要素数を指定する
        :type num: int
        :return: `np.linspace(0,2*np.pi,num,endpoint=False)`と同じ結果同じ結果を求める
        :rtype: ndarray
        """

    @overload
    def _xyd(
        self, x: nListlike, y: nListlike, d: nListlike
    ) -> tuple[NPNumber, NPArray]: ...
    def _apply_labels(self, xlabel: labeltype = None, ylabel: labeltype = None):
        """
        2Dのグラフのx軸,y軸のラベルを作成する

        :param xlabel: x軸のラベルを指定する
        :type label: labeltype
        :param ylabel: y軸のラベルを指定する
        :type ylabel: labeltype
        """

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

    def getticks(self) -> tuple[np.ndarray, np.ndarray]:
        """x軸,y軸の目盛りの位置を座標で返す"""

    def getxticks(self) -> np.ndarray:
        """x軸の目盛りの位置を座標で返す"""

    def getyticks(self) -> np.ndarray:
        """y軸の目盛りの位置を座標で返す"""

    @overload
    def set_thetalim(self, min: np.number, max: np.number, type: bool) -> TupleFloat2:
        """
        特定の角度範囲だけを表示させる

        :param min: 表示される角度の最小を指定する
        :type min: np.number
        :param max: 表示される角度の最大を指定する
        :type max: np.number
        :param type: 制限値を指定する
        :type type: bool
        :return: 表示されている角度の範囲と角度の種類を返す
        :rtype: TupleFloat2
        """

    @overload
    def set_thetalim(
        self, min: np.number, max: np.number, type: bool = True
    ) -> TupleFloat2:
        """
        特定の角度範囲だけを表示させる

        :param min: 表示される角度の最小を指定する
        :type min: np.number
        :param max: 表示される角度の最大を指定する
        :type max: np.number
        :param type: 制限値を度数法で指定する
        :type type: bool
        :return: 表示されている角度の範囲と角度の種類を返す
        :rtype: TupleFloat2
        """

    @overload
    def set_thetalim(
        self, min: np.number, max: np.number, type: bool = False
    ) -> tuple[TupleFloat2, bool]:
        """
        特定の角度範囲だけを表示させる

        :param min: 表示される角度の最小を指定する
        :type min: np.number
        :param max: 表示される角度の最大を指定する
        :type max: np.number
        :param type: 制限値を弧度法で指定する
        :type type: bool
        :return: 表示されている角度の範囲と角度の種類を返す
        :rtype: tuple[TupleFloat2,bool]
        """
