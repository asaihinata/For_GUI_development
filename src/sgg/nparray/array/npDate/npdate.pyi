from datetime import date, datetime
from typing import Any, Iterator, Literal, Self, overload

import numpy as np
from numpy import datetime64
from numpy._typing import _DTypeLikeTD64

from .._typing import _ArrayLikeTD64_co, _DTypeT, _ShapeT
from ..dev import _ArrayShapeMixin
from ..npbool import NPBool
from ..npnumber import NPNumber
from ._types import _DATES_UNITL
from .npformatdate import NPFormatDate

__all__ = ["NPDate"]

class NPDate(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承した日付の配列クラス"""

    _element_type: tuple[
        type[NPFormatDate], type[np.datetime64], type[datetime], type[date]
    ]
    _default_dtype: Literal["datetime64[D]"]

    @overload
    def __new__(
        cls,
        data: _ArrayLikeTD64_co,
        dtype: None = "datetime64[D]",
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[datetime64]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeTD64_co,
        dtype: _DATES_UNITL,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[_DATES_UNITL]]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeTD64_co,
        dtype: datetime64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[datetime64]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeTD64_co,
        dtype: _DTypeLikeTD64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[_DTypeLikeTD64]]: ...
    @overload
    def __new__(
        cls,
        data: NPFormatDate,
        dtype: datetime64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[datetime64]]: ...
    def __new__(
        cls,
        data: _ArrayLikeTD64_co | NPFormatDate,
        dtype: _DTypeLikeTD64 | None = "datetime64[D]",
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeTD64_co | NPFormatDate
        :param dtype: 配列の型を指定する
        :type dtype: _DTypeLikeTD64 | None
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @classmethod
    def today(cls) -> NPDate:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls) -> NPDate:
        """現在時刻(UTC時刻)を返す"""

    def __class_getitem__(
        cls, item: Any
    ) -> type[NPDate[_ShapeT, np.dtype[_DTypeT]]]: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPDate | Any:
        """
        NumPyのufuncの動作をカスタマイズする

        :param ufunc: 呼び出されたufunc
        :type ufunc: np.ufunc
        :param method: 呼び出しメソッド名
        :type method: str
        :param inputs: ufuncへの入力
        :type inputs: Any
        :param kwargs: ufuncへの追加引数
        :type kwargs: Any
        :return: 処理結果を返す
        """

    @overload
    def __array__(
        self, dtype: None = None, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT_co]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT | None, copy: bool | None = None
    ) -> (
        np.ndarray[np._ShapeT_co, np._DTypeT] | np.ndarray[np._ShapeT_co, np._DTypeT_co]
    ): ...
    def __array_function__(
        self,
        func: Any,
        types: Any,
        args: tuple,
        kwargs: dict,
    ) -> Any:
        """
        numpy関数の動作をカスタマイズする

        :param func: 呼び出されたnumpy関数
        :type func: Any
        :param types: 関連する型のコレクション
        :type types: Any
        :param args: 位置引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: 演算結果を返す
        :rtype: Any
        """

    def __add__(self, other: Any) -> Self: ...
    def __radd__(self, other: Any) -> Self: ...
    def __sub__(self, other: Any) -> Self: ...
    def __rsub__(self, other: Any) -> Self: ...
    def __ne__(self, other: Any) -> NPBool[Any, np.dtype[np.bool]]: ...
    def __eq__(self, other: Any) -> NPBool[Any, np.dtype[np.bool]]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> Self:
        """
        逆順にした新しい配列オブジェクトを返す

        :return: 全軸で反転した配列を返す
        """

    @overload
    def __getitem__(self, key: int) -> Any | None: ...
    @overload
    def __getitem__(self, key: slice) -> np.ndarray | None: ...
    def __getitem__(self, key: int | slice) -> Any | np.ndarray | None:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`data[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: int | slice
        :return: インデックスに対応する要素を返す
        :rtype: Any | np.ndarray | None
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """

    @property
    def element_type(
        self,
    ) -> tuple[type[NPFormatDate], type[np.datetime64], type[datetime], type[date]]:
        """NPDateで許可されている型を取得する"""

    def todatetime(self) -> np.ndarray[datetime, np.dtype[datetime]]:
        """配列内の日付を`datetime.datetime`に変換する"""

    def todate(self) -> np.ndarray[date, np.dtype[date]]:
        """配列内の日付を`datetime.date`に変換する"""

    def weekday(self) -> NPNumber[list[np.uint8], np.dtype[np.uint8]]:
        """その日付日時の曜日を求める"""

    @overload
    def diff_today(self, days: bool = ...) -> NPNumber[Any, np.dtype[np.int64]]:
        """
        今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = True) -> NPNumber[Any, np.dtype[np.int64]]:
        """
        今日の日付の差(今日を含む)を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = False) -> NPNumber[Any, np.dtype[np.int64]]:
        """
        今日の日付の差(今日を含めない)を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """
