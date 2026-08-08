"""基本的な数値の操作をするモジュール"""

import numpy as np
from numpy.random import default_rng

from sgg.exceptions import ShapeError

from ..dev import _ArrayCommonMixin, _arrisuint

__all__ = ["NPNumber"]
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


class NPNumber(_ArrayCommonMixin, np.ndarray):
    _element_type = (int, float, complex, np.number)
    _default_dtype = np.float64

    def __new__(
        cls,
        data,
        /,
        dtype=np.float64,
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(data, copy=copy).view(cls)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(dtype)
            obj = np.asarray(data, dtype=resolved, copy=copy).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        if isinstance(d_ndim, int):
            cls._validate_ndim(obj, d_ndim, d_ndim)
            obj._min_ndim = obj._max_ndim = d_ndim
        else:
            cls._validate_ndim(obj, min_ndim, max_ndim)
            obj._min_ndim = min_ndim
            obj._max_ndim = max_ndim
        return obj

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPNumber) else x for x in inputs
        )
        result = getattr(ufunc, method)(*raw_inputs, **dict(kwargs))

        if result is NotImplemented:
            return NotImplemented

        if isinstance(result, np.ndarray):
            result = result.view(type(self))
            result._dtype = getattr(inputs[0], "_dtype", None)

        return result

    def __array_function__(self, func, types, args, kwargs):
        return super().__array_function__(func, types, args, kwargs)

    def __eq__(self, value):
        return np.array(np.equal(self, value), dtype=np.bool_)

    def __ne__(self, value):
        return np.array(np.not_equal(self, value), dtype=np.bool_)

    def __lt__(self, value):
        return np.array(np.less(self, value), dtype=np.bool_)

    def __le__(self, value):
        return np.array(np.less_equal(self, value), dtype=np.bool_)

    def __gt__(self, value):
        return np.array(np.greater(self, value), dtype=np.bool_)

    def __ge__(self, value):
        return np.array(np.greater_equal(self, value), dtype=np.bool_)

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__

    def __sub__(self, value):
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rsub__ = __sub__
    __isub__ = __sub__

    def __mul__(self, value):
        result = np.asarray(np.multiply(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rmul__ = __mul__
    __imul__ = __mul__

    def __truediv__(self, value):
        result = np.asarray(np.divide(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rtruediv__ = __truediv__
    __itruediv__ = __truediv__

    def __floordiv__(self, value):
        result = np.asarray(np.floor_divide(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rfloordiv__ = __floordiv__
    __ifloordiv__ = __floordiv__

    def __mod__(self, value):
        result = np.asarray(np.mod(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rmod__ = __mod__
    __imod__ = __mod__

    def __pow__(self, value):
        result = np.asarray(np.pow(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rpow__ = __pow__
    __ipow__ = __pow__

    def __divmod__(self, value):
        result1, result2 = np.asarray(np.divmod(self, value))
        result1, result2 = result1.view(type(self)), result2.view(type(self))
        result1._dtype = result1.dtype
        result2._dtype = result2.dtype
        return result1, result2

    __rdivmod__ = __divmod__

    def __abs__(self):
        result = np.asarray(np.abs(self)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def sturgesval(self):
        return 1 + np.log2(self.size)

    def dtypeinfo(self):
        if np.issubdtype(self.dtype, np.integer):
            return np.iinfo(self.dtype)
        else:
            return np.finfo(self.dtype)

    def cussum(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    j + np.insert(j, 0, 0)[:-1]
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def cusdiff(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    j - np.insert(j, 0, 0)[:-1]
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def cusprod(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    j * np.insert(j, 0, 0)[:-1]
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def cusdiv(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    np.insert(j, 0, 0)[:-1] / j
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def percentile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.percentile(np.asarray(self), q, axis=axis, method=method).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def quantile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.quantile(np.asarray(self), q, axis=axis, method=method).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def IQR(self, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.percentile(
            np.asarray(self), [25, 50, 75], axis=axis, method=method
        ).view(type(self))
        result._dtype = result.dtype
        return result

    def ratio(self, axis=None):
        result = np.asarray((self / np.sum(self, axis=axis, keepdims=True)) * 100).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    @classmethod
    def zeros(cls, shape, dtype=None):
        result = np.zeros(shape, dtype)
        return cls(result, result.dtype)

    @classmethod
    def ones(cls, shape, dtype=None):
        result = np.ones(shape, dtype)
        return cls(result, result.dtype)

    def zero_check(self):
        return np.array(self == 0, dtype=np.bool_)

    def count_nonzero(self, axis=None, keepdims=False):
        if not isinstance(keepdims, bool):
            keepdims = False
        return np.count_nonzero(np.asarray(self), axis=axis, keepdims=keepdims)

    def isinf(self):
        return np.array(np.isinf(self), dtype=np.bool_)

    def isnan(self):
        return np.array(np.isnan(self), dtype=np.bool_)

    def isfinite(self):
        return np.array(np.isfinite(self), dtype=np.bool_)

    def isposinf(self):
        return np.array(np.isposinf(self), dtype=np.bool_)

    def isreal(self):
        return np.array(np.isreal(self), dtype=np.bool_)

    def iscomplexobj(self):
        return np.iscomplexobj(self)

    def sorts(self, axis=-1, kind=None, order=None):
        result = np.asarray(np.sort(self, axis, kind, order)).view(type(self))
        result._dtype = result.dtype
        return result

    @classmethod
    def sequential(cls, shape):
        if not _arrisuint(shape):
            raise ShapeError(shape)
        result = np.asarray(
            np.arange(np.prod(shape), dtype=np.uint64).reshape(shape)
        ).view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def arange(cls, start, /, stop=None, step=1, *, dtype=None):
        if dtype is None:
            aranges = np.arange(start, stop, step=step)
            dtype = aranges.dtype
        else:
            aranges = np.arange(start, stop, step=step, dtype=dtype)
        return cls(aranges, dtype=dtype)

    @classmethod
    def linspace(
        cls,
        start,
        stop,
        num=50,
        endpoint=True,
        retstep=False,
        dtype=None,
        axis=0,
    ):
        result = np.linspace(
            start,
            stop,
            num,
            endpoint,
            retstep=retstep,
            dtype=dtype,
            axis=axis,
        )
        return cls(result, dtype=result.dtype)

    @classmethod
    def logspace(
        cls, start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0
    ):
        result = np.logspace(
            start, stop, num=num, endpoint=endpoint, base=base, dtype=dtype, axis=axis
        )
        return cls(result, dtype=result.dtype)

    @classmethod
    def geomspace(cls, start, stop, num=50, endpoint=True, dtype=None, axis=0):
        result = np.geomspace(start, stop, num, endpoint, dtype=dtype, axis=axis)
        return cls(result, dtype=result.dtype)

    # 角度
    @property
    def degree(self):
        result = np.asarray(180 * self / np.pi).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def deg(self):
        result = np.asarray(180 * self / np.pi).view(type(self))
        result._dtype = result.dtype
        return result

    def deg_to_rad(self):
        result = np.asarray(180 * self / np.pi).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def radian(self):
        result = np.asarray(self * np.pi / 180).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def rad(self):
        result = np.asarray(self * np.pi / 180).view(type(self))
        result._dtype = result.dtype
        return result

    def rad_to_deg(self):
        result = np.asarray(self * np.pi / 180).view(type(self))
        result._dtype = result.dtype
        return result

    # 三角関数
    def dsin(self):
        result = np.asarray(np.sin(self * np.pi / 180)).view(type(self))
        result._dtype = result.dtype
        return result

    def dcos(self):
        result = np.asarray(np.cos(self * np.pi / 180)).view(type(self))
        result._dtype = result.dtype
        return result

    def dtan(self):
        result = np.asarray(np.tan(self * np.pi / 180)).view(type(self))
        result._dtype = result.dtype
        return result

    def darcsin(self):
        result = np.asarray(180 * np.arcsin(self) / np.pi).view(type(self))
        result._dtype = result.dtype
        return result

    def darccos(self):
        result = np.asarray(180 * np.arccos(self) / np.pi).view(type(self))
        result._dtype = result.dtype
        return result

    def darctan(self):
        result = np.asarray(180 * np.arctan(self) / np.pi).view(type(self))
        result._dtype = result.dtype
        return result

    # random
    @classmethod
    def random(cls, size=None, dtype=None, seed=None):
        result = default_rng(seed).random(size=size, dtype=dtype)
        if dtype is None:
            dtype = np.dtype(type(result)) if np.isscalar(result) else result.dtype
        return cls(result, dtype=dtype)

    @classmethod
    def uniform(cls, low=0.0, high=1.0, shape=None, dtype=None, seed=None):
        result = default_rng(seed).uniform(low, high, size=shape)
        if dtype is None:
            dtype = np.dtype(type(result)) if np.isscalar(result) else result.dtype
        return cls(result, dtype=dtype)

    @classmethod
    def normal(cls, loc=0.0, scale=1.0, shape=None, dtype=None, seed=None):
        result = default_rng(seed).normal(loc, scale, size=shape)
        if dtype is None:
            dtype = np.dtype(type(result)) if np.isscalar(result) else result.dtype
        return cls(result, dtype=dtype)

    @classmethod
    def randint(
        cls, low, high=None, shape=None, dtype=np.int64, endpoint=False, seed=None
    ):
        result = default_rng(seed).integers(
            low, high, size=shape, dtype=dtype, endpoint=endpoint
        )
        return cls(result, dtype=result.dtype)

    @classmethod
    def logseries(cls, p, size=None, dtype=np.int64, seed=None):
        return cls(default_rng(seed).logseries(p, size), dtype=dtype)
