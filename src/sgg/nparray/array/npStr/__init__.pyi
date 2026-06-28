"""基本的な文字列の操作をするモジュール"""

from typing import Any, Iterator

import numpy as np
from numpy._typing import ArrayLike, DTypeLike

from ....typing import TypeArraysLikeString
from ..nparray import NPArray
from ..npnumber import NPNumber

__all__ = ["NPString"]

class NPString(NPArray):
    def __new__(
        cls,
        data: TypeArraysLikeString,
        dtype: DTypeLike = np.str_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPString: ...
    @property
    def data[T](self: T) -> np.ndarray[T]:
        """`NPString`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def tonumpy[T](self: T) -> np.ndarray[T]:
        """`NPString`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def __instancecheck__(cls, instance: Any) -> bool: ...
    def __iter__(self) -> Iterator[np.character]: ...
    def __getitem__(self, key: int) -> np.character:
        """インデックスアクセスをカスタマイズする

        intキーの場合は1次元に展開してからアクセスし,範囲外のインデックスはモジュロで折り返す

        :param key: インデックスまたはスライスを指定する
        :type key: int
        :return: インデックスに対応する要素を返す
        :rtype: np.character
        :raises IndexError: 配列が空の場合に発生させる
        """

    def __add__(self, other: ArrayLike) -> NPString: ...
    def __radd__(self, other: ArrayLike) -> NPString: ...
    def __iadd__(self, other: ArrayLike) -> NPString: ...
    def __mul__(self, i: int) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: int
        :raises TypeError: `i`に`int`型以外を指定した場合に発生させる
        """

    def __rmul__(self, other: int) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: int
        :raises TypeError: `i`に`int`型以外を指定した場合に発生させる
        """

    def __imul__(self, other: int) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: int
        :raises TypeError: `i`に`int`型以外を指定した場合に発生させる
        """

    def __eq__(self, value: Any) -> Any: ...
    def __ne__(self, value: Any) -> Any: ...
    def append(self, val: Any) -> NPString:
        """配列内の要素の文字に`val`を付け加える"""

    def low(self) -> NPString:
        """`NPString`内の要素のアルファベットを小文字に変換する"""

    def upper(self) -> NPString:
        """`NPString`内の要素のアルファベットを大文字に変換する"""

    def stringlen(self) -> NPNumber:
        """配列内の要素の文字の長さを求める"""

    def str_len(self) -> NPNumber:
        """配列内の要素の文字の長さを求める"""

    def replace(self, old: str, new: str) -> NPString:
        """`NPString`内の要素の文字列の`old`を`new`に置き換える"""
