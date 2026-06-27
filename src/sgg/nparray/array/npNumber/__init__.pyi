"""基本的な計算をするモジュール"""

from typing import Literal

from _typeshed import Incomplete
from numpy import float64, ndarray

from ....typing import TypeArraysLikeNumber
from ..nparray import NPArray

__all__ = ["NPNumber"]

class NPNumber(NPArray):
    def __new__(cls, data:TypeArraysLikeNumber, dtype=float64,d_ndim=None, min_ndim=None, max_ndim=None):...
    def __abs__(self) -> NPNumber: ...
    def __add__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __sub__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __mul__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __truediv__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __iadd__ = __add__
    __isub__ = __sub__
    __imul__ = __mul__
    __itruediv__ = __truediv__
    def __eq__(self, value: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __ne__(self, value: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __lt__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __le__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __gt__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __ge__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __mod__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __floordiv__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __pow__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    @property
    def sturgesval(self) -> float64:
        """スタージェスの公式を求める"""
    def cussum(self) -> NPNumber:
        """一つ前の元の値との和を求める"""

    def cumprod(self) -> NPNumber:
        """一つ前の元の値との積を求める"""

    def percentile(
        self,
        q: tuple[int, ...],
        axis: int | None = None,
        method: Literal[
            "inverted_cdf",
            "averaged_inverted_cdf",
            "closest_observation",
            "interpolated_inverted_cdf",
            "hazen",
            "weibull",
            "linear",
            "median_unbiased",
            "normal_unbiased",
        ] = "linear",
    ) -> ndarray: ...
    def quantile(
        self,
        q: tuple[int, ...],
        axis: int | None = None,
        method: Literal[
            "inverted_cdf",
            "averaged_inverted_cdf",
            "closest_observation",
            "interpolated_inverted_cdf",
            "hazen",
            "weibull",
            "linear",
            "median_unbiased",
            "normal_unbiased",
        ] = "linear",
    ) -> ndarray: ...
    def ratio(self, axis: int | None = None) -> ndarray:
        """行や列ごとの合計に対する比率を求める"""

    def zero_check(self) -> ndarray:
        """要素の数値が0の位置を探す"""
