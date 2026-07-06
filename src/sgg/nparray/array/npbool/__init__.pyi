from typing import Any, Iterator, Self, TypeVar, overload

import numpy as np
from numpy._typing import _DTypeLikeBool, _ShapeLike
from numpy.typing import NDArray

from .._typing import _ArrayLikeBool_co, _ShapeT
from ..dev import _ArrayShapeMixin

__all__ = ["NPBool"]
HANDLED_FUNCTIONS: dict
_DTypeT = TypeVar("_DTypeT", bound=np.dtype, default=np.dtype[np.bool_], covariant=True)

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPBool(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承したbool型の配列クラス"""

    _element_type: tuple[type[bool], type[np.bool_], type[np.bool]]
    _default_dtype: type[np.bool_]

    @overload
    def __new__(
        cls,
        data: _ArrayLikeBool_co,
        dtype: None = np.bool_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeBool_co,
        dtype: _DTypeLikeBool,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    def __new__(
        cls,
        data: _ArrayLikeBool_co,
        dtype: _DTypeLikeBool | None = np.bool_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeBool_co
        :param dtype: 配列の型を指定する
        :type dtype: _DTypeLikeBool | None
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

    def __class_getitem__(cls, item: Any) -> type[NPBool[Any, Any]]: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPBool | Any:
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
    ) -> np.ndarray[np._ShapeT_co,]: ...
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

    def __ne__(self, other: Any) -> NPBool[Any, np.dtype[np.bool]]: ...
    def __eq__(self, other: Any) -> NPBool[Any, np.dtype[np.bool]]: ...
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
    def element_type(self) -> tuple[type[bool], type[np.bool_], type[np.bool]]:
        """NPBoolで許可されている型を取得する"""

    @property
    def data(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    def to_1d(self) -> NPBool:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :return: フラット化した配列オブジェクトを返す
        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """

    def roll(self, shift: _ShapeLike, axis: _ShapeLike | None = None) -> NPBool:
        """
        要素を指定された軸に沿って回転させる

        :param shift: 要素を移動させる位置の数を指定する
        :type shift: _ShapeLike
        :param axis: 要素を移動させる軸を指定する
        :type axis: _ShapeLike | None
        """

    def rot90(self, k: int = 1, axes: tuple[int, int] = (0, 1)) -> NPBool:
        """
        指定された軸の平面内で配列を90度回転させる

        :param k: 配列に90度回転させたい回数を指定する
        :type k: int
        :param axes: 平面内で回転される軸を指定する
        :type axes: tuple[int,int]
        :return: 回転させた配列を返す
        :rtype: NPBool
        """

    def all(self) -> bool:
        """全ての要素が`True`かを調べる"""

    def any(self) -> bool:
        """どれかの要素が`True`かを調べる"""

    def inversion(self) -> Self:
        """配列内の真偽値を反転させる"""
