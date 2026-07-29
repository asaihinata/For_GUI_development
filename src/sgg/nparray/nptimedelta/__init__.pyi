"""基本的な時間の差や期間について操作するモジュール"""

from datetime import timedelta
from types import GenericAlias
from typing import Any, Iterator, Self, TypeVar, overload,Never

import numpy as np
import numpy._typing as npt
from numpy import timedelta64,dtype

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool

__all__ = ["NPTimedelta"]
_DType = TypeVar(
    "_DType", bound=np.timedelta64, default=np.timedelta64[int], covariant=True
)
type NDTimedelta[ScalarT]=NPTimedelta[sgt._AnyShape, dtype[ScalarT]]
class NPTimedelta[_ShapeT: sgt._ArrayLikeTD64_co, _Dtypes: _DType](
    _ArrayCommonMixin, np.ndarray[_ShapeT, dtype[_Dtypes]]
):

    _element_type: tuple[type[np.timedelta64]]
    _default_dtype: type[dtype[np.timedelta64]]
    @overload
    def __new__[ShapeT: sgt._ArrayLikeNone_co](
        cls,
        data: ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta[ShapeT, dtype[timedelta64[None]]]: ...
    @overload
    def __new__[ShapeT: sgt._ArrayLikeNone_co](
        cls,
        data: ShapeT,
        /,
        dtype: np._TimeUnitSpec[np._IntTD64Unit],
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta[ShapeT, dtype[timedelta64[None]]]: ...
    @overload
    def __new__[ShapeT: sgt._ArrayLikeTD64Int_co](
        cls,
        data: ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta[ShapeT, dtype[timedelta64[int]]]: ...
    @overload
    def __new__[ShapeT: sgt._ArrayLikeTD64Int_co](
        cls,
        data: ShapeT,
        /,
        dtype: np._TimeUnitSpec[np._IntTD64Unit],
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta[ShapeT, dtype[timedelta64[int]]]: ...
    @overload
    def __new__[ShapeT: sgt._ArrayLikeTD64_co](
        cls,
        data: ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta[ShapeT, dtype[timedelta64[timedelta]]]: ...
    @overload
    def __new__[ShapeT: sgt._ArrayLikeTD64_co](
        cls,
        data: ShapeT,
        /,
        dtype: np._TimeUnitSpec[np._NativeTD64Unit],
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta[ShapeT, dtype[timedelta64[timedelta]]]: ...
    def __new__() -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

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

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPTimedelta | Any:
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
    def __array__[DType: np._dtype | sgt._DTypeLike[np.generic]](
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

    def __eq__(self, value: Any) -> NPBool[sgt._AnyShape, dtype[np.bool_]]: ...
    def __ne__(self, value: Any) -> NPBool[sgt._AnyShape, dtype[np.bool_]]: ...
    @overload
    def __add__(
        self: NPTimedelta[_ShapeT, np.dtype[timedelta64[Never]]], value: NDTimedelta[int | timedelta]|timedelta64[int | timedelta]
    ) -> NPTimedelta[_ShapeT,dtype[timedelta64]]: ...
    __iadd__ = __add__
    __radd__ = __add__
    def __mul__(self, i: npt._ArrayLikeInt_co) -> NPTimedelta:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: int
        """
    __imul__ = __mul__
    __rmul__ = __mul__

    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _Dtypes]]: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
    @property
    def element_type(self) -> tuple[type[np.timedelta64]]:
        """NPTimedeltaで許可されている型を取得する"""
