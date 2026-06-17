from collections.abc import Iterator
from types import NotImplementedType
from typing import Any, Literal

from numpy import _CopyMode, _ScalarT, dtype, ndarray, ufunc
from numpy._typing import ArrayLike, DTypeLike

__all__ = ["NPArray", "is_array_like", "change_array_like"]

def is_array_like(obj: ndarray | list | tuple | range) -> bool:
    """配列もしくは__array__を持つオブジェクトを判定する"""

def change_array_like(obj: ndarray | list | tuple | range) -> bool:
    """NumPyの`array`に変換できるかを判定する"""

class NPArray:
    def __init__(
        self,
        data: ArrayLike,
        dtype: DTypeLike | None = None,
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
    # 親クラス,子クラス共通の特殊メソッド
    def __getitem__(self, key: int) -> Any: ...
    def __contains__(self, item: Any) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __array__(
        self, dtype: DTypeLike | None = None, copy: bool | _CopyMode | None = None
    ) -> ndarray: ...
    def __reversed__(self) -> NPArray:
        """`numpy.fliplr`を実行する"""
    # 以下の特殊メソッドはそれぞれの子クラス毎に処理を変更する必要がある
    def __repr__(self) -> str: ...
    def __array_ufunc__(
        self,
        ufunc: ufunc,
        method: Literal["__call__", "reduce", "reduceat", "accumulate", "outer", "at"],
        *args: Any,
        **kwargs: Any,
    ) -> Any | NotImplementedType | NPArray: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def T(self) -> NPArray: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    @property
    def size(self) -> int: ...
    @property
    def dtype(self) -> DTypeLike: ...
    @property
    def data(self) -> ndarray: ...
    @data.setter
    def data(self, datas: ArrayLike) -> NPArray: ...
    def shapesize(self, shapes: tuple[int, ...]) -> bool:
        """
        配列の形状が指定した`shapes`の形状と一致するか調べる

        :param shape: 形状を指定する
        :type shape: tuple[int,...]
        """

    def astype(self, dtype: DTypeLike | None) -> NPArray:
        """`dtype`で指定された型に変更します"""

    def sort(self) -> NPArray:
        """`data`にソートを実行する"""

    def first_pop(self) -> NPArray:
        """配列の最初の要素のコピーをその配列の末尾に追加する"""

    def clear(self) -> NPArray:
        """配列をクリアする"""

    def deep_add(self, val: int) -> NPArray:
        """配列の深さを`val`分だけ追加する"""

    def deep_add(self, val: int) -> NPArray:
        """配列の深さが`val`より低い場合,深さを`val`にする"""

    def reshape(self, size: tuple[int, ...]) -> NPArray:
        """配列の形状を`size`に変換する"""

    def flatten(self) -> NPArray:
        """配列を一次元に平坦にする"""

    def first_element(self) -> Any:
        """`NPArray`の最初の要素を取得する"""

    def tolist(self) -> list:
        """list型にして返す"""

    def tonp(self, dtype: DTypeLike = "none") -> ndarray:
        """配列をNumPyの`ndarray`に変換する"""

    def lengtharange(
        self, start: int = 0, dtype: DTypeLike | None = None
    ) -> ndarray: ...
    def _flatten(
        self,
    ) -> tuple[ndarray[tuple[int], dtype[_ScalarT]], tuple[int, ...]]: ...
    def dimension(self) -> bool:
        """`NPArray`の次元が1次元か判定する"""

    def dimensions(self) -> bool:
        """`NPArray`の次元が多次元か判定する"""

    def get(self, val: int) -> Any:
        """配列の`val`番目の要素を取得する"""

    def all_None(self) -> bool:
        """全ての要素がNoneかを調べる"""

    def all_None(self) -> bool:
        """要素内にNoneが存在するかを調べる"""
