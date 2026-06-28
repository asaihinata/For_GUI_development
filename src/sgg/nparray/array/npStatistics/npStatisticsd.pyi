"""基本的な統計の計算をするモジュール"""

from typing import Any, Literal, SupportsIndex, TypeAlias

import numpy as np
from numpy.typing import ArrayLike, DTypeLike, NDArray

from ....typing import TypeArrayLikeNumber
from ..npnumber import NPNumber

__all__ = ["NPStatisticsd"]

Type_Method: TypeAlias = Literal[
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
BINS_LIST: TypeAlias = Literal[
    "stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"
]

class NPStatisticsd(NPNumber):
    def __new__(
        cls,
        data: TypeArrayLikeNumber,
        dtype: DTypeLike | None = np.float64,
    ) -> NPStatisticsd:
        """
        基本的な統計の計算をする

        :param data: 数値が入った一次元の配列を指定する
        :type data: TypeArrayLikeNumber
        :param dtype: `NPStatisticsd`内の配列の型を指定する
        :type dtype: DTypeLike | None
        :return: `NPStatisticsd`オブジェクトを返す
        :rtype: NPStatisticsd
        """

    @property
    def data[T](self: T) -> np.ndarray[T]:
        """`NPStatisticsd`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    def tonumpy[T](self: T) -> np.ndarray[T]:
        """`NPStatisticsd`オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def sum(self) -> np.floating:
        """配列の全要素の合計を求める"""

    @property
    def mean(self) -> np.floating:
        """配列の算術平均を求める"""

    @property
    def ave(self) -> np.floating:
        """配列の加重平均を求める"""

    @property
    def max(self) -> np.floating:
        """配列の最大値を求める"""

    @property
    def min(self) -> np.floating:
        """配列の最小値を求める"""

    @property
    def var(self) -> np.floating:
        """配列の分散を求める"""

    @property
    def std(self) -> np.floating:
        """配列の標準偏差を求める"""

    @property
    def pow2(self) -> TypeArrayLikeNumber:
        """配列の各要素を2乗した値を求める"""

    @property
    def deviation(self) -> TypeArrayLikeNumber:
        """配列内の各要素の偏差値を求める"""

    @property
    def log(self) -> TypeArrayLikeNumber:
        """配列の各要素の底が`e`の対数を求める"""

    @property
    def log10(self) -> TypeArrayLikeNumber:
        """配列の各要素の底が`10`の対数を求める"""

    @property
    def log2(self) -> TypeArrayLikeNumber:
        """配列の各要素の底が`2`の対数を求める

        ``numpy.log2`` を使用して計算する"""

    @property
    def log1p(self) -> TypeArrayLikeNumber:
        """配列の各要素について`log(1+x)`を求める"""

    @property
    def devsq(self) -> np.floating:
        """偏差平方和を求める"""

    @property
    def range(self) -> NDArray[Any]:
        """配列の最小値と最大値を求める

        :return: `[最小値,最大値]`の形式の配列を返す
        :rtype: NDArray[Any]
        """

    @property
    def skew(self) -> np.floating:
        """歪度を求める"""

    @property
    def kurtosis(self) -> np.floating:
        """尖度を求める"""

    def percentile(
        self,
        q: tuple[int | float, ...],
        method: Type_Method = "linear",
    ) -> np.floating | NDArray[np.floating]:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: tuple[int | float,...]
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: Type_Method
        """

    def quantile(
        self,
        q: tuple[float, ...],
        method: Type_Method = "linear",
    ) -> np.floating | NDArray[np.floating]:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: tuple[float,...]
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Type_Method
        """

    def IQR(
        method: Type_Method = "linear",
    ) -> NDArray[np.floating]:
        """
        配列の四分位範囲を求める

        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Type_Method
        """

    @property
    def outlier(self) -> NDArray[np.floating]:
        """四分位範囲の外れ値を求める"""

    @property
    def CV(self) -> np.floating:
        """変動係数を求める"""

    @property
    def n(self) -> int:
        """配列の長さの数を返す"""

    @property
    def n1(self) -> int:
        """配列の長さの数-1の値を返す"""
    # ヒストグラム
    def hist_bin_edges(
        self,
        bin: int | BINS_LIST | ArrayLike = 10,
        range: tuple[float, float] | None = None,
        weights: ArrayLike | None = None,
    ) -> NDArray[Any]:
        """
        `bin`で指定された計算方法で計算されたビンの境界を求める

        :param bin: ビンの数や計算方法を指定する
        :type bin: int | BINS_LIST | ArrayLike
        :param range: ビンの下限と上限を指定する
        :type range: tuple[float,float] | None
        :param weights: 重みを指定する
        :type weights: ArrayLike | None
        :return: `bin`で指定された計算方法で計算した結果を返す
        :rtype: NDArray[Any]
        """

    def histogram(
        self,
        bin: int | BINS_LIST | ArrayLike = 10,
        range: tuple[float, float] | None = None,
        weights: ArrayLike | None = None,
    ) -> tuple[NDArray, NDArray]:
        """
        配列のヒストグラムを求める

        :param bin: ビンの数や計算方法を指定する
        :type bin: int | BINS_LIST | ArrayLike
        :param range: ビンの下限と上限を指定する
        :type range: tuple[float,float] | None
        :param weights: 重みを指定する
        :type weights: ArrayLike | None
        :return: 区間内のデータの個数と区間を区切る境界の値を返す
        :rtype: tuple[NDArray,NDArray]
        """

    def bincount(
        self, weights: ArrayLike | None = None, min: SupportsIndex = 0
    ) -> NDArray[np.intp]:
        """
        非負整数の配列に含まれる各値の出現回数を数える

        :param weights: 重みを指定する
        :type weights: ArrayLike | None
        :param min: 出力配列の最小ビン数を指定する
        :type min: SupportsIndex
        :return: 入力配列をビン分割した結果を返す
        :rtype: NDArray[np.intp]
        """
    # 母集団
    def ratio_E_samplingerror(
        self, parcent: int | float, cc: int | float
    ) -> np.float64:
        """
        母比率の標本誤差を求める

        :param parcent: 割合を指定する
        :type parcent: int | float
        :param cc: 信頼係数を指定する
        :type cc: int | float
        :raises TypeError: `parcent`をint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 0.0<=`parcent`<=1.0の範囲で指定しなかった場合に発生させる
        :raises TypeError: 信頼係数`cc`にint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 信頼係数`cc`に0.0から1.0の範囲で指定しなかった場合に発生させる
        """

    def ratio_E(self, p: int | float) -> tuple[np.float64, np.float64]:
        """
        母比率の上限値と下限値を求める

        :param parcent: 割合を指定する
        :type parcent: int | float
        :param cc: 信頼係数を指定する
        :type cc: int | float
        :raises TypeError: `parcent`をint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 0.0<=`parcent`<=1.0の範囲で指定しなかった場合に発生させる
        :raises TypeError: 信頼係数`cc`にint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 信頼係数`cc`に0.0から1.0の範囲で指定しなかった場合に発生させる
        """

    def ave_E_samplingerror(self, cc: int | float = 0.95) -> np.float64:
        """母平均の推定をする

        :param cc: 信頼係数を指定する
        :type cc: int | float"""

    def ave_E(self, cc: float = 0.95) -> tuple[np.float64, np.float64]:
        """
        母平均の上限値と下限値を求める

        :param cc: 信頼係数を指定する
        :type cc: int | float
        """

def cCoefficient(p: int | float = 0.95) -> np.float64:
    """
    信頼係数を求める

    :param p: 信頼係数を指定する
    :type p: int | float
    :raises TypeError: `p`がfloat型を指定しなかった場合に発生させる
    :raises ValueError: `p`が0.0から1.0の範囲外を指定した場合に発生させる
    """
