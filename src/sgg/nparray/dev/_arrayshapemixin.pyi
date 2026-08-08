from types import GenericAlias
from typing import Any, Iterator, Literal, Self, overload

import numpy as np
from numpy._typing import DTypeLike, _ArrayLikeFloat_co, _ShapeLike
from numpy.typing import NDArray

from sgg.typing import _Seed,RUInt64

__all__ = ["_ArrayCommonMixin"]

class _ArrayCommonMixin(np.ndarray):
    """次元数制約(min_ndim/max_ndim)を持つ配列クラス向けの共通メソッド"""

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> Self: ...
    @overload
    def __getitem__(self, key: int) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> np.ndarray: ...
    def __getitem__(self, key: int | slice) -> Any | np.ndarray:
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
        :rtype: Any | np.ndarray
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
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
    def lengtharange(self) -> RUInt64:
        """配列オブジェクトと同じ`shape`を持つ,各軸の最終次元インデックスの配列を返す"""

    def shapesize(self, shapes: tuple[int, ...]) -> bool:
        """
        配列オブジェクトの`shape`が`shapes`と一致するかを確認する

        :param shapes: 比較する`shape`を指定する
        :type shapes: tuple[int, ...]
        :return: `shape`が一致する場合は`True`を返し,一致しない場合は`False`を返す
        :rtype: bool
        """

    def tonumpy(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def _resolve_dtype(
        cls,
        dtype: np.dtype | str | type | None,
    ) -> np.dtype | None:
        """
        引数`dtype`を解決させる

        :param dtype: ユーザーが指定するdtypeを指定する
        :return: 解決された`dtype`を返す
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

        :param obj: 検証対象の配列を指定する
        :raises TypeError: 許可されていない型の要素が含まれる場合に発生させる
        """

    @property
    def element_type(self) -> tuple[type, ...] | None:
        """許可されている型を取得する(各サブクラスで戻り値の型を絞り込む想定)"""

    @property
    def data(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def dtypes(self) -> np.dtype | None:
        """
        インスタンス生成時に確定したdtypeを取得する

        :return:
        :rtype: numpy.dtype | None
        """

    @property
    def min_ndim(self) -> int | None:
        """配列オブジェクトが許容する最小次元数を返す"""

    @property
    def max_ndim(self) -> int | None:
        """配列オブジェクトが許容する最大次元数を返す"""

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

    def isscalar(self) -> bool:
        """配列がスカラー値かを調べる"""

    def choice(
        self,
        size: int | tuple[int, ...] | None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: _Seed = None,
    ) -> np.ndarray:
        """
        配列の要素もしくは軸の配列をランダムに抽選する

        :param size: 出力する配列の形状を指定する
        :type size: int | tuple[int,...] | None
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
        :rtype: np.ndarray
        """

    def to_1d(self) -> Self:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :return: フラット化した配列オブジェクトを返す
        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """
