from datetime import date, datetime
from typing import Any, overload

import numpy as np
from numpy._typing import ArrayLike, _DT64Codes

from ..nparray import NPArray
from ..npnumber import NPNumber

__all__ = ["NPDate"]

class NPDate(NPArray):
    def __new__(
        cls,
        data: ArrayLike,
        dtype: _DT64Codes | np.datetime64 = "datetime64[D]",
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate: ...
    @property
    def data[T](self: T) -> np.ndarray[T]:
        """`NPDate`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def tonumpy[T](self: T) -> np.ndarray[T]:
        """`NPDate`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def __instancecheck__(cls, instance: Any) -> bool: ...
    def __add__(self, other: Any) -> NPDate: ...
    def __sub__(self, other: Any) -> NPDate: ...
    __radd__ = __add__
    __rsub__ = __sub__
    @classmethod
    def today(cls) -> NPDate:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls) -> NPDate:
        """現在時刻(UTC時刻)を返す"""

    def todatetime(self) -> np.ndarray[datetime, np.dtype[datetime]]:
        """配列内の日付を`datetime.datetime`に変換する"""

    def todate(self) -> np.ndarray[date, np.dtype[date]]:
        """配列内の日付を`datetime.date`に変換する"""

    def weekday(self) -> NPNumber:
        """その日付日時の曜日を求める"""

    @overload
    def diff_today(self, days: bool = ...) -> NPNumber:
        """
        今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = True) -> NPNumber:
        """
        今日の日付の差(今日を含む)を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = False) -> NPNumber:
        """今日の日付の差(今日を含めない)を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """
