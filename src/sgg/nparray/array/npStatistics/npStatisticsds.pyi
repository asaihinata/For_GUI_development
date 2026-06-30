"""2つの変数データから様々な統計の計算を行うモジュール"""

from typing import Any, Iterator, Literal, TypeAlias, overload

import numpy as np
from numpy._typing import _ArrayLikeFloat_co
from numpy.lib.mixins import NDArrayOperatorsMixin
from numpy.typing import DTypeLike, NDArray

from ....typing import TypeArrayLikeNumber
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

class NPStatisticsds(NDArrayOperatorsMixin, np.ndarray):
    """2つの変数データから様々な統計の計算を行うオブジェクト"""

    def __new__(
        cls,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNumber,
        dtype: DTypeLike | None = np.float64,
    ) -> NPStatisticsds:
        """
        2つの変数データから様々な統計の計算を行うオブジェクト`NPStatisticsds`を返す

        :param x: 数値が入った一次元の配列を指定する
        :type x: TypeArrayLikeNumber
        :param y: 数値が入った一次元の配列を指定する
        :type y: TypeArrayLikeNumber
        :param dtype: `NPStatisticsds`内の配列の型を指定する
        :type dtype: DTypeLike | None
        :return: `NPStatisticsds`オブジェクトを返す
        :rtype: NPStatisticsds
        """

    @classmethod
    def __instancecheck__(cls, instance: Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[NDArray[Any]] | Iterator[Any]: ...
    def __reversed__(self) -> NPStatisticsd:
        """
        逆順にした新しい配列オブジェクトを返す

        :return: 全軸で反転した配列を返す
        """

    @overload
    def __getitem__(self, key: int) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> np.ndarray: ...
    def __getitem__(self, key: int | slice) -> Any | np.ndarray:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は1次元に展開してからアクセスし,範囲外のインデックスはモジュロで折り返す

        :param key: インデックスまたはスライスを指定する
        :type key: int | slice
        :return: インデックスに対応する要素を返す
        :rtype: Any | np.ndarray
        :raises IndexError: 配列が空の場合に発生させる
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
    def __array_finalize__(self, obj: np.ndarray | None) -> None:
        """スライスやview後もdtypeや次元数情報を引き継がさせるメソッド"""

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
    def dtypes(self, dtype: DTypeLike | None) -> np.dtype | None:
        """
        配列のdtypeを設定する

        :param dtype: 配列のdtypeを指定する
        :type dtype: DTypeLike | None
        :return:
        :rtype: numpy.dtype | None
        """

    def lengtharange(self) -> NDArray[np.unsignedinteger[np._64Bit]]:
        """
        配列オブジェクトと同じ`shape`を持つ,各軸の最終次元インデックスの配列を返す

        `dtype`は`np.uint64`に固定される

        :return: インデックス配列を返す
        """

    def shapesize(self, shapes: tuple[int, ...]) -> bool:
        """
        配列オブジェクトの`shape`が`shapes`と一致するかを確認する

        :param shapes: 比較する`shape`を指定する
        :type shapes: tuple[int, ...]
        :return: `shape`が一致する場合は`True`を返し,一致しない場合は`False`を返す
        :rtype: bool
        """

    def tonumpy(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    def all_None(self) -> bool:
        """
        配列内の全要素が`None`かどうかを返す

        :return: 配列内の全要素が`None`の場合は`True`を返し,そうでなければ`False`を返す
        :rtype: bool
        """

    def any_None(self) -> bool:
        """
        配列内のいずれかの要素が`None`かどうかを返す

        :return: `None`の要素が1つでもある場合は`True`を返し,そうでなければ`False`を返す
        :rtype: bool
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
    # x,y
    @property
    def Sxy(self) -> np.floating:
        """`x`と`y`の共分散を求める"""

    @property
    def Sxxyy(self) -> np.floating:
        """`x`の偏差平方和と`y`の偏差平方和の積を求める"""

    @property
    def Sxxyyroot(self) -> np.floating:
        """`x`の偏差平方和と`y`の偏差平方和の積の平方和を求める"""
    # 回帰直線
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
