"""2つの変数データから様々な統計の計算を行うモジュール"""

from typing import Literal, TypeAlias

import numpy as np
from numpy._typing import _ArrayLikeFloat_co
from numpy.typing import DTypeLike, NDArray

from ....typing import TypeArrayLikeNumber
from ..npnumber import NPNumber
from .npstatisticsd import NPStatisticsd

__all__ = ["NPStatisticsds"]
BINS_LIST: TypeAlias = Literal[
    "stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"
]
METHOD_LIST: TypeAlias = Literal[
    "inverted_cdf",
    "averaged_inverted_cdf",
    "closest_observation",
    "interpolated_inverted_cdf",
    "hazen",
    "weibull",
    "linear",
    "median_unbiased",
    "normal_unbiased",
]

class NPStatisticsds(NPNumber):
    """2つの変数データから様々な統計の計算を行うオブジェクト"""

    def __new__(
        cls,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNumber,
        dtype: DTypeLike | None = np.float64,
    ) -> NPStatisticsds:
        """
        2つの変数データから様々な統計の計算を行うオブジェクト`NPStatisticsds`を返す

        :param x: 数値が入った一次元の配列を指定する
        :type x: TypeArrayLikeNumber
        :param y: 数値が入った一次元の配列を指定する
        :type y: TypeArrayLikeNumber
        :param dtype: `NPStatisticsds`内の配列の型を指定する
        :type dtype: DTypeLike | None
        :return: `NPStatisticsds`オブジェクトを返す
        :rtype: NPStatisticsds
        """

    @property
    def data[T](self: T) -> np.ndarray[T]:
        """`NPStatisticsds`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def tonumpy[T](self: T) -> np.ndarray[T]:
        """`NPStatisticsds`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def x(self) -> NPStatisticsd:
        """`x`データを`NPStatisticsd`オブジェクトで返す"""

    @property
    def xmath(self) -> np.ndarray:
        """`x`データをnumpyの配列で返す"""

    @property
    def y(self) -> NPStatisticsd:
        """`y`データを`NPStatisticsd`オブジェクトで返す"""

    @property
    def ymath(self) -> np.ndarray:
        """`y`データをnumpyの配列で返す"""

    def covariance(self) -> np.floating:
        """共分散を求める"""

    def correlation(self) -> np.floating:
        """相関係数を求める"""

    def correlation_coefficient(self) -> np.floating:
        """単相関係数を求める"""
    # x,y
    @property
    def Sxy(self) -> np.floating:
        """`x`と`y`の共分散を求める"""

    @property
    def Sxxyy(self) -> np.floating:
        """`x`の偏差平方和と`y`の偏差平方和の積を求める"""

    @property
    def Sxxyyroot(self) -> np.floating:
        """`x`の偏差平方和と`y`の偏差平方和の積の平方和を求める"""
    # 回帰直線
    def regression(self, n: int = 1) -> NDArray[np.floating]:
        """点(x,y)に次数`n`の多項式を当てはめる"""

    def oneregression(self) -> NDArray[np.floating]:
        """
        点(x,y)に一次方程式の回帰直線を返す

        :return: [傾き,切片]として返す
        :rtype: NDArray[np.floating]
        """

    def chebysheveve(self, Fx: _ArrayLikeFloat_co, n: int = 1) -> NDArray[np.floating]:
        """
        点`Fx`において点(x,y)に次数`n`の多項式を評価する

        :param Fx: 評価したい点を指定する
        :type Fx: _ArrayLikeFloat_co
        :param n: 次数を指定する
        :type n: int
        """
