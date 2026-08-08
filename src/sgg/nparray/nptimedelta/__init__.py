"""基本的な時間の差や期間について操作するモジュール"""

import numpy as np

from ..dev import _ArrayCommonMixin, _tm64_unit
from ..npdate import NPDate
from ..npnumber import NPNumber

__all__ = ["NPTimedelta"]


class NPTimedelta(_ArrayCommonMixin):
    _element_type = np.timedelta64
    _default_dtype = np.dtype("timedelta64[D]")

    def __new__(
        cls,
        data,
        /,
        dtype="timedelta64[D]",
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        resolved = cls._resolve_dtype(_tm64_unit(dtype))
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
            np.asarray(x) if isinstance(x, NPTimedelta) else x for x in inputs
        )
        result = getattr(ufunc, method)(*raw_inputs, **dict(kwargs))

        if result is NotImplemented:
            return NotImplemented

        if isinstance(result, np.ndarray):
            result = result.view(type(self))
            result._dtype = getattr(inputs[0], "_dtype", None)

        return result

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__

    def __sub__(self, value):
        if isinstance(value, np.ndarray | np.datetime64) and value.dtype.kind == "M":
            result = np.subtract(value, self)
            return NPDate(result, result.dtype)
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __rsub__ = __sub__

    def __mul__(self, value):
        result = np.asarray(np.multiply(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    def __truediv__(self, value):
        if isinstance(value, np.ndarray | np.timedelta64) and value.dtype.kind == "m":
            return NPNumber(np.true_divide(self, value))
        result = np.asarray(np.true_divide(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    def __int__(self):
        lists = self.tolist()
        if np.isscalar(lists):
            return int(lists)
        raise ValueError

    def __float__(self):
        lists = self.tolist()
        if np.isscalar(lists):
            return float(lists)
        raise ValueError

    def __neg__(self):
        result = np.asarray(np.negative(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __pos__(self):
        result = np.asarray(np.positive(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __abs__(self):
        result = np.asarray(np.abs(self)).view(type(self))
        result._dtype = result.dtype
        return result

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

    @classmethod
    def arange(cls, start, /, stop=None, step=1, dtype="timedelta64[D]"):
        return cls(np.arange(start, stop=stop, step=step), dtype=dtype)
