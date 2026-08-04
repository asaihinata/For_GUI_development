from typing import Any, Literal, overload

import numpy as np
from numpy._typing import _DTypeLike
from numpy.typing import NDArray

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPArray"]

class NPArray(_ArrayCommonMixin, np.ndarray):
    """`np.ndarray`を継承した型付き配列クラス"""

    _element_type: None
    _default_dtype: Literal["object"]
    @overload
    def __new__(
        cls,
        data: Any,
        /,
        dtype: _DTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: NPArray
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __new__(
        cls,
        data: Any,
        /,
        dtype: _DTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: NPArray
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @classmethod
    def full(
        fill_value: Any, shape: sgt._AnyShape, dtype: _DTypeLike | None = None
    ) -> NPArray:
        """指定された形状と配列の型を,`fill_value`で埋める"""

    @classmethod
    def sequential(cls, shape: sgt._AnyShape) -> NPArray:
        """
        連続した整数値を要素に持つ配列を生成する

        :param shape: 生成する配列の形状。各要素は正の整数でなければならない。
        :type shape: _AnyShape
        :returns: 連続値を持つ`NPArray`の配列
        :raises ShapeError: `shape`が正の整数のみで構成されていない場合に発生させる
        """

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPArray | Any:
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

    def __eq__(self, value: Any) -> NPArray: ...
    def __ne__(self, value: Any) -> NPArray: ...
    @property
    def element_type(self) -> None:
        """NPArrayで許可されている型を取得する"""

    def count_nonzero(
        self, axis: sgt.Typeaxis = None, keepdims: bool = False
    ) -> np.intp | NDArray[np.intp]:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: Typeaxis
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する。
        :type keepdims: bool
        """

    def EType(self) -> NPArray:
        """配列内の要素の型を調べる"""

    def numandserial(self) -> NPArray:
        """
        配列の`dtype`が数値型場合そのままの配列を返す。

        配列の`dtype`が数値型でない場合は連番を作成し返す。
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
