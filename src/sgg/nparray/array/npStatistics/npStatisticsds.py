"""2つの変数データから様々な統計の計算を行うモジュール"""

from __future__ import annotations

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
from numpy.polynomial.chebyshev import chebfit, chebval

from ...isdtype import numberDtype
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


class NPStatisticsds(NDArrayOperatorsMixin, np.ndarray):

    _element_type = (int, float, complex, np.number)

    def __new__(cls, x, y, dtype=np.float64):
        resolved = cls._resolve_dtype(dtype)
        if numberDtype(resolved):
            raise TypeError("dtypeには数値型を指定してください")
        obj = np.asarray([x, y], dtype=resolved).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        cls._validate_ndim(obj)
        cls.__xs = NPStatisticsd(x)
        cls.__ys = NPStatisticsd(y)
        return obj

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._dtype = getattr(obj, "_dtype", None)

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

    @classmethod
    def __instancecheck__(cls, instance):
        return isinstance(instance, NPStatisticsd)

    def __repr__(self):
        return f"{type(self).__name__}({np.array2string(np.asarray(self), separator=',')},dtype={self.dtype})"

    def __str__(self):
        return self.__repr__()

    def __contains__(self, item):
        return super().__contains__(item)

    def __len__(self):
        return super().__len__()

    def __iter__(self):
        if self.ndim == 1:
            return iter([self.data])
        return iter(self.data)

    def __reversed__(self):
        result = np.flip(np.asarray(self)).view(type(self))
        result._dtype = self._dtype
        return result

    def __getitem__(self, key):
        size = self.size
        if size == 0:
            raise IndexError("空の配列にはアクセスできません")
        data = self.data.flatten()
        if isinstance(key, int):
            if key == size:
                return data[size - 1]
            elif key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return self.data.flatten()[key]

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

    @property
    def data(self):
        return np.asarray(self)

    @property
    def dtypes(self):
        return self._dtype

    @dtypes.setter
    def dtypes(self, dtype):
        if dtype is not None:
            self._dtype = np.dtype(dtype)
        return self._dtype

    def lengtharange(self):
        shapes = self.shape
        lens = len(shapes)
        if lens == 1:
            raw = np.arange(0, self.size, 1, dtype=np.uint64)
        else:
            raw = np.tile(
                np.arange(0, shapes[lens - 1], dtype=np.uint64), np.prod(shapes[:-1])
            ).reshape(shapes)
        result = raw.view(type(self))
        result._dtype = np.dtype("uint64")
        return result

    def shapesize(self, shapes):
        if self.shape == shapes:
            return True
        return False

    def tonumpy(self):
        return np.asarray(self)

    def all_None(self):
        return bool(np.all(self.data == None))

    def any_None(self):
        return bool(np.any(self.data == None))

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
