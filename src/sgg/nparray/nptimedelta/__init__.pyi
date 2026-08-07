"""基本的な時間の差や期間について操作するモジュール"""

from typing import Any, NoReturn, overload

import numpy as np
from numpy import dtype, timedelta64
from numpy.typing import NDArray

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPTimedelta"]

class NPTimedelta(_ArrayCommonMixin, np.ndarray):
    _element_type: tuple[type[timedelta64]]
    _default_dtype: type[dtype[timedelta64]]
    @overload
    def __new__(
        cls,
        data: sgt._ArrayLikeTD64_co,
        /,
        dtype: sgt._DtypeLikeTD = "timedelta64[D]",
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意のtimedelta64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.timedelta64 | _TD64Codes_All
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
        data: sgt._ArrayLikeTD64_co,
        /,
        dtype: sgt._DtypeLikeTD = "timedelta64[D]",
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意のtimedelta64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.timedelta64 | _TD64Codes_All
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

    def __int__(self) -> int | NoReturn: ...
    def __float__(self) -> float | NoReturn: ...
    def __neg__(self) -> NPTimedelta: ...
    def __pos__(self) -> NPTimedelta: ...
    def __abs__(self) -> NPTimedelta: ...
    @overload
    def __eq__(self, value: sgt._ArrayLikeTD64_co | NPTimedelta) -> NPBool: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ArrayLikeTD64_co | NPTimedelta) -> NPBool: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    @overload
    def __add__(
        self, value: int | timedelta64 | NDArray[timedelta64] | NPTimedelta
    ) -> NPTimedelta: ...
    @overload
    def __add__(self, value: Any) -> NoReturn: ...
    __radd__ = __add__
    @overload
    def __sub__(
        self, value: int | timedelta64 | NDArray[timedelta64] | NPTimedelta
    ) -> NPTimedelta: ...
    @overload
    def __sub__(self, value: Any) -> NoReturn: ...
    __rsub__ = __sub__
    @overload
    def __mul__(self, value: sgt._IntLike_co | float | np.floating) -> NPTimedelta: ...
    @overload
    def __mul__(self, value: Any) -> NoReturn: ...
    @overload
    def __truediv__(self, value: sgt._RealNumeric_co) -> NPTimedelta: ...
    @overload
    def __truediv__(self, value: timedelta64 | NPTimedelta) -> NPNumber: ...
    @overload
    def __truediv__(self, value: Any) -> NoReturn: ...
    @property
    def element_type(self) -> tuple[type[timedelta64]]:
        """NPTimedeltaで許可されている型を取得する"""
