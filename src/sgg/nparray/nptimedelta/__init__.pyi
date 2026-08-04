"""基本的な時間の差や期間について操作するモジュール"""

from typing import Any, Iterator

import numpy as np
from numpy import dtype, timedelta64

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool

__all__ = ["NPTimedelta"]

class NPTimedelta(_ArrayCommonMixin, np.ndarray):
    _element_type: tuple[type[timedelta64]]
    _default_dtype: type[dtype[timedelta64]]
    def __new__(
        cls,
        data: sgt._ArrayLikeTD64_co,
        /,
        dtype: sgt._AllTimeUnit = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta:
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
        :rtype: NPTimedelta
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

    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __neg__(self) -> NPTimedelta: ...
    def __pos__(self) -> NPTimedelta: ...
    def __abs__(self) -> NPTimedelta: ...
    def __eq__(self, value: Any) -> NPBool: ...
    def __ne__(self, value: Any) -> NPBool: ...
    def __add__(self, value: Any) -> NPTimedelta: ...
    __radd__ = __add__
    def __sub__(self, value: Any) -> NPTimedelta: ...
    __rsub__ = __sub__
    def __mul__(
        self, value: sgt._IntLike_co | float | np.floating, /
    ) -> NPTimedelta: ...
    def __truediv__(self, value: sgt._IntLike_co) -> NPTimedelta: ...
    def __iter__(self) -> Iterator[np.ndarray]: ...
    @property
    def element_type(self) -> tuple[type[timedelta64]]:
        """NPTimedeltaで許可されている型を取得する"""

    def to_1d(self) -> NPTimedelta:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :return: フラット化した配列オブジェクトを返す
        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """
