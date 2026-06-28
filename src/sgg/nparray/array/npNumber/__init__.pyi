"""基本的な数値の操作をするモジュール"""

from typing import Any, Literal, TypeAlias, Iterator

import numpy as np
from numpy.typing import ArrayLike, DTypeLike

from ....typing import TypeArraysLikeNumber
from ..nparray import NPArray

__all__ = ["NPNumber"]
TYPEMETHOD: TypeAlias = Literal[
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

class NPNumber(NPArray):
    def __new__(
        cls,
        data: TypeArraysLikeNumber,
        dtype: DTypeLike | None = np.float64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber: ...
    @property
    def data[T](self:T) -> np.ndarray[T]:
        """`NPNumber`オブジェクトを`np.ndarray`オブジェクトに変換する"""
    def tonumpy[T](self:T)->np.ndarray[T]:
        """`NPNumber`オブジェクトを`np.ndarray`オブジェクトに変換する"""
    @classmethod
    def __instancecheck__(cls,instance:Any)->bool:...
    def __iter__(self) -> Iterator[np.number]: ...
    def __getitem__(self, key: int) -> np.number:
        """インデックスアクセスをカスタマイズする

        intキーの場合は1次元に展開してからアクセスし,範囲外のインデックスはモジュロで折り返す

        :param key: インデックスまたはスライスを指定する
        :type key: int
        :return: インデックスに対応する要素を返す
        :rtype: np.number
        :raises IndexError: 配列が空の場合に発生させる
        """
    def __abs__(self) -> NPNumber: ...
    def __add__(self, other: ArrayLike) -> NPNumber: ...
    def __sub__(self, other: ArrayLike) -> NPNumber: ...
    def __mul__(self, other: ArrayLike) -> NPNumber: ...
    def __truediv__(self, other: ArrayLike) -> NPNumber: ...
    def __iadd__(self, other: ArrayLike) -> NPNumber: ...
    def __isub__(self, other: ArrayLike) -> NPNumber: ...
    def __imul__(self, other: ArrayLike) -> NPNumber: ...
    def __itruediv__(self, other: ArrayLike) -> NPNumber: ...
    def __radd__(self, other: ArrayLike) -> NPNumber: ...
    def __rsub__(self, other: ArrayLike) -> NPNumber: ...
    def __rmul__(self, other: ArrayLike) -> NPNumber: ...
    def __rtruediv__(self, other: ArrayLike) -> NPNumber: ...
    def __mod__(self, other: ArrayLike) -> NPNumber: ...
    def __floordiv__(self, other: ArrayLike) -> NPNumber: ...
    def __pow__(self, other: ArrayLike) -> NPNumber: ...
    def __eq__(self, value: Any) -> Any: ...
    def __ne__(self, value: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    @property
    def sturgesval(self) -> np.floating:
        """スタージェスの公式を求める"""

    def cussum(self) -> NPNumber:
        """一つ前の元の値との和を求める"""

    def cumprod(self) -> NPNumber:
        """一つ前の元の値との積を求める"""

    def percentile(
        self,
        q: tuple[int | float, ...],
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: tuple[int | float,...]
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    def quantile(
        self,
        q: tuple[float, ...],
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: tuple[float,...]
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    def ratio(self, axis: int | None = None) -> np.ndarray:
        """行や列ごとの合計に対する比率を求める"""

    def zero_check(self) -> np.ndarray:
        """要素の数値が0の位置を探す"""
