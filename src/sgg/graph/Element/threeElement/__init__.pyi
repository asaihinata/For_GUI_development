from collections.abc import Iterable

from matplotlib.axis import Tick
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import ndarray

from ...style import getLabel
from ...typing import *
from ..graph import GElement

__all__ = ["threeElement"]

class threeElement(GElement):
    label: getLabel
    ax: Axes3D
    xlabel: str
    ylabel: str
    zlabel: str
    def _updates(
        self,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
        elev: int | float,
        azim: int | float,
        xlabel: labeltype,
        ylabel: labeltype,
        zlabel: labeltype,
    ) -> None: ...
    def _apply_labels(
        self,
        xlabel: labeltype = None,
        ylabel: labeltype = None,
        zlabel: labeltype = None,
    ) -> None:
        """
        3Dのグラフのx軸,y軸,z軸のラベルを作成する

        :param xlabel: x軸のラベルを指定する
        :type label: labeltype
        :param ylabel: y軸のラベルを指定する
        :type ylabel: labeltype
        :param zlabel: z軸のラベルを指定する
        :type zlabel: labeltype
        """

    def _apply_grid(self) -> None:
        """グリッド線を加えるメソッド"""

    def _adjustment(self) -> None:
        """グラフの調整を行う"""

    def clear(self) -> None:
        """グラフ内のグラフをクリアする"""

    def invert(self) -> None:
        """x軸,y軸,z軸を反転させる"""

    def invert_x(self) -> None:
        """x軸を反転させる"""

    def invert_y(self) -> None:
        """y軸を反転させる"""

    def invert_z(self) -> None:
        """z軸を反転させる"""

    def getbound(
        self,
    ) -> tuple[
        tuple[float64, float64], tuple[float64, float64], tuple[float64, float64]
    ]:
        """x軸,y軸,z軸の下限値と上限値を昇順で返す"""

    def getxbound(self) -> tuple[float64, float64]:
        """x軸の下限値と上限値を昇順で返す"""

    def getybound(self) -> tuple[float64, float64]:
        """y軸の下限値と上限値を昇順で返す"""

    def getzbound(self) -> tuple[float64, float64]:
        """z軸の下限値と上限値を昇順で返す"""

    def getticks(self) -> tuple[ndarray, ndarray, ndarray]:
        """x軸,y軸,z軸の目盛りの位置を座標で返します"""

    def getxticks(self) -> ndarray:
        """x軸の目盛りの位置を座標で返します"""

    def getyticks(self) -> ndarray:
        """y軸の目盛りの位置を座標で返します"""

    def getzticks(self) -> ndarray:
        """z軸の目盛りの位置を座標で返します"""

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

    @overload
    def set_zticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = ...
    ) -> list[Tick]:
        """
        z軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: z軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: z軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: z軸の主目盛りを設定するか補助目盛りのみ設定するか指定する(False)
        :type minor: bool
        """

    @overload
    def set_zticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = True
    ) -> list[Tick]:
        """
        z軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: z軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: z軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: z軸の補助目盛りのみに適用する
        :type minor: bool
        """

    @overload
    def set_zticks(
        self, ticks: ArrayLike, labels: Iterable[str] | None = None, minor: bool = False
    ) -> list[Tick]:
        """
        z軸の目盛りの位置と目盛りのラベルを設定する

        :param ticks: z軸の目盛りの位置を指定する
        :type ticks: ArrayLike
        :param labels: z軸の目盛りのラベルを指定する
        :type labels: Iterable[str]|None
        :param minor: z軸の主目盛りのみに適用する
        :type minor: bool
        """
