"""様々な日付の文字列フォーマットから日付に変換するオブジェクト"""

from typing import Any, Literal, overload

import numpy as np
from numpy import datetime64

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPFormatDate"]

class NPFormatDate(_ArrayCommonMixin, np.ndarray):
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
        :type data: 任意の文字列型(dtype)を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: datetime64 | _DT64Codes_All
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
        :type data: 任意の文字列型(dtype)を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: datetime64 | _DT64Codes_All
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
    def __eq__(self, value: Any) -> NPBool: ...
    def __ne__(self, value: Any) -> NPBool: ...
    def __lt__(self, value: Any) -> NPBool: ...
    def __le__(self, value: Any) -> NPBool: ...
    def __gt__(self, value: Any) -> NPBool: ...
    def __ge__(self, value: Any) -> NPBool: ...
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

    def weekday(self) -> NPNumber:
        """その日付日時の曜日を求める"""

    def diff_today(self, days: bool = ...) -> NPNumber:
        """
        配列の日付と今日の日付の差を求める(今日を含む)

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def range(self, axis: None = None) -> tuple[datetime64, datetime64]: ...
    @overload
    def range(self, axis: np._ShapeLike) -> tuple[NPFormatDate, NPFormatDate]: ...
    def range():
        """
        配列内の日付の最小の日付と最大の日付を求める

        :param axis: 求める軸を指定する
        :type axis: _ShapeLike | None
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
