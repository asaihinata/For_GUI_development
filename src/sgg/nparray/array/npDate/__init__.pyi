from datetime import date, datetime
from typing import Any, Iterator, Literal, Self, overload

import numpy as np
from numpy import datetime64
from numpy._typing import _ArrayLikeDT64_co, _DTypeLikeTD64, _NestedSequence

from sgg.typing import Typeaxis, _ArrayLikeTD64_co

from ..dev import _ArrayShapeMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPDate"]

class NPDate[_ShapeT: np._SupportsArray[_ArrayLikeTD64_co], _DTypeT](
    _ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]
):
    """`np.ndarray`を継承した日付の配列クラス"""

    _element_type: type[datetime64]
    _default_dtype: Literal["datetime64[D]"]

    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[_DTypeLikeTD64]]: ...
    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: _DTypeLikeTD64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[_ShapeT, np.dtype[_DTypeLikeTD64]]: ...
    def __new__(
        cls,
        data: _ShapeT,
        dtype: _DTypeLikeTD64 | None = "datetime64[D]",
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeTD64_co
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
    ) -> np.ndarray[_ShapeT, _DTypeT]: ...
    @overload
    def __array__[DType](
        self, dtype: DType, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, np.dtype[DType]]: ...
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

    @overload
    def __add__(self, value: int | bool) -> NPDate[_ShapeT, _DTypeT]: ...
    @overload
    def __add__(self, value: _ArrayLikeDT64_co) -> NPDate[Any, _DTypeT]: ...
    @overload
    def __iadd__(self, value: int | bool) -> NPDate[_ShapeT, _DTypeT]: ...
    @overload
    def __iadd__(self, value: _ArrayLikeDT64_co) -> NPDate[Any, _DTypeT]: ...
    @overload
    def __radd__(self, value: int | bool) -> NPDate[_ShapeT, _DTypeT]: ...
    @overload
    def __radd__(self, value: _ArrayLikeDT64_co) -> NPDate[Any, _DTypeT]: ...
    @overload
    def __sub__(self, value: int | bool) -> NPDate[_ShapeT, _DTypeT]: ...
    @overload
    def __sub__(self, value: _ArrayLikeDT64_co) -> NPDate[Any, _DTypeT]: ...
    @overload
    def __isub__(self, value: int | bool) -> NPDate[_ShapeT, _DTypeT]: ...
    @overload
    def __isub__(self, value: _ArrayLikeDT64_co) -> NPDate[Any, _DTypeT]: ...
    @overload
    def __rsub__(self, value: int | bool) -> NPDate[_ShapeT, _DTypeT]: ...
    @overload
    def __rsub__(self, value: _ArrayLikeDT64_co) -> NPDate[Any, _DTypeT]: ...
    @overload
    def __ne__(self, value: datetime64) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __ne__(
        self, value: _ArrayLikeDT64_co | _NestedSequence[np._SupportsGT]
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __ne__(self, value: np._SupportsGT) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __eq__(self, value: datetime64) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __eq__(
        self, value: _ArrayLikeDT64_co | _NestedSequence[np._SupportsGT]
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __eq__(self, value: np._SupportsGT) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __lt__(self, value: datetime64) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __lt__(
        self, value: _ArrayLikeDT64_co | _NestedSequence[np._SupportsGT]
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __lt__(self, value: np._SupportsGT) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __le__(self, value: datetime64) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __le__(
        self, value: _ArrayLikeDT64_co | _NestedSequence[np._SupportsGT]
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __le__(self, value: np._SupportsGT) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __gt__(self, value: datetime64) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __gt__(
        self, value: _ArrayLikeDT64_co | _NestedSequence[np._SupportsGT]
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __gt__(self, value: np._SupportsGT) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __ge__(self, value: datetime64) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __ge__(
        self, value: _ArrayLikeDT64_co | _NestedSequence[np._SupportsGT]
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __ge__(self, value: np._SupportsGT) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    @property
    def element_type(self) -> type[datetime64]:
        """NPDateで許可されている型を取得する"""

    def todatetime(self) -> np.ndarray[_ShapeT, np.dtype[datetime]]:
        """配列内の日付を`datetime.datetime`に変換する"""

    def todate(self) -> np.ndarray[_ShapeT, np.dtype[date]]:
        """配列内の日付を`datetime.date`に変換する"""

    @classmethod
    def today(cls) -> NPDate:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls) -> NPDate:
        """現在時刻(UTC時刻)を返す"""

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

    @overload
    def range(
        self: NPDate[_ShapeT, _DTypeT], axis: None = None
    ) -> tuple[datetime64[_DTypeT], datetime64[_DTypeT]]: ...
    @overload
    def range(
        self: NPDate[_ShapeT, _DTypeT], axis: np._ShapeLike
    ) -> tuple[NPDate[_ShapeT, _DTypeT], NPDate[_ShapeT, _DTypeT]]: ...
    def range(self, axis: Typeaxis = None) -> tuple[
        NPDate[_ShapeT, _DTypeT] | datetime64[_DTypeT],
        NPDate[_ShapeT, _DTypeT] | datetime64[_DTypeT],
    ]:
        """
        配列内の日付の最小の日付と最大の日付を求める

        :param axis: 求める軸を指定する。
        :type axis: Typeaxis
        """
