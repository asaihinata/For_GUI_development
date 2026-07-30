"""基本的な数値の操作をするモジュール"""

from types import GenericAlias
from typing import (Any, Iterator, Literal, Self, Sequence, SupportsIndex,
                    TypeVar, overload)

import numpy as np
import numpy._typing as npt
from numpy import dtype
from numpy.typing import NDArray

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool

__all__ = ["NPNumber"]
_DTypeT = TypeVar(
    "_DTypeT", bound=np.generic, default=dtype[np.float64], covariant=True
)
type _ToFloat64 = float | np.integer | np.bool
type _ToArrayFloat64 = sgt._DualArrayLike[
    np.dtype[np.float64 | np.integer | np.bool], float
]
type _NDArrayLikeFloat = NDArray[np.generic[float]] | npt._NestedSequence[float]
type _ArrayF32 = NPNumber[sgt._ShapeLike, np.dtype[type[np.float32]]]
type _ArrayF64 = NPNumber[sgt._ShapeLike, np.dtype[type[np.float64]]]
type _OrderCF = Literal["C", "F"] | None
type _SortKind = Literal[
    "Q",
    "quick",
    "quicksort",
    "M",
    "merge",
    "mergesort",
    "H",
    "heap",
    "heapsort",
    "S",
    "stable",
    "stablesort",
]
type TYPEMETHOD = Literal[
    "inverted_cdf",
    "averaged_inverted_cdf",
    "closest_observation",
    "interpolated_inverted_cdf",
    "hazen",
    "weibull",
    "linear",
    "median_unbiased",
    "normal_unbiased",
]

