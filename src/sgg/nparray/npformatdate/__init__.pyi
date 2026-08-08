"""様々な日付の文字列フォーマットから日付に変換するオブジェクト"""

from typing import Any, Literal, NoReturn, overload

import numpy as np
from numpy import datetime64

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPFormatDate"]

class NPFormatDate(_ArrayCommonMixin):
    """`np.ndarray`を継承した様々な日付のフォーマットを特定の日付フォーマットに変換する配列クラス"""

    _element_type: type[datetime64]
    _default_dtype: Literal["datetime64[D]"]
    @overload
    def __new__(
        cls,
        data: sgt._ArrayLikeString_co,
        /,
        dtype: sgt._DtypeLikeDT = "datetime64[D]",
        *,
        yearfirst: bool = False,
        dayfirst: bool = False,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate:
        """
        様々な日付のフォーマットを特定の日付フォーマットに変換する配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意の文字列型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.datetime64 | _DT64Codes_All
        :param yearfirst: 曖昧な3つの整数からなる日付の最初の値を年として解釈するかどうか指定する
        :type yearfirst: bool
        :param dayfirst: 曖昧な3つの整数からなる日付の最初の値を日もしくは月として解釈するかどうか指定する
        :type dayfirst: bool
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
        data: sgt._ArrayLikeString_co,
        /,
        dtype: sgt._DtypeLikeDT = "datetime64[D]",
        *,
        yearfirst: bool = False,
        dayfirst: bool = False,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate:
        """
        様々な日付のフォーマットを特定の日付フォーマットに変換する配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意の文字列型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.datetime64 | _DT64Codes_All
        :param yearfirst: 曖昧な3つの整数からなる日付の最初の値を年として解釈するかどうか指定する
        :type yearfirst: bool
        :param dayfirst: 曖昧な3つの整数からなる日付の最初の値を日もしくは月として解釈するかどうか指定する
        :type dayfirst: bool
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __add__(self, value: sgt._ArrayLikeTD64_co) -> NPFormatDate: ...
    __iadd__ = __add__
    __radd__ = __add__
    def __sub__(self, value: sgt._ArrayLikeTD64_co) -> NPFormatDate: ...
    __isub__ = __sub__
    __rsub__ = __sub__
    @overload
    def __eq__(self, value: sgt._ComparisonType) -> sgt.RBool_: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ComparisonType) -> sgt.RBool_: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    @overload
    def __lt__(self, value: sgt._ComparisonType) -> sgt.RBool_: ...
    @overload
    def __lt__(self, value: Any) -> NoReturn: ...
    @overload
    def __le__(self, value: sgt._ComparisonType) -> sgt.RBool_: ...
    @overload
    def __le__(self, value: Any) -> NoReturn: ...
    @overload
    def __gt__(self, value: sgt._ComparisonType) -> sgt.RBool_: ...
    @overload
    def __gt__(self, value: Any) -> NoReturn: ...
    @overload
    def __ge__(self, value: sgt._ComparisonType) -> sgt.RBool_: ...
    @overload
    def __ge__(self, value: Any) -> NoReturn: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPFormatDate | Any:
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

    @property
    def element_type(self) -> type[datetime64]:
        """NPFormatDateで許可されている型を取得する"""

    def to_datetime(self) -> np.ndarray:
        """配列内の日付を`datetime.datetime`に変換する"""

    def to_date(self) -> np.ndarray:
        """配列内の日付を`datetime.date`に変換する"""
    # 日付
    @property
    def year(self) -> sgt.RInt64:
        """配列の年を返す"""

    @property
    def month(self) -> sgt.RUInt8:
        """配列の月を返す"""

    @property
    def day(self) -> sgt.RUInt8:
        """配列の日付を返す"""

    def weekday(self) -> sgt.RUInt8:
        """その日付時刻の曜日をツェラーの公式で求める"""

    def diff_today(self, days: bool = ...) -> sgt.RInt64:
        """
        配列の日付と今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    def range(self) -> tuple[datetime64, datetime64]:
        """配列内の日付の最小の日付と最大の日付を求める"""

    def choice(
        self,
        size: int | tuple[int, ...] | None = None,
        replace: bool = True,
        p: sgt._ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: sgt._Seed = None,
    ) -> sgt.Rdatetime64:
        """
        配列の要素もしくは軸の配列をランダムに抽選する

        :param size: 出力する配列の形状を指定する
        :type size: int | tuple[int,...] | None
        :param replace: 抽選する値が復元抽出をするか非復元抽出をするかを指定する
        :type replace: bool
        :param p: 各要素が選ばれる重みを指定する
        :type p: _ArrayLikeFloat_co | None
        :param axis: 選択を行う軸を指定する
        :type axis: int
        :param shuffle: 非復元抽出をする際にサンプルをシャッフルするか指定する
        :type shuffle: bool
        :param seed: 乱数のシード値を指定する
        :type seed: int | SeedSequence | Generator | None
        """
