"""2つの変数データから様々な統計の計算を行うモジュール"""

import numpy as np
from numpy.polynomial.chebyshev import chebfit, chebval

from sgg.nparray.isdtype import numberDtype
from ..dev import NDArrayOperatorsMixin, _ArrayCommonMixin
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
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPStatisticsds(_ArrayCommonMixin, NDArrayOperatorsMixin, np.ndarray):

    _element_type = (int, float, complex, np.number)

    def __new__(cls, x, y, dtype=np.float64):
        resolved = cls._resolve_dtype(dtype)
        if numberDtype(resolved):
            raise TypeError("dtypeには数値型を指定してください")
        obj = np.asarray([x, y], dtype=resolved).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        cls._validate_ndim(obj)
        obj.__xs = NPStatisticsd(x)
        obj.__ys = NPStatisticsd(y)
        return obj

    @classmethod
    def _resolve_dtype(cls, dtype):
        if dtype is not None:
            return np.dtype(dtype)
        return np.dtype(np.float64)

    @classmethod
    def _validate_ndim(cls, obj):
        ndim = obj.ndim
        if ndim != 2:
            raise ValueError(f"{cls.__name__}の次元数は2次元のみです")

    @classmethod
    def _validate_elements(cls, obj):
        if cls._element_type is None:
            return
        for elem in obj.flat:
            if not isinstance(elem, cls._element_type):
                raise TypeError(
                    f"{cls.__name__}の要素は{cls._element_type}のみ許可されています"
                )

    def __array__(self, dtype=np.float64, copy=None):
        return super().__array__(dtype, copy=copy)

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._dtype = getattr(obj, "_dtype", None)
        self.__xs = getattr(obj, "__xs", None)
        self.__ys = getattr(obj, "__ys", None)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPStatisticsd) else x for x in inputs
        )
        result = getattr(ufunc, method)(*raw_inputs, **dict(kwargs))

        if result is NotImplemented:
            return NotImplemented

        if isinstance(result, np.ndarray):
            result = result.view(type(self))
            result._dtype = getattr(inputs[0], "_dtype", None)

        return result

    def __array_function__(self, func, types, args, kwargs):
        if func in HANDLED_FUNCTIONS:
            return HANDLED_FUNCTIONS[func](*args, **kwargs)
        return super().__array_function__(func, types, args, kwargs)

    def __iter__(self):
        return iter(self.data)

    @property
    def element_type(self):
        return self._element_type

    @property
    def data(self):
        return np.asarray(self, dtype=self._dtype)

    @property
    def dtypes(self):
        return self._dtype

    @dtypes.setter
    def dtypes(self, dtype):
        if dtype is not None:
            self._dtype = np.dtype(dtype)

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

    @property
    def Sxy(self):
        return np.cov(self.x, self.y)[0, 1]

    @property
    def Sxxyy(self):
        return self.__xs.devsq * self.__ys.devsq

    @property
    def Sxxyyroot(self):
        return np.power(self.Sxxyy, 0.5)

    def regression(self, n=1):
        return chebfit(self.x, self.y, n)

    def oneregression(self):
        return chebfit(self.x, self.y, 1)

    def chebysheveve(self, Fx, n=1):
        return chebval(Fx, chebfit(self.x, self.y, n))
