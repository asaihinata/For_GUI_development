"""基本的な統計の計算をするモジュール"""

import numpy as np
from scipy.stats import norm

from ..npnumber import NPNumber

__all__ = ["NPStatisticsd"]
method_list = [
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


class NPStatisticsd:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        raise TypeError(f"{cls.__name__}を継承をすることはできません")

    def __init__(self, data):
        if (
            isinstance(data, np.ndarray | list | tuple | range)
            or np.isscalar(data)
            or hasattr(data, "__array__")
        ):
            data = np.array(data)
        elif isinstance(data, NPNumber):
            data = data.data
        else:
            raise TypeError("dataには配列を指定してください")
        if np.issubdtype(data.dtype, np.number):
            self.__data = data
        else:
            raise TypeError
        if self.__data.ndim != 1:
            raise ValueError("dataには1次元の配列を指定してください")

    def __repr__(self):
        return f"NPStatisticsd({self.__data})"

    @property
    def data(self):
        return self.__data

    @property
    def sum(self):
        return np.sum(self.__data)

    @property
    def ave(self):
        return np.average(self.__data)

    @property
    def mean(self):
        return np.mean(self.__data)

    @property
    def max(self):
        return np.max(self.__data)

    @property
    def min(self):
        return np.min(self.__data)

    @property
    def var(self):
        return np.var(self.__data)

    @property
    def std(self):
        return np.std(self.__data)

    @property
    def pow2(self):
        return np.power(self.__data, 2)

    @property
    def deviation(self):
        std = 10 / np.std(self.__data)
        return (std * (self.__data - self.mean)) + 50

    @property
    def log(self):
        return np.log(self.__data)

    @property
    def log10(self):
        return np.log10(self.__data)

    @property
    def log2(self):
        return np.log2(self.__data)

    @property
    def log1p(self):
        return np.log1p(self.__data)

    @property
    def devsq(self):
        return np.sum((self.__data - self.mean) ** 2)

    @property
    def range(self):
        return np.array([self.min, self.max])

    @property
    def skew(self):
        return np.sum((self.__data - self.ave) ** 3) / (self.n * np.pow(self.std, 3))

    @property
    def kurtosis(self):
        return np.sum((self.__data - self.ave) ** 4) / (self.n * np.pow(self.var, 2))

    def percentile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.percentile(self.__data, q, axis=axis, method=method)

    def quantile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.quantile(self.__data, q, axis=axis, method=method)

    def IQR(self, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.percentile(self.__data, [25, 50, 75], axis=axis, method=method)

    @property
    def outlier(self):
        q1, q3 = np.percentile(self.__data, [25, 75])
        iqr = (q3 - q1) * 1.5
        return self.__data[(self.__data < (q1 - iqr)) | (self.__data > (q3 + iqr))]

    @property
    def n(self):
        return self.__data.size

    @property
    def n1(self):
        return self.n - 1

    @property
    def CV(self):
        return self.std / self.ave

    # ヒストグラム
    def hist_bin_edges(self, bins=10, range=None, weights=None):
        return np.histogram_bin_edges(
            self.__data, bins=bins, range=range, weights=weights
        )

    def histogram(self, bins=10, range=None, weights=None):
        return np.histogram(self.__data, bins=bins, range=range, weights=weights)

    def bincount(self, weights=None, min=0):
        return np.bincount(self.__data, weights=weights, minlength=min)

    # 母集団
    def ratio_E_samplingerror(self, parcent, cc=0.95):
        if not isinstance(parcent, float | int):
            raise TypeError("parcentにはint型もしくはfloat型を指定してください")
        elif not 0 <= parcent <= 1:
            raise ValueError("parcentには0.0から1.0の範囲で指定してください")
        return cCoefficient(cc) * np.sqrt(parcent * (1 - parcent) / self.n)

    def ratio_E(self, parcent, cc=0.95):
        serror = self.ratio_E_samplingerror(parcent, cc)
        return parcent + serror, parcent - serror

    def ave_E_samplingerror(self, cc=0.95):
        return cCoefficient(cc) * (self.std / np.sqrt(self.n))

    def ave_E(self, cc=0.95):
        ave = self.ave
        avs = self.ave_E_samplingerror(cc)
        return ave + avs, ave - avs


def cCoefficient(p=0.95):
    if not isinstance(p, int | float):
        raise TypeError("pには数値型で指定してください")
    elif not 0 <= p <= 1:
        raise ValueError("0.0<=p<=1.0の範囲の値を指定してください")
    return norm.ppf(p)
