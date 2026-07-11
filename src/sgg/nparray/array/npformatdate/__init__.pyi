from datetime import date, datetime
from typing import Any, Iterator, Literal, Self, TypeVar, overload

import numpy as np
from numpy import datetime64
from numpy._typing import _ArrayLikeDT64_co, _DTypeLikeTD64

from sgg.typing import _ArrayLikeDateParse_co, _ShapeT

from ..dev import _ArrayShapeMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPFormatDate"]
HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

_DTypeT = TypeVar(
    "_DTypeT", bound=np.dtype, default=np.dtype[datetime64], covariant=True
)

class NPFormatDate(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承した様々な日付のフォーマットを特定の日付フォーマットに変換する配列クラス"""

    _element_type: type[datetime64]
    _default_dtype: Literal["datetime64[D]"]

    @overload
    def __new__(
        cls,
        data: _ArrayLikeDateParse_co,
        dtype: None = None,
        yearfirst: bool = ...,
        dayfirst: bool = ...,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPFormatDate[_ShapeT, np.dtype[datetime64]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeDateParse_co,
        dtype: _DTypeLikeTD64,
        yearfirst: bool = ...,
        dayfirst: bool = ...,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPFormatDate[_ShapeT, np.dtype[_DTypeLikeTD64]]: ...
    def __new__(
        cls,
        data: _ArrayLikeDateParse_co,
        dtype: _DTypeLikeTD64 | None = "datetime64[D]",
        yearfirst: bool = ...,
        dayfirst: bool = ...,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        様々な日付のフォーマットを特定の日付フォーマットに変換する配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeDateParse_co
        :param dtype: 配列の型を指定する
        :type dtype: _DTypeLikeTD64 | None
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
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __add__(self, value: int | bool) -> NPFormatDate[_ShapeT, _DTypeT]: ...
    @overload
    def __add__(self, value: _ArrayLikeDT64_co) -> NPFormatDate[Any, _DTypeT]: ...
    def __add__(self, value: int | bool | _ArrayLikeDT64_co) -> NPFormatDate: ...
    @overload
    def __iadd__(self, value: int | bool) -> NPFormatDate[_ShapeT, _DTypeT]: ...
    @overload
    def __iadd__(self, value: _ArrayLikeDT64_co) -> NPFormatDate[Any, _DTypeT]: ...
    def __iadd__(self, value: int | bool | _ArrayLikeDT64_co) -> NPFormatDate: ...
    @overload
    def __radd__(self, value: int | bool) -> NPFormatDate[_ShapeT, _DTypeT]: ...
    @overload
    def __radd__(self, value: _ArrayLikeDT64_co) -> NPFormatDate[Any, _DTypeT]: ...
    def __radd__(self, value: int | bool | _ArrayLikeDT64_co) -> NPFormatDate: ...
    @overload
    def __sub__(self, value: int | bool) -> NPFormatDate[_ShapeT, _DTypeT]: ...
    @overload
    def __sub__(self, value: _ArrayLikeDT64_co) -> NPFormatDate[Any, _DTypeT]: ...
    def __sub__(self, value: int | bool | _ArrayLikeDT64_co) -> NPFormatDate: ...
    @overload
    def __isub__(self, value: int | bool) -> NPFormatDate[_ShapeT, _DTypeT]: ...
    @overload
    def __isub__(self, value: _ArrayLikeDT64_co) -> NPFormatDate[Any, _DTypeT]: ...
    def __isub__(self, value: int | bool | _ArrayLikeDT64_co) -> NPFormatDate: ...
    @overload
    def __rsub__(self, value: int | bool) -> NPFormatDate[_ShapeT, _DTypeT]: ...
    @overload
    def __rsub__(self, value: _ArrayLikeDT64_co) -> NPFormatDate[Any, _DTypeT]: ...
    def __rsub__(self, value: int | bool | _ArrayLikeDT64_co) -> NPFormatDate: ...
    def __class_getitem__(cls, item: Any) -> type[NPFormatDate[Any, Any]]: ...
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

    def __ne__(self, value: Any) -> NPBool[Any]: ...
    def __eq__(self, value: Any) -> NPBool[Any]: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    @property
    def element_type(self) -> type[datetime64]:
        """NPFormatDateで許可されている型を取得する"""

    def todatetime(self) -> np.ndarray[_ShapeT, np.dtype[datetime]]:
        """配列内の日付を`datetime.datetime`に変換する"""

    def todate(self) -> np.ndarray[_ShapeT, np.dtype[date]]:
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

    def diff_today(self, days: bool = ...) -> NPNumber[_ShapeT, np.dtype[np.int64]]:
        """
        配列の日付と今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """
