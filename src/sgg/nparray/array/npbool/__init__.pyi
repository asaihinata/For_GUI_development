from typing import Any, Iterator

import numpy as np
from numpy.typing import DTypeLike

from ....typing import TypeArraysLikeBool
from ..nparray import NPArray

__all__ = ["NPBool"]

class NPBool:
    def __new__(
        cls,
        data: TypeArraysLikeBool,
        dtype: DTypeLike | None = np.bool_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPBool: ...
    @classmethod
    def __instancecheck__(cls, instance: Any) -> bool: ...
    def __ne__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __iter__(self) -> Iterator[bool]: ...
    def __getitem__(self, key: int) -> bool:
        """インデックスアクセスをカスタマイズする

        intキーの場合は1次元に展開してからアクセスし,範囲外のインデックスはモジュロで折り返す

        :param key: インデックスまたはスライスを指定する
        :type key: int
        :return: インデックスに対応する要素を返す
        :rtype: bool
        :raises IndexError: 配列が空の場合に発生させる
        """

    @property
    def data(self) -> np.ndarray:
        """`NPBool`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def tonumpy(self) -> np.ndarray:
        """`NPBool`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def all(self) -> np.bool[bool]: ...
    def any(self) -> np.bool[bool]: ...
