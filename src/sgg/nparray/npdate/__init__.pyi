from datetime import date, datetime
from types import GenericAlias
from typing import Any, Iterator, Literal, Self, TypeVar, overload

import numpy as np
from numpy import datetime64
from numpy._typing import _DTypeLike, _SupportsArrayFunc, _TD64Like_co

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool
from ..npnumber import NPNumber
from ..npstr import NPString

__all__ = ["NPDate"]
_DTypeT_co = TypeVar(
    "_DTypeT_co", bound=np.dtype, default=np.dtype[datetime64], covariant=True
)

class NPDate[_ShapeT, _Dtypes: _DTypeT_co](
    _ArrayCommonMixin, np.ndarray[_ShapeT, np.dtype[_Dtypes]]
):
    """`np.ndarray`を継承した日付の配列クラス"""

    _element_type: type[datetime64]
    _default_dtype: Literal["datetime64[D]"]
    @overload
    def __new__[_ShapeT, Dtype](
        cls,
        data: NPDate[_ShapeT, Dtype],
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, Dtype]: ...
    @overload
    def __new__[_ShapeT, Dtype: sgt._MonthU64](
        cls,
        data: NPDate[_ShapeT],
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[_ShapeT, Dtype: (sgt._DayU64 | sgt._NVU64)](
        cls,
        data: NPDate[_ShapeT],
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[datetime]]]: ...
    @overload
    def __new__[_ShapeT, Dtype: sgt._DT64Codes_any](
        cls,
        data: NPDate[_ShapeT],
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[Any]]]: ...
    @overload
    def __new__[_ShapeT, Dtype: sgt._IntUD64](
        cls,
        data: NPDate[_ShapeT],
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[int]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeNone_co](
        cls,
        data: _ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeNone_co, Dtype: sgt._MonthU64](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeNone_co, Dtype: (sgt._DayU64 | sgt._NVU64)](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[datetime]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeNone_co, Dtype: sgt._DT64Codes_any](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[Any]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeNone_co, Dtype: sgt._IntUD64](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[int]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeDT64_co](
        cls,
        data: _ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeDT64_co, Dtype: sgt._MonthU64](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[date]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeDT64_co, Dtype: (sgt._DayU64 | sgt._NVU64)](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[datetime]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeDT64_co, Dtype: sgt._IntUD64](
        cls,
        data: _ShapeT,
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[int]]]: ...
    @overload
    def __new__[_ShapeT: sgt._ArrayLikeDT64_co, Dtype: sgt._DT64Codes_any](
        cls,
        data: _ShapeT,
        dtype: Dtype,
        /,
        d_ndim: int | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate[_ShapeT, np.dtype[datetime64[Any]]]: ...
    def __new__() -> Self:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
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

    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
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
        self, dtype: None = None, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, _Dtypes]: ...
    @overload
    def __array__[DType: np._dtype | _DTypeLike[np.generic]](
        self, dtype: DType, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, DType]: ...
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
    def __iter__(self) -> Iterator[np.ndarray[Any, Any]]: ...
    @property
    def year(self) -> NPNumber:
        """配列の年を返す"""

    @property
    def month(self) -> NPNumber:
        """配列の月を返す"""

    @property
    def day(self) -> NPNumber:
        """配列の日付を返す"""

    @property
    def element_type(self) -> type[datetime64]:
        """NPDateで許可されている型を取得する"""

    def to_datetime(self) -> np.ndarray[Any, np.dtype[datetime]]:
        """配列内の日付を`datetime.datetime`に変換する"""

    def to_date(self) -> np.ndarray[Any, np.dtype[date]]:
        """配列内の日付を`datetime.date`に変換する"""

    @classmethod
    def arange(
        cls,
        start: sgt._DateArangeScalar,
        stop: sgt._DateArangeScalar,
        /,
        step: _TD64Like_co | None = 1,
        *,
        dtype: _DTypeLike[datetime64] | None = None,
        device: Literal["cpu"] | None = None,
        like: _SupportsArrayFunc | None = None,
    ) -> NPDate[
        sgt._Array1D[datetime64[sgt.Incomplete]], np.dtype[datetime64[sgt.Incomplete]]
    ]:
        """
        指定された間隔内で等間隔の日付を返す

        :param start: 区間を開始する日付を指定する
        :type start: datetime64 | str | np.str_
        :param stop: 区間を終了する日付を指定する
        :type stop: datetime64 | str | np.str_
        :param step: 値の間隔を指定する
        :type step: _TD64Like_co | None
        :param dtype: 出力配列の型を指定する
        :type dtype: dtype
        :param device: 作成された配列を配置する場所を指定する
        :type device: Literal["cpu"] | None
        :param like: NumPy配列ではない配列を作成できるようにする参照するオブジェクトを指定する
        :type like: _SupportsArrayFunc | None
        """

    @classmethod
    def today(cls) -> NPDate[datetime64[date], np.dtype[datetime64[date]]]:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls) -> NPDate[datetime64[datetime], np.dtype[datetime64[datetime]]]:
        """現在時刻(UTC時刻)を返す"""

    @classmethod
    def unix(cls) -> NPDate[datetime64[datetime], np.dtype[datetime64[datetime]]]:
        """UTC時刻を返す"""

    def strftime[ShapeT](
        self: NPDate[ShapeT, np.dtype[datetime64]], format: str
    ) -> NPString[ShapeT, np.dtype[np.str_]]:
        """日付のフォーマットを別のフォーマットで変換する"""

    def weekday[ShapeT](
        self: NPDate[ShapeT, np.dtype[datetime64]],
    ) -> NPNumber[ShapeT, np.dtype[np.uint8]]:
        """その日付日時の曜日を求める"""

    @overload
    def diff_today(self, days: bool = True) -> NPNumber[Any, np.dtype[np.int64]]:
        """
        配列の日付と今日の日付の差を求める(今日を含む)

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def diff_today(self, days: bool = False) -> NPNumber[Any, np.dtype[np.int64]]:
        """
        配列の日付と今日の日付の差を求める(今日を含めない)

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    def diff_today(self, days: bool = ...) -> NPNumber[Any, np.dtype[np.int64]]:
        """
        配列の日付と今日の日付の差を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    @overload
    def range(self, axis: None = None) -> tuple[datetime64, datetime64]: ...
    @overload
    def range(
        self, axis: np._ShapeLike
    ) -> tuple[NPDate[_ShapeT, _Dtypes], NPDate[_ShapeT, _Dtypes]]: ...
    def range():
        """
        配列内の日付の最小の日付と最大の日付を求める

        :param axis: 求める軸を指定する。
        :type axis: Typeaxis
        """

    def leapyear(
        self: NPDate[_ShapeT, np.dtype[_Dtypes]],
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]:
        """その日付の年がうるう年かどうかを判定する"""

    def leapcount(self) -> int:
        """配列内のうるう年の数を数える"""

    def cleanNaT[_Dtype](self: NPDate[_ShapeT, _Dtype]) -> NPDate[tuple[int], _Dtype]:
        """配列を一次元配列にし欠損日(NaT)を削除する"""

    def to_1d(self) -> NPDate[tuple[int], _Dtypes]:
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
