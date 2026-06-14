"""基本的な文字列操作をするモジュール"""

from collections.abc import Iterator
from types import NotImplementedType
from typing import Any, Literal

from _typeshed import Incomplete
import numpy as np
from numpy._typing import ArrayLike, DTypeLike, NDArray

from ..npArray import NPArray

__all__ = ["NPString"]

class NPString(NPArray):
    def __init__(
        self,
        data: ArrayLike,
        dtype: DTypeLike = np.str_,
        depth_limit: int | None = None,
    ) -> None:
        """
        :param data: データの配列を指定する
        :type data: ArrayLike
        :param dtype: numpyの配列で指定する型を指定する
        :type dtype: DTypeLike|None
        :param depth_limit: 配列の最大の深さを指定する
        :type depth_limit: int|None
        """

    def __getitem__(self, key: int) -> Any: ...
    def __contains__(self, item: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __reversed__(self) -> NPString:
        """`numpy.fliplr`を実行する"""

    def __array__(
        self, dtype: DTypeLike | None = None, copy: bool | np._CopyMode | None = None
    ) -> np.ndarray: ...
    def __repr__(self) -> str: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: Literal["__call__", "reduce", "reduceat", "accumulate", "outer", "at"],
        *args: Any,
        **kwargs: Any,
    ) -> Any | NotImplementedType | NPString: ...
    def __add__(self, other: np.ndarray | NPString) -> NPString: ...
    def __mul__(self, other: int) -> NPString:
        """
        配列内の要素を`other`回付け加える

        :raises TypeError: `other`に`int`型以外で指定した場合に発生させる
        """
    __radd__ = __add__
    __rmul__ = __mul__
    __iadd__ = __add__
    __imul__ = __mul__
    def __eq__(self, value: np.ndarray | NPString) -> np.ndarray[Incomplete]: ...
    def __ne__(self, value: np.ndarray | NPString) -> np.ndarray[Incomplete]: ...
    @property
    def T(self) -> NPString: ...
    def append(self, val: np.ndarray | NPString) -> NPString: ...
    def low(self) -> NPString:
        """アルファベットを小文字に変換する"""

    def upper(self) -> NPString:
        """アルファベットを大文字に変換する"""

    def stringlen(self) -> NDArray[np.int_]: ...
    def str_len(self) -> NDArray[np.int_]: ...
    def replace(self, old: str, new: str) -> NPString:
        """NPString内の`old`を`new`に置き換える"""

    def astype(self, dtype: DTypeLike | None) -> NPString:
        """`dtype`で指定された型に変更します"""

    def sort(self) -> NPString:
        """`data`にソートを実行する"""

    def first_pop(self) -> NPString:
        """配列の最初の要素のコピーをその配列の末尾に追加する"""

    def clear(self) -> NPString:
        """配列をクリアする"""

    def deep_add(self, val: int) -> NPString:
        """配列の深さを`val`分だけ追加する"""

    def deep_add(self, val: int) -> NPString:
        """配列の深さが`val`より低い場合,深さを`val`にする"""

    def reshape(self, size: tuple[int, ...]) -> NPString:
        """配列の形状を`size`で指定する"""

    def flatten(self) -> NPString:
        """配列を一次元に平坦にする"""
