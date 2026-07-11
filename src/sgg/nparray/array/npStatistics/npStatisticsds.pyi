"""2つの変数データから様々な統計の計算を行うモジュール"""

from typing import Any, Iterator, Literal, Self, TypeAlias, overload

import numpy as np
from numpy._typing import _ArrayLikeFloat_co
from numpy.typing import DTypeLike, NDArray

from sgg.typing import _ArrayLikeNumber_co, _NumberT

from ..dev import _ArrayCommonMixin
from .npstatisticsd import NPStatisticsd

__all__ = ["NPStatisticsds"]

BINS_LIST: TypeAlias = Literal[
    "stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"
]
METHOD_LIST: TypeAlias = Literal[
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

class NPStatisticsds(_ArrayCommonMixin, np.ndarray):
    """2つの変数データから様々な統計の計算を行うオブジェクト"""
    _element_type=tuple[type[int], type[float], type[complex], type[np.number]]
    def __new__(
        cls,
        x: _ArrayLikeNumber_co,
        y: _ArrayLikeNumber_co,
        dtype: np.dtype[_NumberT] | None = np.float64,
    ) -> Self:
        """
        2つの変数データから様々な統計の計算を行うオブジェクト`NPStatisticsds`を返す

        :param x: 数値が入った一次元の配列を指定する
        :type x: TypeArrayLikeNumber
        :param y: 数値が入った一次元の配列を指定する
        :type y: TypeArrayLikeNumber
        :param dtype: `NPStatisticsds`内の配列の型を指定する
        :type dtype: np.dtype[_NumberT] | None
        :rtype: Self
        :return: `NPStatisticsds`オブジェクトを返す
        """

    @classmethod
    def _resolve_dtype(
        cls,
        dtype: np.dtype | str | type | None,
    ) -> np.dtype | None:
        """
        引数dtypeを解決させる

        :param dtype: ユーザーが指定するdtype
        :return: 解決されたdtypeを返す
        :rtype: numpy.dtype | None
        """

    @classmethod
    def _validate_ndim(
        cls,
        obj: np.ndarray,
    ) -> None:
        """
        配列の次元数が2次元か検証する

        :param obj: 検証対象の配列
        :raises ValueError: 次元数が範囲外の場合に発生させる
        """

    @classmethod
    def _validate_elements(cls, obj: np.ndarray) -> None:
        """
        配列内の要素が`_element_type`と一致するか検証する

        :param obj: 検証対象の配列
        :raises TypeError: 許可されていない型の要素が含まれる場合に発生させる
        """

    def __array_finalize__(self, obj: np.ndarray | None) -> None:
        """スライスやview後もdtypeやx,yの情報を引き継がさせるメソッド"""

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPStatisticsd | Any:
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

    def __iter__(self) -> Iterator[Any]: ...
    @property
    def element_type(
        self,
    ) -> tuple[type[int], type[float], type[complex], type[np.number]]:
        """NPStatisticsdsで許可されている型を取得する"""

    @property
    def data(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def dtypes(self) -> np.dtype | None:
        """
        インスタンス生成時に確定したdtypeを取得する

        :return:
        :rtype: numpy.dtype | None
        """

    @dtypes.setter
    def dtypes(self, dtype: DTypeLike | None) -> None:
        """
        配列のdtypeを設定する

        :param dtype: 配列の型を指定する
        :type dtype: DTypeLike | None
        """

    @property
    def x(self) -> NPStatisticsd:
        """`x`データを`NPStatisticsd`オブジェクトで返す"""

    @property
    def xmath(self) -> np.ndarray:
        """`x`データをnumpyの配列で返す"""

    @property
    def y(self) -> NPStatisticsd:
        """`y`データを`NPStatisticsd`オブジェクトで返す"""

    @property
    def ymath(self) -> np.ndarray:
        """`y`データをnumpyの配列で返す"""

    def covariance(self) -> np.floating:
        """共分散を求める"""

    def correlation(self) -> np.floating:
        """相関係数を求める"""

    def correlation_coefficient(self) -> np.floating:
        """単相関係数を求める"""

    @property
    def Sxy(self) -> np.floating:
        """`x`と`y`の共分散を求める"""

    @property
    def Sxxyy(self) -> np.floating:
        """`x`の偏差平方和と`y`の偏差平方和の積を求める"""

    @property
    def Sxxyyroot(self) -> np.floating:
        """`x`の偏差平方和と`y`の偏差平方和の積の平方和を求める"""

    def regression(self, n: int = 1) -> NDArray[np.floating]:
        """点(x,y)に次数`n`の多項式を当てはめる"""

    def oneregression(self) -> NDArray[np.floating]:
        """
        点(x,y)に一次方程式の回帰直線を返す

        :return: [傾き,切片]として返す
        :rtype: NDArray[np.floating]
        """

    def chebysheveve(self, Fx: _ArrayLikeFloat_co, n: int = 1) -> NDArray[np.floating]:
        """
        点`Fx`において点(x,y)に次数`n`の多項式を評価する

        :param Fx: 評価したい点を指定する
        :type Fx: _ArrayLikeFloat_co
        :param n: 次数を指定する
        :type n: int
        """
