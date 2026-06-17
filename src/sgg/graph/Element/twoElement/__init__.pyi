from collections.abc import Iterable

from matplotlib.axes._axes import Axes
from matplotlib.axis import Tick
from numpy import ndarray

from ...style import getLabel
from ...typing import *
from ..graph import GElement

__all__ = ["twoElement"]

class twoElement(GElement):
    label: getLabel
    ax: Axes
    xlabel: str
    ylabel: str
    def _updates(
        self,
        fg: ColorType,
        bg: ColorType,
        graph_grid: ColorType,
        title: str,
        alpha: int | float,
        xlabel: labeltype,
        ylabel: labeltype,
    ) -> None: ...
    def _apply_labels(self, xlabel: labeltype = None, ylabel: labeltype = None) -> None:
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

    def getticks(self) -> tuple[ndarray, ndarray]:
        """x軸,y軸の目盛りの位置を座標で返します"""

    def getxticks(self) -> ndarray:
        """x軸の目盛りの位置を座標で返します"""

    def getyticks(self) -> ndarray:
        """y軸の目盛りの位置を座標で返す"""

    @overload
    def set_xticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = ...
    ) -> list[Tick]:
        """
        x軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: x軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: x軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: x軸の主目盛りを設定するか補助目盛りのみ設定するか指定する(False)
        :type minor: bool
        """

    @overload
    def set_xticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = True
    ) -> list[Tick]:
        """
        x軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: x軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: x軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: x軸の補助目盛りのみに適用する
        :type minor: bool
        """

    @overload
    def set_xticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = False
    ) -> list[Tick]:
        """
        x軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: x軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: x軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: x軸の主目盛りのみに適用する
        :type minor: bool
        """

    @overload
    def set_yticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = ...
    ) -> list[Tick]:
        """
        y軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: y軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: y軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: y軸の主目盛りを設定するか補助目盛りのみ設定するか指定する(False)
        :type minor: bool
        """

    @overload
    def set_yticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = True
    ) -> list[Tick]:
        """
        y軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: y軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: y軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: y軸の補助目盛りのみに適用する
        :type minor: bool
        """

    @overload
    def set_yticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = False
    ) -> list[Tick]:
        """
        y軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: y軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: y軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: y軸の主目盛りのみに適用する
        :type minor: bool
        """