class NPNumber[_ShapeT: sgt._ArrayLikeNumber_co, _Dtypes: _DTypeT](
    _ArrayCommonMixin, np.ndarray[_ShapeT, dtype[_Dtypes]]
):
    """`np.ndarray`を継承した数値型の配列クラス"""

    _element_type: tuple[type[int], type[float], type[complex], type[np.number]]
    _default_dtype: type[np.float64]

    @overload
    def __new__[_ShapeTs, _Dtype](
        cls,
        data: NPNumber[_ShapeTs, _Dtype],
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber[_ShapeTs, _Dtype]: ...
    @overload
    def __new__[Dtype: sgt._NumericDTypeLike](
        cls,
        data: NPNumber[_ShapeT, _Dtypes],
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber[_ShapeT, dtype[Dtype]]: ...
    @overload
    def __new__(
        cls,
        data: _ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber[_ShapeT, _DTypeT]: ...
    @overload
    def __new__[DType: sgt._NumericDTypeLike](
        cls,
        data: _ShapeT,
        /,
        dtype: DType,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber[_ShapeT, dtype[DType]]: ...
    def __new__() -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
    def __array_ufunc__[DType](
        self: NPNumber[_ShapeT, DType],
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPNumber[_ShapeT, DType] | Any:
        """
        NumPyのufuncの動作をカスタマイズする

        :param ufunc: 呼び出されたufunc
        :type ufunc: np.ufunc
        :param method: 呼び出しメソッド名
        :type method: str
        :param inputs: ufuncへの入力
        :type inputs: Any
        :param kwargs: ufuncへの追加引数
        :type kwargs: Any
        :return: 処理結果を返す
        """

    @overload
    def __array__(
        self, dtype: None = None, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, _Dtypes]: ...
    @overload
    def __array__[DType: np._dtype | sgt._DTypeLike[np.generic]](
        self, dtype: DType, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, DType]: ...
    def __array_function__(
        self,
        func: Any,
        types: Any,
        args: tuple,
        kwargs: dict,
    ) -> Any:
        """
        numpy関数の動作をカスタマイズする

        :param func: 呼び出されたnumpy関数
        :type func: Any
        :param types: 関連する型のコレクション
        :type types: Any
        :param args: 位置引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: 演算結果を返す
        :rtype: Any
        """

    def __eq__(self, value: Any) -> NPBool[_ShapeT, dtype[np.bool_]]: ...
    def __ne__(self, value: Any) -> NPBool[_ShapeT, dtype[np.bool_]]: ...
    def __lt__(self, value: Any) -> NPBool[_ShapeT, dtype[np.bool_]]: ...
    def __le__(self, value: Any) -> NPBool[_ShapeT, dtype[np.bool_]]: ...
    def __gt__(self, value: Any) -> NPBool[_ShapeT, dtype[np.bool_]]: ...
    def __ge__(self, value: Any) -> NPBool[_ShapeT, dtype[np.bool_]]: ...
    def __add__(self, value: Any) -> NPNumber: ...
    def __radd__(self, value: Any) -> NPNumber: ...
    def __iadd__(self, value: Any) -> NPNumber: ...
    def __sub__(self, value: Any) -> NPNumber: ...
    def __rsub__(self, value: Any) -> NPNumber: ...
    def __isub__(self, value: Any) -> NPNumber: ...
    def __mul__(self, value: Any) -> NPNumber: ...
    def __rmul__(self, value: Any) -> NPNumber: ...
    def __imul__(self, value: Any) -> NPNumber: ...
    def __truediv__(self, value: Any) -> NPNumber: ...
    def __rtruediv__(self, value: Any) -> NPNumber: ...
    def __itruediv__(self, value: Any) -> NPNumber: ...
    def __floordiv__(self, value: Any) -> NPNumber: ...
    def __rfloordiv__(self, value: Any) -> NPNumber: ...
    def __ifloordiv__(self, value: Any) -> NPNumber: ...
    def __mod__(self, value: Any) -> NPNumber: ...
    def __rmod__(self, value: Any) -> NPNumber: ...
    def __imod__(self, value: Any) -> NPNumber: ...
    def __pow__(self, value: Any) -> NPNumber: ...
    def __rpow__(self, value: Any) -> NPNumber: ...
    def __ipow__(self, value: Any) -> NPNumber: ...
    def __divmod__(self, value: Any) -> tuple[NPNumber, NPNumber]: ...
    def __rdivmod__(self, value: Any) -> tuple[NPNumber, NPNumber]: ...
    def __abs__(self) -> Self: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    @property
    def element_type(
        self,
    ) -> tuple[type[int], type[float], type[complex], type[np.number]]:
        """NPNumberで許可されている型を取得する"""

    @overload
    def count_nonzero(self, axis: None = None, keepdims: bool = False) -> np.intp: ...
    @overload
    def count_nonzero(
        self, axis: np._ShapeLike | None = None, keepdims: bool = True
    ) -> NDArray[np.intp]: ...
    def count_nonzero():
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: Typeaxis
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する。
        :type keepdims: bool
        """

    @property
    def sturgesval(self) -> np.floating:
        """スタージェスの公式を求める"""

    def cussum(self) -> NPNumber[_ShapeT, _DTypeT]:
        """一つ前の元の値との和を求める"""

    def cusdiff(self) -> NPNumber[_ShapeT, _DTypeT]:
        """一つ前の元の値との差を求める"""

    def cusprod(self) -> NPNumber[_ShapeT, _DTypeT]:
        """一つ前の元の値との積を求める"""

    def cusdiv(self) -> NPNumber[_ShapeT, _DTypeT]:
        """一つ前の元の値との除算を求める"""

    def percentile(
        self,
        q: npt._FloatLike_co,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[Any, dtype[np.float64]]:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: npt._FloatLike_co
        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def quantile(
        self,
        q: npt._FloatLike_co,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[Any, dtype[np.float64]]:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: npt._FloatLike_co
        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """
    @overload
    def ratio(self, axis: None=None) -> NPNumber[_ShapeT,np.dtype[np.float64]]:...
    @overload
    def ratio(self, axis: SupportsIndex) -> NPNumber[_ShapeT,np.dtype[np.float64]]:...
    def ratio():
        """行や列ごとの合計に対する比率を求める"""

    @overload
    @classmethod
    def zeros(
        cls,
        shape: SupportsIndex,
        dtype: None = None,
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def zeros[DTypeT: np.generic](
        cls,
        shape: SupportsIndex,
        dtype: type[DTypeT],
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], np.dtype[DTypeT]]: ...
    @overload
    @classmethod
    def zeros[ShapeT: npt._Shape](
        cls,
        shape: ShapeT,
        dtype: None = None,
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[ShapeT, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def zeros[ShapeT: npt._Shape, DTypeT: np.generic](
        cls,
        shape: ShapeT,
        dtype: type[DTypeT],
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[ShapeT, np.dtype[DTypeT]]: ...
    @classmethod
    def zeros():
        """指定された形状と型の新しい配列を0で埋めた配列を作成する"""

    @overload
    @classmethod
    def ones(
        cls,
        shape: SupportsIndex,
        dtype: None = None,
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def ones[DTypeT: np.generic](
        cls,
        shape: SupportsIndex,
        dtype: type[DTypeT],
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], np.dtype[DTypeT]]: ...
    @overload
    @classmethod
    def ones[ShapeT: npt._Shape](
        cls,
        shape: ShapeT,
        dtype: None = None,
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[ShapeT, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def ones[ShapeT: npt._Shape, DTypeT: np.generic](
        cls,
        shape: ShapeT,
        dtype: type[DTypeT],
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[ShapeT, np.dtype[DTypeT]]: ...
    @classmethod
    def ones():
        """指定された形状と型の新しい配列を0で埋めた配列を作成する"""

    def zero_check(self) -> NPBool[_ShapeT, dtype[np.bool_]]:
        """要素の数値が0の位置を探す"""

    def IQR(
        self,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[_ShapeT, dtype[np.float64]]:
        """
        配列の四分位数を求める

        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def isinf(self) -> NPBool[_ShapeT, dtype[np.bool_]]:
        """配列の各要素が正または負の無限大(`np.inf`)かどうかを判定する"""

    def isnan(self) -> NPBool[_ShapeT, dtype[np.bool_]]:
        """配列の各要素がNaN(`np.nan`)であるかを判定する"""

    def isfinite(self) -> NPBool[_ShapeT, dtype[np.bool_]]:
        """配列の各要素が有限かどうかを判定する"""

    def isposinf(self) -> NPBool[_ShapeT, dtype[np.bool_]]:
        """配列の各要素が正の無限大(`+np.inf`)かどうかを判定する"""

    def isreal(self) -> NPBool[_ShapeT, dtype[np.bool_]]:
        """配列の各要素が実数かどうかを判定する"""

    def iscomplexobj(self) -> bool:
        """配列の型が複素数型かどうかを判定する"""

    def sorts(
        self,
        axis: SupportsIndex | None = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
    ) -> Self:
        """
        配列内の数値を並び替える

        :param axis: ソートの基準となる軸を指定する
        :type axis: SupportsIndex | None
        :param kind: ソートアルゴリズムの種類を指定する
        :type kind: _SortKind | None
        :param order: `NPNumber`がフィールド定義を持つ配列である場合,どのフィールドを優先して比較するかを指定する
        :type order: str | Sequence[str] | None
        """

    @overload
    @classmethod
    def arange[ScalarT: sgt._ArangeNumber_DtypeLike](
        cls,
        start: sgt._Arange_Number,
        /,
        stop: sgt._Arange_Number,
        step: sgt._Arange_Number | None = 1,
        *,
        dtype: ScalarT,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], dtype[ScalarT]]: ...
    @overload
    @classmethod
    def arange(
        cls,
        start: npt._IntLike_co,
        /,
        stop: npt._IntLike_co | None,
        step: npt._IntLike_co | None = 1,
        *,
        dtype: type[int] | sgt._DTypeLike[np.int_] | None = None,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], dtype[np.int_]]: ...
    @overload
    @classmethod
    def arange(
        cls,
        start: float | np.floating,
        /,
        stop: npt._FloatLike_co,
        step: npt._FloatLike_co | None = 1,
        *,
        dtype: type[float] | sgt._DTypeLike[np.float64] | None = None,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber[tuple[int], dtype[np.float64 | Any]]: ...
    @classmethod
    def arange():
        """
        指定された間隔内で等間隔の数値の配列を返す

        :param start: 区間を開始する数値を指定する
        :type start: -
        :param stop: 区間を終了する数値を指定する
        :type stop: -
        :param step: 値の間隔を指定する
        :type step: -
        :param dtype: 出力される配列の型を指定する
        :type dtype: dtype
        :param device: 作成された配列を配置する場所を指定する
        :type device: Literal["cpu"] | None
        :param like: NumPy配列ではない配列を作成できるようにする参照するオブジェクトを指定する
        :type like: npt._SupportsArrayFunc | None
        :return: 指定された間隔内で等間隔の数値の配列を返す
        """

    @overload
    @classmethod
    def linspace(
        cls,
        start: _ToFloat64,
        stop: _ToFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[tuple[int], np.float64]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: complex,
        stop: complex,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[tuple[int], np.complex128 | Any]: ...
    @overload
    @classmethod
    def linspace[ScalarT: np.generic](
        cls,
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex,
        endpoint: bool,
        retstep: Literal[False],
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[tuple[int], ScalarT]: ...
    @overload
    @classmethod
    def linspace[ScalarT: np.generic](
        cls,
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        *,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[tuple[int], ScalarT]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: _ToArrayFloat64,
        stop: _ToArrayFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[sgt._AnyShape, np.float64]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[sgt._AnyShape, np.float64 | Any]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[sgt._AnyShape, np.complex128 | Any]: ...
    @overload
    @classmethod
    def linspace[ScalarT: np.generic](
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex,
        endpoint: bool,
        retstep: Literal[False],
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def linspace[ScalarT: np.generic](
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        *,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: npt.DTypeLike | None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber[sgt._AnyShape, sgt.Incomplete]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: _ToFloat64,
        stop: _ToFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: None = None,
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[tuple[int], np.float64], np.float64]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: complex,
        stop: complex,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: None = None,
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[tuple[int], np.complex128 | Any], np.complex128 | Any]: ...
    @overload
    @classmethod
    def linspace[ScalarT: np.generic](
        cls,
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[tuple[int], ScalarT], ScalarT]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: _ToArrayFloat64,
        stop: _ToArrayFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: None = None,
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[sgt._AnyShape, np.float64], np.float64]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: None = None,
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[sgt._AnyShape, np.float64 | Any], np.float64 | Any]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: None = None,
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[sgt._AnyShape, np.complex128 | Any], np.complex128 | Any]: ...
    @overload
    @classmethod
    def linspace[ScalarT: np.generic](
        cls,
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[sgt._AnyShape, ScalarT], ScalarT]: ...
    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        retstep: Literal[True],
        dtype: npt.DTypeLike | None = None,
        axis: SupportsIndex = 0,
        device: Literal["cpu"] | None = None,
    ) -> tuple[NPNumber[sgt._AnyShape, sgt.Incomplete], sgt.Incomplete]: ...
    @classmethod
    def linspace():
        """
        指定された間隔で等間隔​​の数値の配列を作成する

        :param start: 数列の開始値を指定する
        :type start: -
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は[`start`,`stop`)である。
        `endpoint`が`True` の場合,生成される値の範囲は[`start`,`stop`]である。

        :type stop: -
        :param retstep: `retstep`が`True`の場合,戻り値にステップ数を追加する
        :type retstep: bool
        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param dtype: 出力する配列の型を指定する
        :type dtype: dtype
        :param axis: 結果にサンプルを格納する軸を指定する
        :type axis: int
        :param device: 作成された配列を配置するデバイスを指定する
        :type device: Literal["cpu"] | None
        """

    @overload
    @classmethod
    def logspace(
        cls,
        start: _ToFloat64,
        stop: _ToFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: _ToFloat64 = 10.0,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.float64]: ...
    @overload
    @classmethod
    def logspace(
        cls,
        start: complex,
        stop: complex,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: complex = 10.0,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.complex128 | Any]: ...
    @overload
    @classmethod
    def logspace[ScalarT: np.generic](
        cls,
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex,
        endpoint: bool,
        base: npt._ComplexLike_co,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def logspace[ScalarT: np.generic](
        cls,
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: sgt._ArrayLikeComplex_co = 10.0,
        *,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def logspace(
        cls,
        start: _ToArrayFloat64,
        stop: _ToArrayFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: _ToArrayFloat64 = 10.0,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.float64]: ...
    @overload
    @classmethod
    def logspace(
        cls,
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: sgt._ArrayLikeComplex_co = 10.0,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.float64 | Any]: ...
    @overload
    @classmethod
    def logspace(
        cls,
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: sgt._ArrayLikeComplex_co = 10.0,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.complex128 | Any]: ...
    @overload
    @classmethod
    def logspace[ScalarT: np.generic](
        cls,
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex,
        endpoint: bool,
        base: sgt._ArrayLikeComplex_co,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def logspace[ScalarT: np.generic](
        cls,
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: sgt._ArrayLikeComplex_co = 10.0,
        *,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def logspace(
        cls,
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: sgt._ArrayLikeComplex_co = 10.0,
        dtype: npt.DTypeLike | None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, sgt.Incomplete]: ...
    @classmethod
    def logspace():
        """
        対数スケール上で等間隔に並んだ数値の配列を作成する

        :param start: 数列の開始値を指定する
        :type start: -
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は[`start`,`stop`)である。
        `endpoint`が`True` の場合,生成される値の範囲は[`start`,`stop`]である。

        :type stop: -
        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param base: 対数の底を指定する
        :type base: array_like
        :param dtype: 出力される配列の型を指定する
        :type dtype: dtype
        :param axis: 結果を収納する軸を指定する
        :type axis: int
        """

    @overload
    @classmethod
    def geomspace(
        start: _ToFloat64,
        stop: _ToFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[tuple[int], np.float64]: ...
    @overload
    @classmethod
    def geomspace(
        start: complex,
        stop: complex,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[tuple[int], np.complex128 | Any]: ...
    @overload
    @classmethod
    def geomspace[ScalarT: np.generic](
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex,
        endpoint: bool,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[tuple[int], ScalarT]: ...
    @overload
    @classmethod
    def geomspace[ScalarT: np.generic](
        start: npt._ComplexLike_co,
        stop: npt._ComplexLike_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[tuple[int], ScalarT]: ...
    @overload
    @classmethod
    def geomspace(
        start: _ToArrayFloat64,
        stop: _ToArrayFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.float64]: ...
    @overload
    @classmethod
    def geomspace(
        start: sgt._ArrayLikeFloat_co,
        stop: sgt._ArrayLikeFloat_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.float64 | Any]: ...
    @overload
    @classmethod
    def geomspace(
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, np.complex128 | Any]: ...
    @overload
    @classmethod
    def geomspace[ScalarT: np.generic](
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex,
        endpoint: bool,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def geomspace[ScalarT: np.generic](
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        *,
        dtype: sgt._DTypeLike[ScalarT],
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, ScalarT]: ...
    @overload
    @classmethod
    def geomspace(
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: npt.DTypeLike | None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber[sgt._AnyShape, sgt.Incomplete]: ...
    @classmethod
    def geomspace():
        """
        対数スケール上で等間隔に配置された(等比数列)配列を作成する

        :param start: 数列の開始値を指定する
        :type start: -
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は[`start`,`stop`)である。
        `endpoint`が`True` の場合,生成される値の範囲は[`start`,`stop`]である。

        :type stop: -
        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param dtype: 出力される配列の型を指定する
        :type dtype: dtype
        :param axis: 結果を収納する軸を指定する
        :type axis: int
        """

    @overload
    @property
    def degree[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """角度を弧度法から度数法に変換する"""

    @overload
    @property
    def degree[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """角度を弧度法から度数法に変換する"""

    @overload
    @property
    def deg[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """角度を弧度法から度数法に変換する"""

    @overload
    @property
    def deg[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """角度を弧度法から度数法に変換する"""

    @overload
    def deg_to_rad[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """角度を弧度法から度数法に変換する"""

    @overload
    def deg_to_rad[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """角度を弧度法から度数法に変換する"""

    @overload
    @property
    def radian[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """角度を度数法から弧度法に変換する"""

    @overload
    @property
    def radian[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """角度を度数法から弧度法に変換する"""

    @overload
    @property
    def rad[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """角度を度数法から弧度法に変換する"""

    @overload
    @property
    def rad[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """角度を度数法から弧度法に変換する"""

    @overload
    def rad_to_deg[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """角度を度数法から弧度法に変換する"""

    @overload
    def rad_to_deg[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """角度を度数法から弧度法に変換する"""

    @overload
    def dsin[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """三角関数の正弦を度数法として要素毎に計算する"""

    @overload
    def dsin[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """三角関数の正弦を度数法として要素毎に計算する"""

    @overload
    def dcos[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """三角関数の余弦を度数法として要素毎に計算する"""

    @overload
    def dcos[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """三角関数の余弦を度数法として要素毎に計算する"""

    @overload
    def dtan[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """三角関数の正接を度数法として要素毎に計算する"""

    @overload
    def dtan[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """三角関数の正接を度数法として要素毎に計算する"""

    @overload
    def darcsin[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """逆正弦関数の結果を度数法で求める"""

    @overload
    def darcsin[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """逆正弦関数の結果を度数法で求める"""

    @overload
    def darccos[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """逆余弦関数の結果を度数法で求める"""

    @overload
    def darccos[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """逆余弦関数の結果を度数法で求める"""

    @overload
    def dartan[DType: sgt._RealNumericDTypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[np.floating]]:
        """逆正接関数の結果を度数法で求める"""

    @overload
    def dartan[DType: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, dtype[DType]],
    ) -> NPNumber[_ShapeT, dtype[sgt._ComplexDtypeLike]]:
        """逆正接関数の結果を度数法で求める"""

    @overload
    def dtypeinfo[_DTypeT: sgt._FloatsNumericDTypeLike](
        self: NPNumber[_ShapeT, _DTypeT],
    ) -> np.finfo[_DTypeT]: ...
    @overload
    def dtypeinfo[_DTypeT: sgt._ComplexDtypeLike](
        self: NPNumber[_ShapeT, _DTypeT],
    ) -> np.finfo[_DTypeT]: ...
    @overload
    def dtypeinfo[_DTypeT: sgt._IntsNumericDTypeLike](
        self: NPNumber[_ShapeT, _DTypeT],
    ) -> np.iinfo[_DTypeT]: ...
    @overload
    @classmethod
    def random(
        cls,
        size: None = None,
        dtype: sgt._DTypeLikeFloat = ...,
        out: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[np.float64, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def random(
        cls,
        size: sgt._ShapeLike,
        dtype: sgt._DTypeLikeF64 = ...,
        out: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._ShapeLike, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def random(
        cls,
        size: sgt._ShapeLike,
        dtype: sgt._DTypeLikeF32,
        out: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._ShapeLike, np.dtype[np.float32]]: ...
    @overload
    @classmethod
    def random[ShapeT: _ArrayF64](
        cls,
        size: sgt._ShapeLike | None = None,
        dtype: sgt._DTypeLikeF64 = ...,
        *,
        out: ShapeT,
        seed: sgt._Seed = None,
    ) -> ShapeT: ...
    @overload
    @classmethod
    def random[ShapeT: _ArrayF32](
        cls,
        size: sgt._ShapeLike | None = None,
        *,
        dtype: sgt._DTypeLikeF32,
        out: ShapeT,
        seed: sgt._Seed = None,
    ) -> ShapeT: ...
    @overload
    @classmethod
    def random[ShapeT: _ArrayF64](
        cls,
        size: sgt._ShapeLike | None,
        dtype: sgt._DTypeLikeF64,
        out: ShapeT,
        seed: sgt._Seed = None,
    ) -> ShapeT: ...
    @overload
    @classmethod
    def random[ShapeT: _ArrayF32](
        cls,
        size: sgt._ShapeLike | None,
        dtype: sgt._DTypeLikeF32,
        out: ShapeT,
        seed: sgt._Seed = None,
    ) -> ShapeT: ...
    @classmethod
    def random():
        """
        [0,1)の範囲でランダムな浮動小数点数の配列を作成する

        :param size: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param out: 結果を格納する代替出力配列を指定する
        :param seed: 乱数のシード値を指定する
        """

    @overload
    @classmethod
    def uniform(
        cls,
        /,
        low: npt._FloatLike_co = 0.0,
        high: npt._FloatLike_co = 1.0,
        shape: None = None,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[float, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def uniform[Dtype: npt.DTypeLike](
        cls,
        /,
        low: npt._FloatLike_co = 0.0,
        high: npt._FloatLike_co = 1.0,
        shape: None = None,
        *,
        dtype: Dtype,
        seed: sgt._Seed = None,
    ) -> NPNumber[float, np.dtype[Dtype]]: ...
    @overload
    @classmethod
    def uniform(
        cls,
        /,
        low: npt._FloatLike_co = 0.0,
        high: npt._FloatLike_co = 1.0,
        *,
        shape: sgt._ShapeLike,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def uniform[Dtype: npt.DTypeLike](
        cls,
        /,
        low: npt._FloatLike_co = 0.0,
        high: npt._FloatLike_co = 1.0,
        *,
        shape: sgt._ShapeLike,
        dtype: Dtype,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[Dtype]]: ...
    @classmethod
    def uniform():
        """
        一様分布からなる配列を生成する

        :param low: 生成する乱数の下限値を指定する
        :param high: 生成する乱数の上限値を指定する
        :param shape: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @overload
    @classmethod
    def normal(
        cls,
        /,
        loc: npt._FloatLike_co = 0.0,
        scale: npt._FloatLike_co = 1.0,
        shape: None = None,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[float, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def normal[Dtype: np.number](
        cls,
        /,
        loc: npt._FloatLike_co = 0.0,
        scale: npt._FloatLike_co = 1.0,
        shape: None = None,
        *,
        dtype: sgt._DTypeLike[Dtype],
        seed: sgt._Seed = None,
    ) -> NPNumber[float, np.dtype[Dtype]]: ...
    @overload
    @classmethod
    def normal(
        cls,
        /,
        loc: npt._FloatLike_co = 0.0,
        scale: npt._FloatLike_co = 1.0,
        *,
        shape: sgt._ShapeLike,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[np.float64]]: ...
    @overload
    @classmethod
    def normal[Dtype: np.number](
        cls,
        /,
        loc: npt._FloatLike_co = 0.0,
        scale: npt._FloatLike_co = 1.0,
        *,
        shape: sgt._ShapeLike,
        dtype: sgt._DTypeLike[Dtype],
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[Dtype]]: ...
    @classmethod
    def normal():
        """
        正規分布からなる配列を生成する

        :param loc: 分布の平均値を指定する
        :param scale: 分布の標準偏差を指定する
        :param shape: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @overload
    @classmethod
    def randint(
        cls,
        /,
        low: int,
        high: int | None = None,
        shape: None = None,
        dtype: None = None,
        endpoint: bool = False,
        seed: sgt._Seed = None,
    ) -> NPNumber[np.int64, np.dtype[np.int64]]: ...
    @overload
    @classmethod
    def randint[Dtype: np.integer | np.bool](
        cls,
        /,
        low: int,
        high: int | None = None,
        shape: None = None,
        *,
        dtype: sgt._DTypeLike[Dtype],
        endpoint: bool = False,
        seed: sgt._Seed = None,
    ) -> NPNumber[np.int64, np.dtype[Dtype]]: ...
    @overload
    @classmethod
    def randint(
        cls,
        /,
        low: int,
        high: int | None = None,
        *,
        shape: sgt._ShapeLike,
        dtype: None = None,
        endpoint: bool = False,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[np.int64]]: ...
    @overload
    @classmethod
    def randint[Dtype: np.integer | np.bool](
        cls,
        /,
        low: int,
        high: int | None = None,
        *,
        shape: sgt._ShapeLike,
        dtype: sgt._DTypeLike[Dtype],
        endpoint: bool = False,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[Dtype]]: ...
    @classmethod
    def randint():
        """
        最小値から最大値までの整数の値からなるランダムに生成された配列を作成する

        :param low: 生成される範囲の最小値を指定する
        :param high: 生成される範囲の最大値を指定する
        :param shape: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param endpoint: 生成される区間の範囲を指定する
        :param seed: 乱数のシード値を指定する
        """

    @overload
    @classmethod
    def logseries(
        cls,
        /,
        p: npt._FloatLike_co,
        size: None = None,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[np.int64, np.dtype[np.int64]]: ...
    @overload
    @classmethod
    def logseries[Dtype: np.number](
        cls,
        /,
        p: npt._FloatLike_co,
        size: None = None,
        *,
        dtype: sgt._DTypeLike[Dtype],
        seed: sgt._Seed = None,
    ) -> NPNumber[Dtype, np.dtype[Dtype]]: ...
    @overload
    @classmethod
    def logseries(
        cls,
        /,
        p: sgt._ArrayLikeFloat_co,
        size: sgt._ShapeLike,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[np.int64]]: ...
    @overload
    @classmethod
    def logseries[Dtype: np.number](
        cls,
        /,
        p: sgt._ArrayLikeFloat_co,
        size: sgt._ShapeLike,
        *,
        dtype: sgt._DTypeLike[Dtype],
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[Dtype]]: ...
    @overload
    @classmethod
    def logseries(
        cls,
        /,
        p: _NDArrayLikeFloat,
        size: None = None,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[np.int64]]: ...
    @overload
    @classmethod
    def logseries[Dtype: np.number](
        cls,
        /,
        p: _NDArrayLikeFloat,
        size: None = None,
        *,
        dtype: sgt._DTypeLike[Dtype],
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[Dtype]]: ...
    @overload
    @classmethod
    def logseries(
        cls,
        /,
        p: sgt._ArrayLikeFloat_co,
        size: None = None,
        dtype: None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[np.int64]] | Any: ...
    @overload
    @classmethod
    def logseries[Dtype: np.number](
        cls,
        /,
        p: sgt._ArrayLikeFloat_co,
        size: None = None,
        *,
        dtype: sgt._DTypeLike[Dtype],
        seed: sgt._Seed = None,
    ) -> NPNumber[sgt._AnyShape, np.dtype[Dtype]] | Any: ...
    @classmethod
    def logseries():
        """
        対数級数分布からなる配列を生成する

        :param p: 分布の形状を指定する。`p`の範囲は[0,1)である必要がある。
        :param size: 出力する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
