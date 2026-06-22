from collections.abc import Iterator
from datetime import tzinfo
from types import NotImplementedType
from typing import Any, Literal, overload

import numpy as np
from numpy._typing import ArrayLike, DTypeLike, NDArray, _DT64Codes

from ..nparray import NPArray
from ._typing import DateUnit, NativeTimeUnit

__all__ = ["NPDate"]

class NPDate(NPArray):
    def __init__(
        self,
        data: ArrayLike,
        dtype: _DT64Codes | np.datetime64 = "datetime64[D]",
        depth_limit: int | None = None,
    ) -> None:
        """
        :param data: データの配列を指定する
        :type data: ArrayLike
        :param dtype: numpyの配列で指定する型を指定する
        :type dtype: _DT64Codes | np.datetime64
        :param depth_limit: 配列の最大の深さを指定する
        :type depth_limit: int | None
        """

    def __iter__(self) -> Iterator[Any]: ...
    def __getitem__(self, key: int) -> Any: ...
    def __contains__(self, item: Any) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> NPDate:
        """`numpy.fliplr`を実行する"""

    def __array__(
        self, dtype: DTypeLike | None = None, copy: bool | np._CopyMode | None = None
    ) -> np.ndarray: ...
    def __repr__(self) -> str: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: Literal["__call__", "reduce", "reduceat", "accumulate", "outer", "at"],
        *args: Any,
        **kwargs: Any,
    ) -> Any | NotImplementedType | NPDate: ...
    @property
    def T(self) -> NPDate: ...
    def astype(self, dtype: _DT64Codes) -> NPDate: ...
    @property
    def max(self) -> np.timedelta64:
        """NPDate内の最大の日付を取得する"""

    @property
    def min(self) -> np.timedelta64:
        """NPDate内の最小の日付を取得する"""

    def __add__(self, other: np.timedelta64 | int) -> NPDate: ...
    def __sub__(self, other: np.timedelta64 | int) -> NPDate: ...
    __radd__ = __add__
    __rsub__ = __sub__
    @classmethod
    def today(cls, unit: DateUnit = "D") -> NPDate:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls, unit: NativeTimeUnit = "h") -> NPDate:
        """現在時刻(UTC時刻)を返す"""

    def tostr(
        self,
        unit: (
            Literal[
                "auto",
                "Y",
                "M",
                "D",
                "h",
                "m",
                "s",
                "ms",
                "us",
                "μs",
                "ns",
                "ps",
                "fs",
                "as",
            ]
            | None
        ) = None,
        tz: Literal["naive", "UTC", "local"] | tzinfo = "naive",
        casting: Literal[
            "no", "equiv", "safe", "same_kind", "same_value", "unsafe"
        ] = "same_kind",
    ) -> NDArray[np.str_]:
        """配列内の日付を`np.str_`型に変換する"""

    def todatetime(self) -> np.ndarray:
        """配列内の日付を`datetime.datetime`に変換する"""

    def weekday(self) -> np.ndarray:
        """その日付日時の曜日を求める"""

    @overload
    def diff_today(self, days: bool = ...) -> np.ndarray:
        """
        今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = True) -> np.ndarray:
        """
        今日の日付の差(今日を含む)を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = False) -> np.ndarray:
        """今日の日付の差(今日を含めない)を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    def astype(self, dtype: DTypeLike = "datetime64[D]") -> NPDate:
        """`dtype`で指定された型に変更します"""

    def sort(self) -> NPDate:
        """`data`にソートを実行する"""

    def first_pop(self) -> NPDate:
        """配列の最初の要素のコピーをその配列の末尾に追加する"""

    def clear(self) -> NPDate:
        """配列をクリアする"""

    def deep_add(self, val: int) -> NPDate:
        """配列の深さを`val`分だけ追加する"""

    def deep_add(self, val: int) -> NPDate:
        """配列の深さが`val`より低い場合,深さを`val`にする"""

    def reshape(self, size: tuple[int, ...]) -> NPDate:
        """配列の形状を`size`で指定する"""

    def flatten(self) -> NPDate:
        """配列を一次元に平坦にする"""
