"""基本的な数値の操作をするモジュール"""

from typing import Any, Iterator, Literal, Self, TypeAlias, TypeVar, overload

import numpy as np
from numpy._typing import _FloatLike_co
from numpy.typing import NDArray

from sgg.typing import Typeaxis, _ArrayLikeNumber_co, _NumberT, _ShapeT

from ..dev import _ArrayShapeMixin
from ..npbool import NPBool

_DTypeT = TypeVar(
    "_DTypeT", bound=np.dtype, default=np.dtype[np.float64], covariant=True
)
__all__ = ["NPNumber"]
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

class NPNumber(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承した数値型の配列クラス"""

    _element_type: tuple[type[int], type[float], type[complex], type[np.number]]
    _default_dtype: type[np.float64]

    @overload
    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[np.float64]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: type[_NumberT],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[_NumberT]]: ...
    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: type[_NumberT] | None = np.float64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeNumber_co
        :param dtype: 配列の型を指定する
        :type dtype: type[_NumberT] | None
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

    def __class_getitem__(cls, item: Any) -> type[NPNumber[Any, Any]]: ...
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
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT_co]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT | None, copy: bool | None = None
    ) -> (
        np.ndarray[np._ShapeT_co, np._DTypeT] | np.ndarray[np._ShapeT_co, np._DTypeT_co]
    ): ...
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

    def __eq__(self, value: Any) -> NPBool[Any]: ...
    def __ne__(self, value: Any) -> NPBool[Any]: ...
    def __lt__(self, value: Any) -> NPBool[Any]: ...
    def __le__(self, value: Any) -> NPBool[Any]: ...
    def __gt__(self, value: Any) -> NPBool[Any]: ...
    def __ge__(self, value: Any) -> NPBool[Any]: ...
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
    def __rmod__(self, value: Any) -> NPNumber: ...
    def __imod__(self, value: Any) -> NPNumber: ...
    def __divmod__(self, value: Any) -> NPNumber: ...
    def __rdivmod__(self, value: Any) -> NPNumber: ...
    def __abs__(self) -> NPNumber: ...
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
    def count_nonzero(
        self, axis: np._ShapeLike | None = ..., keepdims: bool = ...
    ) -> np.intp | NDArray[np.intp]:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: _ShapeLike | None
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
        q: tuple[int | float, ...],
        axis: Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber[Any, np.dtype[np.float64]]:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: tuple[int | float,...]
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
    ) -> NPNumber:
        """
        配列の四分位範囲を求める

        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """
