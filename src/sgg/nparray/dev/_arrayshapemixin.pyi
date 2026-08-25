from types import GenericAlias
from typing import (Any, Iterable, Iterator, Literal, LiteralString, Self,
                    overload)

import numpy as np
from numpy._typing import DTypeLike, NDArray, _DTypeLike, _ShapeLike

import sgg._typing as sgt

__all__ = ["_ArrayCommonMixin"]

class _ArrayCommonMixin(np.ndarray):
    """次元数制約(min_ndim/max_ndim)を持つ配列クラス向けの共通メソッド"""

    _min_ndim: int | None
    _max_ndim: int | None
    _dtype: _DTypeLike | None
    __doc__: str
    __name__: str
    def __dir__(self) -> Iterable[str]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> Self: ...
    @overload
    def __getitem__(self, key: sgt._IntScalar) -> Any:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`obj[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: int | np.integer
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """

    @overload
    def __getitem__(self, key: slice) -> NDArray[Any]:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`obj[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: slice
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """
    @overload
    def __getitem__(self, key: Any) -> Any:...

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

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> Self | Any:
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
        """

    def __array_finalize__(self, obj: np.ndarray | None) -> None:
        """スライスやview後もdtypeや次元数情報を引き継がさせるメソッド"""

    def __iter__(
        self,
    ) -> Iterator[np._ScalarNotObject | np.ndarray[np._AnyShape, np._dtype] | Any]: ...
    @overload
    def __array__(
        self, dtype: None = None, /, *, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT_co]: ...
    @overload
    def __array__[DTypeT: np.dtype](
        self, dtype: DTypeT, /, *, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co, DTypeT]: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
    @classmethod
    def _resolve_dtype(cls, dtype: np.dtype | str | type | None) -> np.dtype | None: ...
    @classmethod
    def _validate_ndim(
        cls,
        obj: np.ndarray,
        min_ndim: int | None,
        max_ndim: int | None,
    ) -> None:
        """
        配列の次元数がmin_ndim・max_ndimの範囲内か検証する

        :param obj: 検証対象の配列を指定する
        :type obj: ndarray
        :param min_ndim: 許可する最小次元数を指定する。Noneの場合は制約なし
        :type min_ndim: int | None
        :param max_ndim: 許可する最大次元数を指定する。Noneの場合は制約なし
        :type max_ndim: int | None
        :raises ValueError: 次元数(ndim)がmin_ndim<=ndim<=max_ndimの範囲外の場合に発生させる
        """

    @classmethod
    def _validate_elements(cls, obj: np.ndarray) -> None:
        """
        配列内の要素が`_element_type`と一致するか検証する

        :param obj: 検証対象の配列を指定する
        :type obj: ndarray
        :raises TypeError: 許可されていない型の要素が含まれる場合に発生させる
        """

    def lengtharange(self) -> sgt.RUInt64:
        """配列オブジェクトと同じ`shape`を持つ,各軸の最終次元インデックスの配列を返す"""

    def shapesize(self, shapes: _ShapeLike) -> bool:
        """
        配列オブジェクトの`shape`が`shapes`と一致するかを確認する

        :param shapes: 比較する`shape`を指定する
        :type shapes: int | tuple[int, ...]
        """

    def reshape(self, shape: _ShapeLike) -> Self:
        """配列の形状を`shape`に変更する

        :param shape: 変更したい形状を指定する
        :type shape: int | tuple[int, ...]
        """

    def ravel(self, order: sgt._orderKACF = "C") -> Self:
        """連続した平坦化された配列を返す"""

    def tolist(self) -> Any | sgt.NestedList: ...
    def tonumpy(self, copy: bool | None = None) -> NDArray[Any]:
        """配列オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def typeconversion(
        self,
        type: DTypeLike,
        casting: Literal[
            "no", "equiv", "safe", "same_kind", "same_value", "unsafe"
        ] = "safe",
    ) -> bool:
        """
        配列の型が`type`で指定された型に変換可能か調べる

        :param type: 型変換先のデータ型を指定する
        :type type: DTypeLike
        :param casting: どのようなデータ変換が行われるか指定する
        :type casting: Literal["no", "equiv", "safe", "same_kind", "same_value", "unsafe"]
        """

    def unique(self) -> NDArray[Any]:
        """配列の固有要素を見つける"""

    def counts(self) -> tuple[NDArray[Any], NDArray[np.intp]]:
        """配列内の要素とその要素が配列内に存在する個数を返す"""

    def roll(self, shift: _ShapeLike, axis: _ShapeLike | None = None) -> Self:
        """
        要素を指定された軸に沿って回転させる

        :param shift: 要素を移動させる位置の数を指定する
        :type shift: _ShapeLike
        :param axis: 要素を移動させる軸を指定する
        :type axis: _ShapeLike | None
        """

    def rot90(self, k: int = 1, axes: tuple[int, int] = (0, 1)) -> Self:
        """
        指定された軸の平面内で配列を90度回転させる

        :param k: 配列に90度回転させたい回数を指定する
        :type k: int
        :param axes: 平面内で回転される軸を指定する
        :type axes: tuple[int, int]
        :return: 回転させた配列を返す
        """

    def to_1d(self) -> Self:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """

    @property
    def __array_priority__(self) -> float: ...
    @property
    def element_type(self) -> tuple[type, ...] | None:
        """許可されている型を取得する(各サブクラスで戻り値の型を絞り込む想定)"""

    @property
    def data(self) -> NDArray[Any]:
        """配列オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def min_ndim(self) -> int | None:
        """配列オブジェクトが許容する最小次元数を返す"""

    @property
    def max_ndim(self) -> int | None:
        """配列オブジェクトが許容する最大次元数を返す"""

    @property
    def zero_ndim(self) -> bool:
        """配列の次元数が0の時にTrueを返す"""

    @property
    def one_ndim(self):
        """配列の次元数が1の時にTrueを返す"""
    # dtype
    @property
    def types(self) -> type[np.generic | Any]: ...
    @property
    def dtypes(self) -> np.dtype | None:
        """インスタンス生成時に確定したdtypeを取得する"""

    @property
    def kinds(self) -> np._DTypeKind:
        """配列のデータ型の一般的な種類を識別する文字コードを返す"""

    @property
    def chars(self) -> np._DTypeChar:
        """配列のデータ型固有の文字コードを返す"""

    @property
    def nums(self) -> np._DTypeNum:
        """配列のデータ型固有の番号を返す"""

    @property
    def strs(self) -> LiteralString:
        """データ型の配列プロトコル型文字列を返す"""

    @property
    def names(self) -> LiteralString:
        """データ型を表すビット幅名を返す"""

    @property
    def itemsizes(self) -> int:
        """データ型の容量を返す"""
