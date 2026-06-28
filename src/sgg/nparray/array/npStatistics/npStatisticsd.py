"""基本的な統計の計算をするモジュール"""

import numpy as np
from scipy.stats import norm

from ...isdtype import numberDtype
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


class NPStatisticsd(NPNumber):
    def __new__(cls, data, dtype=np.float64):
        if numberDtype(dtype):
            raise ValueError("dtypeには数値の型を指定してください")
        return super().__new__(cls, data, dtype=dtype, d_ndim=1)

    def __repr__(self):
        return super().__repr__()

    @property
    def sum(self):
        return np.sum(self.data)

    @property
    def ave(self):
        return np.average(self.data)

    @property
    def mean(self):
        return np.mean(self.data)

    @property
    def max(self):
        return np.max(self.data)

    @property
    def min(self):
        return np.min(self.data)

    @property
    def var(self):
        return np.var(self.data)

    @property
    def std(self):
        return np.std(self.data)

    @property
    def pow2(self):
        return np.power(self.data, 2)

    @property
    def deviation(self):
        std = 10 / np.std(self.data)
        return (std * (self.data - self.mean)) + 50

    @property
    def log(self):
        return np.log(self.data)

    @property
    def log10(self):
        return np.log10(self.data)

    @property
    def log2(self):
        return np.log2(self.data)

    @property
    def log1p(self):
        return np.log1p(self.data)

    @property
    def devsq(self):
        return np.sum((self.data - self.mean) ** 2)

    @property
    def range(self):
        return np.array([self.min, self.max])

    @property
    def skew(self):
        return np.sum((self.data - self.ave) ** 3) / (self.n * np.pow(self.std, 3))

    @property
    def kurtosis(self):
        return np.sum((self.data - self.ave) ** 4) / (self.n * np.pow(self.var, 2))

    def percentile(self, q, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.percentile(self.data, q, method=method)

    def quantile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.quantile(self.data, q, method=method)

    def IQR(self, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.percentile(self.data, [25, 50, 75], method=method)

    @property
    def outlier(self):
        q1, q3 = np.percentile(self.data, [25, 75])
        iqr = (q3 - q1) * 1.5
        return self.data[(self.data < (q1 - iqr)) | (self.data > (q3 + iqr))]

    @property
    def n(self):
        return self.data.size

    @property
    def n1(self):
        return self.n - 1

    @property
    def CV(self):
        return self.std / self.ave

    # ヒストグラム
    def hist_bin_edges(self, bin=10, range=None, weights=None):
        return np.histogram_bin_edges(self.data, bins=bin, range=range, weights=weights)

    def histogram(self, bin=10, range=None, weights=None):
        return np.histogram(self.data, bins=bin, range=range, weights=weights)

    def bincount(self, weights=None, min=0):
        return np.bincount(self.data, weights=weights, minlength=min)

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
