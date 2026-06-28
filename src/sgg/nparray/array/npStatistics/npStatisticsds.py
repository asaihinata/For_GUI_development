"""2つの変数データから様々な統計の計算を行うモジュール"""

import numpy as np
from numpy.polynomial.chebyshev import chebfit, chebval

from ..npnumber import NPNumber
from .npstatisticsd import NPStatisticsd

__all__ = ["NPStatisticsds"]
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


class NPStatisticsds(NPNumber):
    def __new__(cls, x, y, dtype=np.float64):
        obj = super().__new__(cls, [x, y], dtype=dtype, d_ndim=2)
        cls.__xs = NPStatisticsd(x)
        cls.__ys = NPStatisticsd(y)
        return obj

    def __repr__(self):
        return super().__repr__()

    @property
    def x(self):
        return self.__xs

    @property
    def xmath(self):
        return self.__xs.data

    @property
    def y(self):
        return self.__ys

    @property
    def ymath(self):
        return self.__ys.data

    def covariance(self):
        return np.cov(self.x, self.y)[0, 1]

    def correlation(self):
        return np.corrcoef(self.x, self.y)[0, 1]

    def correlation_coefficient(self):
        return self.Sxy / self.Sxxyyroot

    # x,y
    @property
    def Sxy(self):
        return np.cov(self.x, self.y)[0, 1]

    @property
    def Sxxyy(self):
        return self.__xs.devsq * self.__ys.devsq

    @property
    def Sxxyyroot(self):
        return np.power(self.Sxxyy, 0.5)

    # 回帰直線
    def regression(self, n=1):
        return chebfit(self.x, self.y, n)

    def oneregression(self):
        return chebfit(self.x, self.y, 1)

    def chebysheveve(self, Fx, n=1):
        return chebval(Fx, chebfit(self.x, self.y, n))
