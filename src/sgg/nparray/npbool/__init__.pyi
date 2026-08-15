from typing import Any, Literal, NoReturn, overload

import numpy as np

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPBool"]

class NPBool(_ArrayCommonMixin):
    """`np.ndarray`を継承したbool型の配列クラス"""

    __doc__: str
    _element_type: tuple[type[bool], type[np.bool_], type[np.bool]]
    _default_dtype: np.bool_
    @overload
    def __new__(
        cls,
        obj: sgt._ArrayLikeBool_co,
        /,
        dtype: sgt._BoolDTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPBool:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のbool型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.bool_ | np.bool | bool
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __new__(
        cls,
        obj: sgt._ArrayLikeBool_co,
        /,
        dtype: sgt._BoolDTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPBool:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のbool型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.bool_ | np.bool | bool
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __eq__(self, value: sgt._ArrayLikeBool_co | NPBool) -> NPBool: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ArrayLikeBool_co | NPBool) -> NPBool: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    def __invert__(self) -> NPBool:
        """配列内の真偽値を反転させる"""

    @overload
    def __getitem__(self, key: int | np.integer) -> np.bool | np.bool_:
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
    def __getitem__(self, key: slice) -> sgt.NDArray[np.bool | np.bool_]:
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

    @property
    def element_type(self) -> tuple[type[bool], type[np.bool_], type[np.bool]]:
        """NPBoolで許可されている型を取得する"""

    @property
    def TrueCount(self) -> int:
        """配列内の`True`の数を数える"""

    @property
    def FalseCount(self) -> int:
        """配列内の`False`の数を数える"""

    def all(self) -> bool:
        """全ての要素が`True`かを調べる"""

    def any(self) -> bool:
        """どれかの要素が`True`かを調べる"""

    def inversion(self) -> NPBool:
        """配列内の真偽値を反転させる"""

    @overload
    def astype(self, dtype: sgt._BoolDTypeLike, copy: bool = True) -> NPBool:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _BoolDTypeLike
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    def choice(
        self,
        size: sgt._ShapeInt | None = None,
        replace: bool = True,
        p: sgt._ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: sgt._Seed = None,
    ) -> sgt.RBool_:
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
    def types(self) -> type[np.bool | np.bool_]: ...
    @property
    def dtypes(self) -> np.dtype[np.bool | np.bool_]:
        """インスタンス生成時に確定したdtypeを取得する"""

    @property
    def kinds(self) -> Literal["b"]:
        """配列のデータ型の一般的な種類を識別する文字コードを返す"""

    @property
    def chars(self) -> Literal["b"]:
        """配列のデータ型固有の文字コードを返す"""

    @property
    def nums(self) -> Literal[0]:
        """配列のデータ型固有の番号を返す"""
