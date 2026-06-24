"""基本的な統計の計算をするモジュール"""

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


class NPStatisticsds:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        raise TypeError(f"{cls.__name__}を継承をすることはできません")

    def __init__(self, x, y):
        self.__xs = NPStatisticsd(x)
        self.__ys = NPStatisticsd(y)
        self.__x = self.__xs.data
        self.__y = self.__ys.data

    def __repr__(self):
        return f"NPStatisticsds(\nx={self.__x},\ny={self.__y})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def xmath(self):
        return self.__xs

    @property
    def ymath(self):
        return self.__ys

    def covariance(self):
        return np.cov(self.__x, self.__y)[0, 1]

    def correlation(self):
        return np.corrcoef(self.__x, self.__y)[0, 1]

    def correlation_coefficient(self):
        return self.Sxy / self.Sxxyyroot

    # x,y
    @property
    def Sxy(self):
        return np.cov(self.__x, self.__y)[0, 1]

    @property
    def Sxxyy(self):
        return self.__xs.devsq * self.__ys.devsq

    @property
    def Sxxyyroot(self):
        return np.power(self.Sxxyy, 0.5)

    # 回帰直線
    def regression(self, n=1):
        return chebfit(self.__x, self.__y, n)

    def oneregression(self):
        return chebfit(self.__x, self.__y, 1)

    def chebysheveve(self, Fx, n=1):
        return chebval(Fx, chebfit(self.__x, self.__y, n))
