"""基本的な計算をするモジュール"""

from collections.abc import Iterator
from types import NotImplementedType
from typing import Any, Literal

from _typeshed import Incomplete
from numpy import _CopyMode, float64, ndarray, ufunc
from numpy._typing import ArrayLike, DTypeLike

from ..npArray import NPArray

__all__ = ["NPNumber"]

class NPNumber(NPArray):
    def __init__(
        self,
        data: ArrayLike,
        dtype: DTypeLike = float64,
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
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> NPNumber:
        """`numpy.fliplr`を実行する"""

    def __array__(
        self, dtype: DTypeLike | None = None, copy: bool | _CopyMode | None = None
    ) -> ndarray: ...
    def __array_ufunc__(
        self,
        ufunc: ufunc,
        method: Literal["__call__", "reduce", "reduceat", "accumulate", "outer", "at"],
        *args: Any,
        **kwargs: Any,
    ) -> Any | NotImplementedType | NPNumber: ...
    def __abs__(self) -> NPNumber: ...
    def __add__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __sub__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __mul__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __truediv__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __iadd__ = __add__
    __isub__ = __sub__
    __imul__ = __mul__
    __itruediv__ = __truediv__
    def __eq__(self, value: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __ne__(self, value: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __lt__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __le__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __gt__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __ge__(self, other: ndarray | NPNumber) -> ndarray[Incomplete]: ...
    def __mod__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __floordiv__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    def __pow__(self, other: int | float | ndarray | NPNumber) -> NPNumber: ...
    @property
    def T(self) -> NPNumber: ...
    def sum(self):
        """配列の合計を求める"""

    def median(self): ...
    def var(self): ...
    def max(self): ...
    def min(self): ...
    def mean(self): ...
    def std(self): ...
    def pow2(self): ...
    def deviation(self):
        """標準偏差を求める"""

    def log(self): ...
    def log10(self): ...
    def log2(self): ...
    def log1p(self): ...
    def degree(self): ...
    def radian(self): ...
    def sturgesval(self) -> float64:
        """
        データ数からヒストグラムの階級数を求める(スタージェスの公式を使用)

        :return: スタージェスの公式で求めた値を返す
        :rtype: float64
        """

    def logx(self, x: int | float): ...
    def mod(self, x): ...
    def divmod(self, x): ...
    def pow(self, x) -> NPNumber: ...
    def sqrt(self, root: int | float = 2) -> NPNumber: ...
    def floor(self, digit: int | None = ...) -> NPNumber: ...
    def trunc(self, digit: int | None = ...) -> NPNumber: ...
    def ceil(self, digit: int | None = ...) -> NPNumber: ...
    def round(self, digit: int | None = ...) -> NPNumber: ...
    def cussum(self) -> NPNumber:
        """一つ前の元の値との和を求める"""

    def cumprod(self) -> NPNumber:
        """一つ前の元の値との積を求める"""

    def percentile(
        self,
        q: tuple[int, ...],
        axis: int | None = None,
        method: Literal[
            "inverted_cdf",
            "averaged_inverted_cdf",
            "closest_observation",
            "interpolated_inverted_cdf",
            "hazen",
            "weibull",
            "linear",
            "median_unbiased",
            "normal_unbiased",
        ] = "linear",
    ) -> ndarray: ...
    def quantile(
        self,
        q: tuple[int, ...],
        axis: int | None = None,
        method: Literal[
            "inverted_cdf",
            "averaged_inverted_cdf",
            "closest_observation",
            "interpolated_inverted_cdf",
            "hazen",
            "weibull",
            "linear",
            "median_unbiased",
            "normal_unbiased",
        ] = "linear",
    ) -> ndarray: ...
    def ratio(self, axis: int | None = None) -> ndarray:
        """行や列ごとの合計に対する比率を求める"""

    def zero_check(self) -> ndarray:
        """要素の数値が0の位置を探す"""

    def ints(self) -> NPNumber:
        """配列の型を`int`型にする"""

    def floats(self) -> NPNumber:
        """配列の型を`float`型にする"""

    def get_axis(self) -> int | None: ...
    def set_axis(self, axis: int | None) -> int | None: ...
    @property
    def axis(self) -> int | None: ...
    @axis.setter
    def axis(self, axis: int | None) -> int | None: ...
    def astype(self, dtype: DTypeLike | None) -> NPNumber:
        """`dtype`で指定された型に変更します"""

    def sort(self) -> NPNumber:
        """`data`にソートを実行する"""

    def first_pop(self) -> NPNumber:
        """配列の最初の要素のコピーをその配列の末尾に追加する"""

    def clear(self) -> NPNumber:
        """配列をクリアする"""

    def deep_add(self, val: int) -> NPNumber:
        """配列の深さを`val`分だけ追加する"""

    def deep_add(self, val: int) -> NPNumber:
        """配列の深さが`val`より低い場合,深さを`val`にする"""

    def reshape(self, size: tuple[int, ...]) -> NPNumber:
        """配列の形状を`size`で指定する"""

    def flatten(self) -> NPNumber:
        """配列を一次元に平坦にする"""
