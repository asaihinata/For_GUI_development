from typing import Any, overload

import numpy as np
from numpy._typing import _DTypeLike

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPArray"]

class NPArray(_ArrayCommonMixin):
    """`np.ndarray`を継承した型付き配列クラス"""

    __doc__: str
    _element_type: None
    _default_dtype: str = "object"
    @overload
    def __new__(
        cls,
        obj: Any,
        /,
        dtype: _DTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: dtype | type
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
        obj: Any,
        /,
        dtype: _DTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: dtype | type
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __eq__(self, value: Any) -> NPArray: ...
    def __ne__(self, value: Any) -> NPArray: ...
    @property
    def element_type(self) -> None:
        """NPArrayで許可されている型を取得する"""

    @classmethod
    def full(
        fill_value: Any, shape: sgt._ShapeInt, dtype: _DTypeLike | None = None
    ) -> NPArray:
        """
        指定された形状と配列の型で,`fill_value`で埋める

        :param fill_value: 配列内に埋めるスカラー値を指定する
        :type fill_value: スカラー値
        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DTypeLike | None
        """

    @classmethod
    def sequential(cls, shape: sgt._ShapeInt) -> NPArray:
        """
        連続した整数値を要素に持つ配列を生成する

        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        :returns: 連続値を持つNPArrayの配列を返す
        :rtype: NPArray
        """

    def count_nonzero(
        self, axis: sgt._ShapeLike | None = None, keepdims: bool = False
    ) -> NPArray:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: int | tuple[int, ...] | None
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する
        :type keepdims: bool
        """

    def EType(self) -> NPArray:
        """配列内の要素の型を調べる"""

    @overload
    def astype[ScalarT: np.generic](
        self, dtype: _DTypeLike[ScalarT], copy: bool = True
    ) -> NPArray:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _DTypeLike[generic]
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype(self, dtype: np.DTypeLike | None, copy: bool = True) -> NPArray:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: DTypeLike | None
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
    ) -> sgt.RAny:
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
