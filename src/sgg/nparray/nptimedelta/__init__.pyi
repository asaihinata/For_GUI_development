"""基本的な時間の差や期間について操作するモジュール"""

from datetime import timedelta
from typing import Any, Literal, NoReturn, overload

import numpy as np
from numpy import dtype, timedelta64
from numpy.typing import NDArray

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npdate import NPDate

__all__ = ["NPTimedelta"]

class NPTimedelta(_ArrayCommonMixin):
    _element_type: timedelta64
    _default_dtype: dtype[timedelta64[timedelta]]
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
    def __eq__(self, value: sgt._ArrayLikeTD64_co | NPTimedelta) -> sgt.RBool_: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ArrayLikeTD64_co | NPTimedelta) -> sgt.RBool_: ...
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
    def __sub__(
        self, value: NDArray[np.datetime64] | np.datetime64 | NPDate
    ) -> sgt.Rdatetime64: ...
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
    def __truediv__(self, value: timedelta64 | NPTimedelta) -> sgt.RNumber: ...
    @overload
    def __truediv__(self, value: Any) -> NoReturn: ...
    @property
    def element_type(self) -> tuple[type[timedelta64]]:
        """NPTimedeltaで許可されている型を取得する"""

    def choice(
        self,
        size: sgt._ShapeInt | None = None,
        replace: bool = True,
        p: sgt._ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: sgt._Seed = None,
    ) -> sgt.Rtimedelta64:
        """
        配列の要素もしくは軸の配列をランダムに抽選する

        :param size: 出力する配列の形状を指定する
        :type size: int | tuple[int, ...] | None
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
    # dtype
    @property
    def types(self) -> type[timedelta64]: ...
    @property
    def dtypes(self) -> np.dtype[timedelta64]:
        """インスタンス生成時に確定したdtypeを取得する"""

    @property
    def dtypeunit(self) -> Literal[sgt._TimeStrUnit, "timedelta64"]: ...
    @property
    def kinds(self) -> Literal["m"]:
        """配列のデータ型の一般的な種類を識別する文字コードを返す"""

    @property
    def chars(self) -> Literal["m"]:
        """配列のデータ型固有の文字コードを返す"""

    @property
    def nums(self) -> Literal[22]:
        """配列のデータ型固有の番号を返す"""
