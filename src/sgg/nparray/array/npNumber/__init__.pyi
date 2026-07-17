"""基本的な数値の操作をするモジュール"""

from typing import (Any, Iterator, Literal, Self, Sequence, SupportsIndex,
                    TypeAlias, TypeVar, overload)

import numpy as np
from numpy._typing import (_ArrayLikeNumber_co, _DTypeLike, _FloatLike_co,
                           _NumberLike_co)
from numpy.typing import NDArray

from sgg.typing import Typeaxis

from ..dev import _ArrayShapeMixin
from ..npbool import NPBool

__all__ = ["NPNumber"]
_DType = TypeVar(
    "_DType", bound=np.generic, default=np.dtype[np.float64], covariant=True
)
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

TYPEMETHOD: TypeAlias = Literal[
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
HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPNumber[_ShapeTs](_ArrayShapeMixin, np.ndarray[_ShapeTs, np.dtype[_DType]]):
    """`np.ndarray`を継承した数値型の配列クラス"""

    _element_type: tuple[type[int], type[float], type[complex], type[np.number]]
    _default_dtype: type[np.float64]

    @overload
    def __new__[_ShapeT: _NumberLike_co](
        cls,
        data: _ShapeT,
        dtype: None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[np.float64]]: ...
    @overload
    def __new__[_ShapeT: _NumberLike_co, DType: np.number](
        cls,
        data: _ShapeT,
        dtype: _DTypeLike[DType],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[DType]]: ...
    @overload
    def __new__[_ShapeT: _ArrayLikeNumber_co](
        cls,
        data: _ShapeT,
        dtype: None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, _DType]: ...
    @overload
    def __new__[_ShapeT: _ArrayLikeNumber_co, DType: np.number](
        cls,
        data: _ShapeT,
        dtype: _DTypeLike[DType],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[DType]]: ...
    def __new__() -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: -
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __class_getitem__(
        cls, item: Any
    ) -> type[NPNumber[_ShapeTs, np.dtype[_DType]]]: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPNumber | Any:
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
        self, dtype: None = None, copy: bool | None = None
    ) -> np.ndarray[_ShapeTs, _DType]: ...
    @overload
    def __array__[DType](
        self, dtype: DType, copy: bool | None = None
    ) -> np.ndarray[_ShapeTs, np.dtype[DType]]: ...
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

    def __eq__(self, value: Any) -> NPBool[_ShapeTs, np.dtype[np.bool_]]: ...
    def __ne__(self, value: Any) -> NPBool[_ShapeTs, np.dtype[np.bool_]]: ...
    def __lt__(self, value: Any) -> NPBool[_ShapeTs, np.dtype[np.bool_]]: ...
    def __le__(self, value: Any) -> NPBool[_ShapeTs, np.dtype[np.bool_]]: ...
    def __gt__(self, value: Any) -> NPBool[_ShapeTs, np.dtype[np.bool_]]: ...
    def __ge__(self, value: Any) -> NPBool[_ShapeTs, np.dtype[np.bool_]]: ...
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
    def __abs__(self) -> NPNumber: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeTs, _DType]]: ...
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
    def count_nonzero(
        self, axis: Typeaxis = ..., keepdims: bool = ...
    ) -> np.intp | NDArray[np.intp]:
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

    def cussum(self) -> NPNumber[_ShapeTs, _DType]:
        """一つ前の元の値との和を求める"""

    def cusdiff(self) -> NPNumber[_ShapeTs, _DType]:
        """一つ前の元の値との差を求める"""

    def cusprod(self) -> NPNumber[_ShapeTs, _DType]:
        """一つ前の元の値との積を求める"""

    def cusdiv(self) -> NPNumber[_ShapeTs, _DType]:
        """一つ前の元の値との除算を求める"""

    def percentile(
        self,
        q: _FloatLike_co,
        axis: Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[Any, np.dtype[np.float64]]:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: _FloatLike_co
        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def quantile(
        self,
        q: _FloatLike_co,
        axis: Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[Any, np.dtype[np.float64]]:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: _FloatLike_co
        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def ratio(self, axis: Typeaxis = None) -> NPNumber:
        """行や列ごとの合計に対する比率を求める"""

    def zero_check(self) -> NPBool[Any, np.dtype[np.bool]]:
        """要素の数値が0の位置を探す"""

    def IQR(
        self,
        axis: Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[_ShapeTs, np.dtype[np.float64]]:
        """
        配列の四分位数を求める

        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def isinf(self) -> NPBool:
        """配列の各要素が正または負の無限大(`np.inf`)かどうかを判定する"""

    def isnan(self) -> NPBool:
        """配列の各要素がNaN(`np.nan`)であるかを判定する"""

    def isfinite(self) -> NPBool:
        """配列の各要素が有限かどうかを判定する"""

    def isposinf(self) -> NPBool:
        """配列の各要素が正の無限大(`+np.inf`)かどうかを判定する"""

    def isreal(self) -> NPBool:
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
