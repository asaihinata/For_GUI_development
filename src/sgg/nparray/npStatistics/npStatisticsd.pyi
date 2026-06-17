"""基本的な統計の計算をするモジュール"""

from typing import Any, Literal, SupportsIndex, TypeAlias

from numpy import float64, intp, ndarray
from numpy.typing import ArrayLike, NDArray

from ..npNumber import NPNumber

__all__ = ["NPStatisticsd"]
BINS_LIST: TypeAlias = Literal[
    "stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"
]

class NPStatisticsd:
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """raises TypeError: `NPStatisticsd`オブジェクトを継承するときに発生させる"""

    def __init__(self, data: NPNumber | ndarray = ...) -> None:
        """
        基本的な統計の計算をする

        :param data: 配列を指定する
        :type data: NPNumber|ndarray
        """

    def __repr__(self) -> str: ...
    @property
    def sum(self):
        """配列の合計を求める"""

    @property
    def mean(self):
        """配列の算術平均を求める"""

    @property
    def ave(self):
        """配列の加重平均を求める"""

    @property
    def max(self):
        """配列の最大値を求める"""

    @property
    def min(self):
        """配列の最低値を求める"""

    @property
    def var(self):
        """配列の分散を求める"""

    @property
    def std(self):
        """配列の標準偏差を求める"""

    @property
    def pow2(self):
        """配列を2乗した値を求める"""

    @property
    def deviation(self):
        """配列内の偏差値を求める"""

    @property
    def log(self):
        """配列の底が`e`の対数を求める"""

    @property
    def log10(self):
        """配列の底が`10`の対数を求める"""

    @property
    def log2(self):
        """配列の底が`2`の対数を求める"""

    @property
    def log1p(self):
        """np.log1p(data)を返す"""

    @property
    def devsq(self):
        """偏差平方和を求める"""

    @property
    def range(self):
        """配列の範囲を求める"""

    @property
    def skew(self):
        """歪度を求める"""

    @property
    def kurtosis(self):
        """尖度を求める"""

    def percentile(
        self,
        q: tuple[int | float, ...],
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
    ):
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: tuple[int|float,...]
        :param axis: 計算する軸を指定する
        :type axis: int|None
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    def quantile(
        self,
        q: tuple[float, ...],
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
    ):
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: tuple[float,...]
        :param axis: 計算する軸を指定する
        :type axis: int|None
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    def IQR(
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
    ):
        """
        配列の四分位範囲を求める

        :param axis: 計算する軸を指定する
        :type axis: int|None
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    @property
    def outlier(self):
        """四分位範囲の外れ値を求める"""

    @property
    def CV(self):
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
        bins: int | BINS_LIST | ArrayLike = 10,
        range: tuple[float, float] | None = None,
        weights: ArrayLike | None = None,
    ) -> NDArray[Any]:
        """
        `bins`で指定された計算方法で計算されたビンの境界を求める

        :param bins: ビンの数や計算方法を指定する
        :type bins: int|Literal["stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"]|ArrayLike
        :param range: ビンの下限と上限を指定する
        :type range: tuple[float,float]|None
        :param weights: 重みを指定する
        :type weights: ArrayLike|None
        :return: `bins`で指定された計算方法で計算した結果を返す
        :rtype: NDArray[Any]
        """

    def histogram(
        self,
        bins: int | BINS_LIST | ArrayLike = 10,
        range: tuple[float, float] | None = None,
        weights: ArrayLike | None = None,
    ) -> tuple[NDArray, NDArray]:
        """
        配列のヒストグラムを求める

        :param bins: ビンの数や計算方法を指定する
        :type bins: int|Literal["stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"]|ArrayLike
        :param range: ビンの下限と上限を指定する
        :type range: tuple[float,float]|None
        :param weights: 重みを指定する
        :type weights: ArrayLike|None
        :return: 区間内のデータの個数と区間を区切る境界の値を返す
        :rtype: tuple[NDArray,NDArray]
        """

    def bincount(
        self, weights: ArrayLike | None = None, min: SupportsIndex = 0
    ) -> NDArray[intp]:
        """
        非負整数の配列に含まれる各値の出現回数を数える

        :param weights: 重みを指定する
        :type weights: ArrayLike|None
        :param min: 出力配列の最小ビン数を指定する
        :type min: SupportsIndex
        :return: 入力配列をビン分割した結果を返す
        :rtype: NDArray[intp]
        """
    # 母集団
    def ratio_E_samplingerror(self, parcent: int | float, cc: int | float) -> float64:
        """
        母比率の標本誤差を求める

        :param parcent: 割合を指定する
        :type parcent: int|float
        :param cc: 信頼係数を指定する
        :type cc: int|float
        :raises TypeError: `parcent`をint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 0.0<=`parcent`<=1.0の範囲で指定しなかった場合に発生させる
        :raises TypeError: 信頼係数`cc`にint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 信頼係数`cc`に0.0から1.0の範囲で指定しなかった場合に発生させる
        """

    def ratio_E(self, p: int | float) -> tuple[float64, float64]:
        """
        母比率の上限値と下限値を求める

        :param parcent: 割合を指定する
        :type parcent: int|float
        :param cc: 信頼係数を指定する
        :type cc: int|float
        :raises TypeError: `parcent`をint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 0.0<=`parcent`<=1.0の範囲で指定しなかった場合に発生させる
        :raises TypeError: 信頼係数`cc`にint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 信頼係数`cc`に0.0から1.0の範囲で指定しなかった場合に発生させる
        """

    def ave_E_samplingerror(self, cc: int | float = 0.95) -> float64:
        """母平均の推定をする

        :param cc: 信頼係数を指定する
        :type cc: int|float"""

    def ave_E(self, cc: float = 0.95) -> tuple[float64, float64]:
        """
        母平均の上限値と下限値を求める

        :param cc: 信頼係数を指定する
        :type cc: int|float
        """

def cCoefficient(p: int | float = 0.95) -> float64:
    """
    信頼係数を求める

    :param p: 信頼係数を指定する
    :type p: int|float
    :raises TypeError: `p`がfloat型を指定しなかった場合に発生させる
    :raises ValueError: `p`が0.0から1.0の範囲外を指定した場合に発生させる
    """
