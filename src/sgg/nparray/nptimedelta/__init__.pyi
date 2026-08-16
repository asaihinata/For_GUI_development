"""基本的な時間の差や期間について操作するモジュール"""

from datetime import timedelta
from typing import Any, Literal, NoReturn, overload

import numpy as np
from numpy import dtype, timedelta64
from numpy._typing import NDArray, _DTypeLike

import sgg._typing as sgt

from ..dev import _ArrayCommonMixin
from ..npdate import NPDate

__all__ = ["NPTimedelta"]

class NPTimedelta(_ArrayCommonMixin):
    """`np.ndarray`を継承したtimedelta64型の配列クラス"""

    __doc__: str
    _element_type: timedelta64
    _default_dtype: dtype[timedelta64[timedelta]]
    @overload
    def __new__(
        cls,
        obj: sgt._ArrayLikeTD64_co,
        /,
        dtype: sgt._DtypeLikeTD = "timedelta64[D]",
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のtimedelta64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.timedelta64 | _TD64Codes_All
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
        obj: sgt._ArrayLikeTD64_co,
        /,
        dtype: sgt._DtypeLikeTD = "timedelta64[D]",
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPTimedelta:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のtimedelta64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: np.timedelta64 | _TD64Codes_All
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
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
    def __add__(self, value: sgt._ArrayLikeTD64_co | NPTimedelta) -> NPTimedelta: ...
    @overload
    def __add__(self, value: Any) -> NoReturn: ...
    __radd__ = __add__
    @overload
    def __sub__(self, value: sgt._ArrayLikeTD64_co | NPTimedelta) -> NPTimedelta: ...
    @overload
    def __sub__(
        self, value: NDArray[np.datetime64] | np.datetime64 | NPDate
    ) -> sgt.RDatetime64: ...
    @overload
    def __sub__(self, value: Any) -> NoReturn: ...
    __rsub__ = __sub__
    @overload
    def __mul__(self, value: NPTimedelta) -> NoReturn: ...
    @overload
    def __mul__(self, value: sgt._ArrayLikeInt_co) -> NPTimedelta: ...
    @overload
    def __mul__(self, value: Any) -> NoReturn: ...
    @overload
    def __truediv__(self, value: timedelta64 | NPTimedelta) -> sgt.RNumber: ...
    @overload
    def __truediv__(self, value: sgt._RealNumeric_co) -> NPTimedelta: ...
    @overload
    def __truediv__(self, value: Any) -> NoReturn: ...
    @overload
    def __getitem__(self, key: sgt._IntScalar) -> timedelta64:
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
    def __getitem__(self, key: slice) -> sgt.NDArray[timedelta64]:
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
    def element_type(self) -> tuple[type[timedelta64]]:
        """NPTimedeltaで許可されている型を取得する"""

    @overload
    def astype(self, dtype: sgt._DtypeLikeTD, copy: bool = True) -> NPTimedelta:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _DtypeLikeTD
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype[ScalarT: np.generic](
        self, dtype: _DTypeLike[ScalarT], copy: bool = True
    ) -> NDArray[ScalarT]:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _DTypeLike[ScalarT]
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype(self, dtype: sgt.DTypeNLike, copy: bool = True) -> NDArray[Any]:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: DTypeLike | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    def tonumpy(self, copy: bool | None = None) -> sgt.NDTimedelta64:
        """配列オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def full(
        cls,
        fill_value: sgt._TD64Scalar,
        shape: sgt._ShapeInt,
        dtype: sgt._DtypeLikeTD | None = None,
    ) -> NPTimedelta:
        """
        指定された形状と配列の型で`fill_value`で埋められた配列のオブジェクトを返す

        :param fill_value: 配列内に埋めるスカラー値を指定する
        :type fill_value: _TD64Scalar
        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DtypeLikeTD | None
        :raises ValueError: `fill_value`にスカラー値で指定しなかった場合に発生させる
        :raises ShapeError: `shape`で正しい値ではない場合に発生させる
        """

    def choice(
        self,
        size: sgt._ShapeInt | None = None,
        replace: bool = True,
        p: sgt._ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: sgt._Seed = None,
    ) -> sgt.RTimedelta64:
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
