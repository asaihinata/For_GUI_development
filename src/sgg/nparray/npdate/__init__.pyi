from typing import Any, Literal, NoReturn, SupportsIndex, overload

import numpy as np
from numpy import datetime64, timedelta64
from numpy._typing import _TD64Like_co,NDArray

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPDate"]

class NPDate(_ArrayCommonMixin, np.ndarray):
    """`np.ndarray`を継承した日付の配列クラス"""

    _element_type: type[datetime64]
    _default_dtype: Literal["datetime64[D]"]
    @overload
    def __new__(
        cls,
        data: sgt._ArrayLikeDT64_co,
        /,
        dtype: sgt._DtypeLikeDT = "datetime64[D]",
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意のdatetime64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: datetime64 | _DT64Codes_All
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __new__(
        cls,
        data: sgt._ArrayLikeDT64_co,
        /,
        dtype: sgt._DtypeLikeDT = "datetime64[D]",
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意のdatetime64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: datetime64 | _DT64Codes_All
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

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

    def __add__(self, value: sgt._ArrayLikeTD64_co) -> NPDate: ...
    __iadd__ = __add__
    def __sub__(self, value: sgt._ArrayLikeTD64_co) -> NPDate: ...
    __isub__ = __sub__

    @overload
    def __eq__(self, value: sgt._ComparisonType | NPDate) -> NDArray[np.bool_]: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ComparisonType | NPDate) -> NDArray[np.bool_]: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    @overload
    def __lt__(self, value: sgt._ComparisonType | NPDate) -> NDArray[np.bool_]: ...
    @overload
    def __lt__(self, value: Any) -> NoReturn: ...
    @overload
    def __le__(self, value: sgt._ComparisonType | NPDate) -> NDArray[np.bool_]: ...
    @overload
    def __le__(self, value: Any) -> NoReturn: ...
    @overload
    def __gt__(self, value: sgt._ComparisonType | NPDate) -> NDArray[np.bool_]: ...
    @overload
    def __gt__(self, value: Any) -> NoReturn: ...
    @overload
    def __ge__(self, value: sgt._ComparisonType | NPDate) -> NDArray[np.bool_]: ...
    @overload
    def __ge__(self, value: Any) -> NoReturn: ...

    @property
    def element_type(self) -> type[datetime64]:
        """NPDateで許可されている型を取得する"""

    # 日付
    @property
    def year(self) -> NDArray[np.int64]:
        """配列の年を返す"""

    @property
    def month(self) -> NDArray[np.uint8]:
        """配列の月を返す"""

    @property
    def day(self) -> NDArray[np.uint8]:
        """配列の日付を返す"""

    # 判定
    def isnat(self) -> NDArray[np.bool_]:
        """要素が欠損(Nat)かを判定する"""

    # 変換
    def to_datetime(self) -> np.ndarray:
        """配列内の日付を`datetime.datetime`に変換する"""

    def to_date(self) -> np.ndarray:
        """配列内の日付を`datetime.date`に変換する"""

    def to_str(self) -> NDArray[np.str_]:
        """配列内の日付を`NPString`に変換する"""

    def strftime(self, format: str) -> NDArray[np.str_]:
        """日付のフォーマットを別のフォーマットで変換する"""

    @classmethod
    def arange(
        cls,
        start: sgt._DateArangeScalar,
        stop: sgt._DateArangeScalar,
        /,
        step: _TD64Like_co | None = 1,
        *,
        dtype: sgt._DT64Codes_All | None = "D",
    ) -> NPDate:
        """
        指定された間隔内で等間隔の日付を返す

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param step: 値の間隔を指定する
        :type step: int | np.timedelta64 | np.integer | np.bool | None
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Codes_All | None
        """

    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._DateArangeScalar,
        stop: sgt._DateArangeScalar,
        /,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False]= False,
        dtype: sgt._DT64Codes_All = "D",
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPDate:
        """
        指定された間隔で等間隔​​の日付を返します。

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param num: 生成する日付の数を指定する
        :type num: int
        :param endpoint: `stop`を結果に含めるか指定する
        :type endpoint: bool
        :param retstep: 計算された間隔を返すか指定する
        :type retstep: bool
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Codes_All
        :param axis: 結果にサンプルを格納する軸
        :type axis: int
        :param device: 作成された配列を配置するデバイスを指定する
        :type device: Literal["cpu"] | None
        """

    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._DateArangeScalar,
        stop: sgt._DateArangeScalar,
        /,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[True] = True,
        dtype: sgt._DT64Codes_All | None = "D",
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPDate, timedelta64]:
        """
        指定された間隔で等間隔​​の日付を返します。

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param num: 生成する日付の数を指定する
        :type num: int
        :param endpoint: `stop`を結果に含めるか指定する
        :type endpoint: bool
        :param retstep: 計算された間隔を返すか指定する
        :type retstep: bool
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Codes_All | None
        :param axis: 結果にサンプルを格納する軸
        :type axis: int
        :param device: 作成された配列を配置するデバイスを指定する
        :type device: Literal["cpu"] | None
        """

    @classmethod
    def linspace():
        """
        指定された間隔で等間隔​​の日付を返します。

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param num: 生成する日付の数を指定する
        :type num: int
        :param endpoint: `stop`を結果に含めるか指定する
        :type endpoint: bool
        :param retstep: 計算された間隔を返すか指定する
        :type retstep: bool
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Codes_All
        :param axis: 結果にサンプルを格納する軸
        :type axis: int
        :param device: 作成された配列を配置するデバイスを指定する
        :type device: Literal["cpu"] | None
        """

    def range(self) -> tuple[datetime64, datetime64]:
        """配列内の日付の最小の日付と最大の日付を求める"""

    @classmethod
    def today(cls) -> NPDate:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls) -> NPDate:
        """現在時刻(UTC時刻)を返す"""

    @classmethod
    def unix(cls) -> NPDate:
        """UTC時刻を返す"""

    def weekday(self) -> NDArray[np.uint8]:
        """その日付時刻の曜日をツェラーの公式で求める"""

    def begin_month_weekday(self) -> NDArray[np.uint8]:
        """その日付時刻の月初の曜日をツェラーの公式で求める"""

    def end_month_weekday(self) -> NDArray[np.uint8]:
        """その日付時刻の月末の曜日をツェラーの公式で求める"""

    def diff_today(self, days: bool = ...) -> NDArray[np.int64]:
        """
        配列の日付と今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    # 閏年
    def leapyear(self) -> NDArray[np.bool_]:
        """その日付の年がうるう年かどうかを判定する"""

    def leapcount(self) -> int:
        """配列内のうるう年の数を数える"""
