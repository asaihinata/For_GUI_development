"""様々な日付の文字列フォーマットから日付に変換するオブジェクト"""

from datetime import date, datetime
from types import GenericAlias
from typing import Any, Iterator, Literal, Self, TypeVar, overload

import numpy as np
from numpy import datetime64

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPFormatDate"]

_DTypeT = TypeVar(
    "_DTypeT", bound=np.generic, default=np.dtype[datetime64], covariant=True
)

class NPFormatDate[_ShapeT: sgt._ArrayLikeStr_co, _Dtypes: _DTypeT](
    _ArrayCommonMixin, np.ndarray[_ShapeT, np.dtype[_Dtypes]]
):
    """`np.ndarray`を継承した様々な日付のフォーマットを特定の日付フォーマットに変換する配列クラス"""

    _element_type: type[datetime64]
    _default_dtype: Literal["datetime64[D]"]

    @overload
    def __new__(
        cls,
        data: _ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[Dtype: sgt._MonthU64](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeStr_co, Dtype: (sgt._DayU64 | sgt._NVU64)](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate[_ShapeT, np.dtype[datetime64[datetime]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeStr_co, Dtype: sgt._IntUD64](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate[_ShapeT, np.dtype[datetime64[int]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeStr_co, Dtype: sgt._DT64Codes_any](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPFormatDate[_ShapeT, np.dtype[datetime64[Any]]]: ...
    def __new__() -> Self:
        """
        様々な日付のフォーマットを特定の日付フォーマットに変換する配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
        :param yearfirst: 曖昧な3つの整数からなる日付の最初の値を年として解釈するかどうか指定する
        :type yearfirst: bool
        :param dayfirst: 曖昧な3つの整数からなる日付の最初の値を日もしくは月として解釈するかどうか指定する
        :type dayfirst: bool
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __add__(self, value: sgt._ArrayLikeTD64_co) -> Self: ...
    __iadd__ = __add__
    __radd__ = __add__
    def __sub__(self, value: sgt._ArrayLikeTD64_co) -> Self: ...
    __isub__ = __sub__
    __rsub__ = __sub__
    def __eq__(self, value: Any) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    def __ne__(self, value: Any) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    def __lt__(self, value: Any) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    def __le__(self, value: Any) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    def __gt__(self, value: Any) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    def __ge__(self, value: Any) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
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

    @overload
    def __array__(
        self, dtype: None = None, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, _Dtypes]: ...
    @overload
    def __array__[Dtype: np._dtype | sgt._DTypeLike[np.generic]](
        self, dtype: Dtype, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, Dtype]: ...
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

    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    @property
    def element_type(self) -> type[datetime64]:
        """NPFormatDateで許可されている型を取得する"""

    def to_datetime(self) -> np.ndarray[_ShapeT, np.dtype[datetime]]:
        """配列内の日付を`datetime.datetime`に変換する"""

    def to_date(self) -> np.ndarray[_ShapeT, np.dtype[date]]:
        """配列内の日付を`datetime.date`に変換する"""

    def weekday(self) -> NPNumber[_ShapeT, np.dtype[np.uint8]]:
        """その日付日時の曜日を求める"""

    @overload
    def diff_today(self, days: bool = True) -> NPNumber[_ShapeT, np.dtype[np.int64]]:
        """
        配列の日付と今日の日付の差を求める(今日を含む)

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = False) -> NPNumber[_ShapeT, np.dtype[np.int64]]:
        """
        配列の日付と今日の日付の差を求める(今日を含めない)

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    def diff_today():
        """
        配列の日付と今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def range(
        self: NPFormatDate[_ShapeT, _DTypeT], axis: None = None
    ) -> tuple[datetime64[_DTypeT], datetime64[_DTypeT]]: ...
    @overload
    def range(
        self: NPFormatDate[_ShapeT, _DTypeT], axis: np._ShapeLike
    ) -> tuple[NPFormatDate[_ShapeT, _DTypeT], NPFormatDate[_ShapeT, _DTypeT]]: ...
    def range():
        """
        配列内の日付の最小の日付と最大の日付を求める

        :param axis: 求める軸を指定する。
        :type axis: Typeaxis
        """

    def to_1d(self) -> NPFormatDate[tuple[int], _Dtypes]:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :return: フラット化した配列オブジェクトを返す
        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
