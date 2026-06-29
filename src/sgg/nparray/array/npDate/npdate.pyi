from datetime import date, datetime
from typing import Any, Iterator, overload

import numpy as np
from numpy._typing import _DTypeLikeTD64
from numpy.lib.mixins import NDArrayOperatorsMixin
from numpy.typing import DTypeLike

from ....typing import TypeArraysLikedatetime
from ..npnumber import NPNumber

__all__ = ["NPDate"]

class NPDate(NDArrayOperatorsMixin, np.ndarray):
    """`np.ndarray`を継承した日付の配列クラス"""

    def __new__(
        cls,
        data: TypeArraysLikedatetime,
        dtype: _DTypeLikeTD64 = "datetime64[D]",
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPDate[Any, np.dtype[np.datetime64]]:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: TypeArraysLikedatetime
        :param dtype: 配列のdtypeを指定する
        :type dtype: _DTypeLikeTD64
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: NPDate
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @classmethod
    def __instancecheck__(cls, instance: Any) -> bool: ...
    def __ne__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __add__(self, other: Any) -> NPDate: ...
    def __radd__(self, other: Any) -> NPDate: ...
    def __sub__(self, other: Any) -> NPDate: ...
    def __rsub__(self, other: Any) -> NPDate: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> NPDate:
        """
        逆順にした新しい配列オブジェクトを返す

        :return: 全軸で反転した配列を返す
        """

    @overload
    def __getitem__(self, key: int) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> np.ndarray: ...
    def __getitem__(self, key: int | slice) -> Any | np.ndarray:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は1次元に展開してからアクセスし,範囲外のインデックスはモジュロで折り返す

        :param key: インデックスまたはスライスを指定する
        :type key: int | slice
        :return: インデックスに対応する要素を返す
        :rtype: Any | np.ndarray
        :raises IndexError: 配列が空の場合に発生させる
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

    def __class_getitem__(cls, item: Any) -> np.ndarray:
        return np.ndarray.__class_getitem__.__func__(cls, item)

    def __array_finalize__(self, obj: np.ndarray | None) -> None:
        """スライスやview後もdtypeや次元数情報を引き継がさせるメソッド"""

    @classmethod
    def _resolve_dtype(
        cls,
        dtype: np.dtype | str | type | None,
    ) -> np.dtype | None:
        """
        引数dtypeを解決させる

        :param dtype: ユーザーが指定するdtype
        :return: 解決されたdtypeを返す
        :rtype: numpy.dtype | None
        """

    @classmethod
    def _validate_ndim(
        cls,
        obj: np.ndarray,
        min_ndim: int | None,
        max_ndim: int | None,
    ) -> None:
        """
        配列の次元数がmin_ndim・max_ndimの範囲内か検証する

        :param obj: 検証対象の配列
        :param min_ndim: 許可する最小次元数を指定する。Noneの場合は制約なし
        :param max_ndim: 許可する最大次元数を指定する。Noneの場合は制約なし
        :raises ValueError: 次元数が範囲外の場合に発生させる
        """

    @classmethod
    def _validate_elements(cls, obj: np.ndarray) -> None:
        """
        配列内の要素が`_element_type`と一致するか検証する

        :param obj: 検証対象の配列
        :raises TypeError: 許可されていない型の要素が含まれる場合に発生させる
        """

    @property
    def data(self) -> np.ndarray:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def dtypes(self) -> np.dtype | None:
        """
        インスタンス生成時に確定したdtypeを取得する

        :return:
        :rtype: numpy.dtype | None
        """

    @dtypes.setter
    def dtypes(self, dtype: DTypeLike | None) -> np.dtype | None:
        """
        配列のdtypeを設定する

        :param dtype: 配列のdtypeを指定する
        :type dtype: DTypeLike | None
        :return:
        :rtype: numpy.dtype | None
        """

    @property
    def min_ndim(self) -> int | None:
        """配列オブジェクトが許容する最小次元数を返す"""

    @property
    def max_ndim(self) -> int | None:
        """配列オブジェクトが許容する最大次元数を返す"""

    def to_1d(self) -> NPDate:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :return: フラット化した配列オブジェクトを返す
        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """

    def lengtharange(self) -> NPDate:
        """
        配列オブジェクトと同じ`shape`を持つ,各軸の最終次元インデックスの配列を返す

        `dtype`は`np.uint64`に固定される

        :return: インデックス配列を返す
        """

    def shapesize(self, shapes: tuple[int, ...]) -> bool:
        """
        配列オブジェクトの`shape`が`shapes`と一致するかを確認する

        :param shapes: 比較する`shape`を指定する
        :type shapes: tuple[int, ...]
        :return: `shape`が一致する場合は`True`を返し,一致しない場合は`False`を返す
        :rtype: bool
        """

    def tonumpy(self) -> np.ndarray:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    def all_None(self) -> bool:
        """
        配列内の全要素が`None`かどうかを返す

        :return: 配列内の全要素が`None`の場合は`True`を返し,そうでなければ`False`を返す
        :rtype: bool
        """

    def any_None(self) -> bool:
        """
        配列内のいずれかの要素が`None`かどうかを返す

        :return: `None`の要素が1つでもある場合は`True`を返し,そうでなければ`False`を返す
        :rtype: bool
        """

    @classmethod
    def today(cls) -> NPDate:
        """現在日付(UTC時刻)を返す"""

    @classmethod
    def now(cls) -> NPDate:
        """現在時刻(UTC時刻)を返す"""

    def todatetime(self) -> np.ndarray[datetime, np.dtype[datetime]]:
        """
        配列内の日付を`datetime.datetime`に変換する"""

    def todate(self) -> np.ndarray[date, np.dtype[date]]:
        """
        配列内の日付を`datetime.date`に変換する"""

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
