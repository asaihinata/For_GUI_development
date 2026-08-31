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


class NPNumber(_ArrayCommonMixin):
    """`np.ndarray`を継承した数値型の配列クラス"""

    _element_type = np.number
    _default_dtype = None

    def __new__(
        cls,
        obj,
        /,
        dtype=None,
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(obj, copy=copy).view(cls)
            if obj.dtype.kind == "b":
                obj = obj.astype(int)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(dtype)
            obj = np.asarray(obj, dtype=resolved, copy=copy).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        if isinstance(d_ndim, int):
            obj._min_ndim = obj._max_ndim = d_ndim
        else:
            obj._min_ndim = min_ndim
            obj._max_ndim = max_ndim
        cls._validate_ndim(obj, obj._min_ndim, obj._max_ndim)
        return obj

    def __eq__(self, value):
        result = np.equal(self, value)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def __ne__(self, value):
        result = np.not_equal(self, value)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def __lt__(self, value):
        result = np.less(self, value)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def __le__(self, value):
        result = np.less_equal(self, value)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def __gt__(self, value):
        result = np.greater(self, value)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def __ge__(self, value):
        result = np.greater_equal(self, value)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __iadd__ = __add__
    __radd__ = __add__

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

    __imul__ = __mul__
    __rmul__ = __mul__

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

    def __pos__(self):
        result = np.asarray(np.positive(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __neg__(self):
        result = np.asarray(np.negative(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __abs__(self):
        result = np.asarray(np.abs(self)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def sturgesval(self):
        return 1 + np.log2(self.size)

    def dtypeinfo(self):
        if np.issubdtype(self._dtype, np.integer):
            return np.iinfo(self._dtype)
        else:
            return np.finfo(self._dtype)

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

    def bin(self):
        if not self.dtype.kind in ["i", "u"]:
            raise TypeError
        if self.ndim == 0:
            return bin(int(self))
        return np.vectorize(lambda i: bin(i))(self.tolist())

    def oct(self):
        if not self.dtype.kind in ["i", "u"]:
            raise TypeError
        if self.ndim == 0:
            return oct(int(self))
        return np.vectorize(lambda i: oct(i))(self.tolist())

    def hex(self):
        if not self.dtype.kind in ["i", "u"]:
            raise TypeError
        if self.ndim == 0:
            return hex(int(self))
        return np.vectorize(lambda i: hex(i))(self.tolist())

    # 生成
    @classmethod
    def zeros(cls, shape, dtype=None):
        result = np.zeros(shape, dtype)
        return cls(result, result.dtype)

    @classmethod
    def ones(cls, shape, dtype=None):
        result = np.ones(shape, dtype)
        return cls(result, result.dtype)

    # 判定
    def zero_check(self):
        return np.array(self == 0, dtype=np.bool_)

    def count_nonzero(self, axis=None, keepdims=False):
        if not isinstance(keepdims, bool):
            keepdims = False
        result = np.asarray(
            np.count_nonzero(self, axis=axis, keepdims=keepdims), np.uint64
        ).view(type(self))
        result._dtype = np.uint64
        return result

    def isinf(self):
        result = np.isinf(self)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def isnan(self):
        result = np.isnan(self)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def isfinite(self):
        result = np.isfinite(self)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def isposinf(self):
        result = np.isposinf(self)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def isreal(self):
        result = np.isreal(self)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

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
        if dtype is not None and np.dtype(dtype).kind not in ["i", "u", "f"]:
            raise ValueError
        if not (np.isscalar(start) and np.asarray(start).dtype.kind in ["i", "u", "f"]):
            raise ValueError
        if stop is not None and not (
            np.isscalar(stop) and np.asarray(stop).dtype.kind in ["i", "u", "f"]
        ):
            raise ValueError
        result = np.asarray(np.arange(start, stop, step=step)).view(cls)
        result._dtype = result.dtype
        return result

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
        if dtype is not None and not np.issubdtype(np.dtype(dtype), np.number):
            raise TypeError
        result = np.linspace(
            start,
            stop,
            num,
            endpoint,
            dtype=dtype,
            retstep=retstep,
            axis=axis,
        )
        if retstep:
            result, step = result
        result = np.asarray(result).view(cls)
        result._dtype = result.dtype
        if retstep:
            return result, step
        else:
            return result

    @classmethod
    def logspace(
        cls, start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0
    ):
        dtype = _dtype_check(dtype)
        result = np.asarray(
            np.logspace(start, stop, num=num, endpoint=endpoint, base=base, axis=axis),
            dtype=dtype,
        ).view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def geomspace(cls, start, stop, num=50, endpoint=True, dtype=None, axis=0):
        dtype = _dtype_check(dtype)
        result = np.asarray(
            np.geomspace(start, stop, num, endpoint, axis=axis), dtype
        ).view(cls)
        result._dtype = result.dtype
        return result

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

    # 変換
    def baserepr(self, base=2, padding=None):
        if self._dtype.kind not in ["i", "u"]:
            raise TypeError
        elif not 2 <= base <= 36:
            raise ValueError("baseには2から36の範囲の整数で指定してください")
        if padding is None:
            padding = 0
        if self.zero_ndim:
            return np.base_repr(self[0], base, padding)
        return np.vectorize(lambda x, b, p: np.base_repr(x, b, p))(
            self.__array__(), base, padding
        )

    # 乱数
    @classmethod
    def random(cls, size=None, dtype=None, seed=None):
        dtype = _dtype_check(dtype)
        result = default_rng(seed).random(size=size, dtype=dtype)
        result = np.asarray(result).view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def uniform(cls, low=0.0, high=1.0, size=None, dtype=None, seed=None):
        dtype = _dtype_check(dtype)
        result = default_rng(seed).uniform(low, high, size=size)
        result = np.asarray(result, dtype=dtype).view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def normal(cls, loc=0.0, scale=1.0, size=None, dtype=None, seed=None):
        dtype = _dtype_check(dtype)
        result = default_rng(seed).normal(loc, scale, size=size)
        result = np.asarray(result, dtype=dtype).view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def integers(
        cls, low, high=None, size=None, dtype=np.int64, endpoint=False, seed=None
    ):
        dtype, kind = _dtype_check(dtype, True)
        if kind not in ["u", "i"]:
            raise TypeError("型が不正です")
        result = default_rng(seed).integers(
            low, high, size=size, dtype=dtype, endpoint=endpoint
        )
        result = np.asarray(result).view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def logseries(cls, p, size=None, dtype=np.int64, seed=None):
        dtype = _dtype_check(dtype)
        result = default_rng(seed).logseries(p, size)
        result = np.asarray(result, dtype=dtype).view(cls)
        result._dtype = result.dtype
        return result


def _dtype_check(dtype, kind=False):
    dtypes = np.dtype(dtype)
    if dtype is None or not np.issubdtype(dtypes, np.number):
        if kind:
            return None, dtypes.kind
        return None
    if kind:
        return dtype, dtypes.kind
    return dtype
