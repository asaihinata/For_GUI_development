"""基本的な統計の計算をするモジュール"""

from typing import Any, Literal, TypeAlias

from numpy import floating, ndarray
from numpy._typing import _ArrayLikeFloat_co
from numpy.typing import NDArray

from ....typing import ArrayLikeNumber
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

class NPStatisticsds:
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    def __init__(self, x: ArrayLikeNumber, y: ArrayLikeNumber) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def x(self) -> ndarray:
        """`x`の配列を返す"""

    @property
    def y(self) -> ndarray:
        """`y`の配列を返す"""

    @property
    def xmath(self) -> NPStatisticsd: ...
    @property
    def ymath(self) -> NPStatisticsd: ...
    def covariance(self):
        """共分散を求める"""

    def correlation(self):
        """相関係数を求める"""

    def correlation_coefficient(self):
        """単相関係数を求める"""
    # x,y
    @property
    def Sxxyy(self):
        """`x`の偏差平方和と`y`の偏差平方和の積を求める"""

    @property
    def Sxxyyroot(self):
        """`x`の偏差平方和と`y`の偏差平方和の積の平方和を求める"""
    # 回帰直線
    def regression(self, n: int = 1) -> NDArray[floating]:
        """点(x,y)に次数`n`の多項式を当てはめる"""

    def oneregression(self) -> NDArray[floating]:
        """
        点(x,y)に一次方程式の回帰直線を返す

        :return: [傾き,切片]として返す
        :rtype: NDArray[floating]
        """

    def chebysheveve(
        self, Fx: _ArrayLikeFloat_co, n: int = 1
    ) -> NDArray[floating[Any]]:
        """
        点`Fx`において点(x,y)に次数`n`の多項式を評価する

        :param Fx: 評価したい点を指定する
        :type Fx: _ArrayLikeFloat_co
        :param n: 次数を指定する
        :type n: int
        """
