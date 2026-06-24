"""フレームワーク全体で使用する型を設定しているモジュール"""

from typing import (Any, Callable, Collection, Literal, TypeAlias, TypeVar, Union,
                    overload)

import numpy as np
from numpy.typing import ArrayLike

__all__ = [
    "ArrayLike",
    "Any",
    "Callable",
    "Collection",
    "Literal",
    "TypeAlias",
    "TypeVar",
    "overload",
    "ArrayLikeNumber",
    "TypeArrayLikeNumber",
    "TypeArray2LikeNumber",
    "TypeArraysLikeNumber",
    "ArrayLikeString",
    "TypeArrayLikeString",
    "TypeArray2LikeString",
    "TypeArraysLikeString",
    "ArrayLikeNS",
    "TypeArrayLikeNS",
    "TypeArray2LikeNS",
    "TypeArraysLikeNS",
    "ColorType",
    "ColorTypeN",
]
# 色
ColorType: TypeAlias = str
ColorTypeN: TypeAlias = str | None
# 数値
ArrayLikeNumber = TypeVar("ArrayLikeNumber", bound=Union[np.generic, int, float])
TypeArrayLikeNumber: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeNumber]]
TypeArray2LikeNumber: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeNumber]]
TypeArraysLikeNumber: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeNumber]]
# 文字列
ArrayLikeString = TypeVar("ArrayLikeString", bound=Union[np.str_, str])
TypeArrayLikeString: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeString]]
TypeArray2LikeString: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeString]]
TypeArraysLikeString: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeString]]
# 数値+文字列
ArrayLikeNS = TypeVar("ArrayLikeNS", bound=Union[np.generic, int, float, np.str_, str])
TypeArrayLikeNS: TypeAlias = np.ndarray[tuple[int], np.dtype[ArrayLikeNS]]
TypeArray2LikeNS: TypeAlias = np.ndarray[tuple[int, int], np.dtype[ArrayLikeNS]]
TypeArraysLikeNS: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[ArrayLikeNS]]
