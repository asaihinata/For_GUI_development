"""基本的な文字列操作をするモジュール"""

from typing import Any

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
        dtype: DTypeLike | None = np.str_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPString: ...
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
    def append(self, val: Any) -> NPString: ...
    def low(self) -> NPString:
        """`NPString`内の要素のアルファベットを小文字に変換する"""

    def upper(self) -> NPString:
        """`NPString`内の要素のアルファベットを大文字に変換する"""

    def stringlen(self) -> NPNumber: ...
    def str_len(self) -> NPNumber: ...
    def replace(self, old: str, new: str) -> NPString:
        """`NPString`内の要素の文字列の`old`を`new`に置き換える"""
