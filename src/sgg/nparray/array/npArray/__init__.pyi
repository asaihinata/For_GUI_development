from typing import Any, Iterator, Literal, Self, overload

import numpy as np
from numpy.typing import DTypeLike, NDArray

from sgg.typing import Incomplete, _DTypeT, _ShapeT

from ..dev import _ArrayShapeMixin

__all__ = ["NPArray"]

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPArray(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承した型付き配列クラス"""

    _element_type: None
    _default_dtype: Literal["object"]

    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPArray[_ShapeT, np.dtype[Any]]: ...
    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: type[np.generic],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPArray[_ShapeT, np.dtype[np.generic]]: ...
    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: np.dtype[_DTypeT],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPArray[_ShapeT, _DTypeT]: ...
    def __new__(
        cls,
        data: _ShapeT,
        dtype: DTypeLike | None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: ArrayLike
        :param dtype: 配列の型を指定する
        :type dtype: DTypeLike | None
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

    @classmethod
    def full(
        cls, fill_value: Any, shape: np._AnyShapeT, dtype: _DTypeT | None = None
    ) -> NPArray[np._AnyShapeT, _DTypeT]:
        """指定された形状と配列の型を,fill_valueで埋める"""

    @classmethod
    def sequential(
        cls, shape: np._AnyShapeT
    ) -> NPArray[np._AnyShapeT, np.dtype[np.uint64]]:
        """
        連続した整数値を要素に持つ配列を生成する

        :param shape: 生成する配列の形状。各要素は正の整数でなければならない。
        :type shape: _AnyShapeT
        :returns: 連続値を持つ`NPArray`の配列
        :rtype:
        :raises ShapeError: `shape`が正の整数のみで構成されていない場合に発生させる
        """

    def __class_getitem__(cls, item: Any) -> type[NPArray[Any, Any]]: ...
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

    @overload
    def __array__(
        self, dtype: None = None, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, _DTypeT]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, np._DTypeT]: ...
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

    def __ne__(self, other: Any) -> NPArray[Any, np.dtype[np.bool]]: ...
    def __eq__(self, other: Any) -> NPArray[Any, np.dtype[np.bool]]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> Self:
        """
        逆順にした新しい配列オブジェクトを返す

        :return: 全軸で反転した配列を返す
        """

    @overload
    def __getitem__(self, key: int) -> Any | None: ...
    @overload
    def __getitem__(self, key: slice) -> np.ndarray | None: ...
    def __getitem__(self, key: int | slice) -> Any | np.ndarray | None:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`data[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: int | slice
        :return: インデックスに対応する要素を返す
        :rtype: Any | np.ndarray | None
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """

    @property
    def element_type(self) -> None:
        """NPArrayで許可されている型を取得する"""

    def count_nonzero(
        self, axis: np._ShapeLike | None = None, keepdims: bool = False
    ) -> np.intp | NDArray[np.intp]:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: _ShapeLike | None
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する。
        :type keepdims: bool
        """

    def EType(self) -> NDArray[Incomplete]:
        """要素の型を調べる"""
