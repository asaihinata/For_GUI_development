"""基本的な時間の差や期間について操作するモジュール"""

from datetime import date, datetime, timedelta

import numpy as np

from sgg.dev import _tonparray

from ..dev import _ArrayCommonMixin, _get_dtype, _tm64_unit

__all__ = ["NPTimedelta"]


class NPTimedelta(_ArrayCommonMixin):
    """`np.ndarray`を継承したtimedelta64型の配列クラス"""

    _element_type = (np.timedelta64,)
    _default_dtype = np.dtype("timedelta64[D]")

    def __new__(
        cls,
        obj,
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
        resolved = cls._resolve_dtype(
            "timedelta64[D]" if dtype is None else _tm64_unit(dtype)
        )
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

    def __add__(self, value):
        if isinstance(value, date | datetime):
            return np.add(self, np.datetime64(value))
        elif isinstance(value, np.datetime64) or (
            isinstance(value, np.ndarray) and value.dtype.kind == "M"
        ):
            return np.add(self, value)
        if isinstance(value, timedelta):
            value = np.timedelta64(value, self.dtypeunit)
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __iadd__ = __add__

    def __radd__(self, value):
        if isinstance(value, date | datetime):
            return np.add(np.datetime64(value), self)
        elif isinstance(value, np.datetime64) or (
            isinstance(value, np.ndarray) and value.dtype.kind == "M"
        ):
            return np.add(value, self)
        if isinstance(value, timedelta):
            value = np.timedelta64(value, self.dtypeunit)
        result = np.asarray(np.add(value, self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __sub__(self, value):
        if not (
            isinstance(value, timedelta | np.timedelta64)
            or (isinstance(value, np.ndarray) and value.dtype.kind == "m")
        ):
            return NotImplemented
        if isinstance(value, timedelta):
            value = np.timedelta64(value, self.dtypeunit)
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __isub__ = __sub__

    def __rsub__(self, value):
        if isinstance(value, date | datetime):
            return np.subtract(np.datetime64(value), self)
        elif isinstance(value, np.datetime64) or (
            isinstance(value, np.ndarray) and value.dtype.kind == "M"
        ):
            return np.subtract(value, self)
        if isinstance(value, timedelta):
            value = np.timedelta64(value, self.dtypeunit)
        result = np.asarray(np.subtract(value, self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __mul__(self, value):
        value = _tonparray(value)
        if value.dtype.kind in ["b", "i", "u", "f"]:
            result = np.asarray(np.multiply(self, value)).view(type(self))
            result._dtype = result.dtype
            return result
        return NotImplemented

    __imul__ = __mul__

    def __truediv__(self, value):
        if isinstance(value, timedelta):
            value = np.timedelta64(value)
        if isinstance(value, np.ndarray | np.timedelta64) and value.dtype.kind == "m":
            return np.true_divide(self, value)
        if np.asarray(value).dtype.kind in ["b", "i", "u", "f"]:
            result = np.asarray(np.true_divide(self, value)).view(type(self))
            result._dtype = result.dtype
            return result
        return NotImplemented

    __itruediv__ = __truediv__

    def __rtruediv__(self, value):
        if isinstance(value, timedelta):
            value = np.timedelta64(value)
        if isinstance(value, np.timedelta64) or (
            isinstance(value, np.ndarray) and value.dtype.kind == "m"
        ):
            return np.true_divide(value, self)
        return NotImplemented

    def __pow__(self, value):
        value = np.asarray(value)
        if value.dtype.kind in ["b", "i", "u", "f"]:
            dtype = self._dtype
            result = np.power(self.__array__(np.int64), value)
            result = np.asarray(result.astype(dtype)).view(type(self))
            result._dtype = dtype
            return result
        return NotImplemented

    __ipow__ = __pow__

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

    def astype(self, dtype, copy=True):
        try:
            dtype = np.dtype(_tm64_unit(dtype))
        except:
            dtype = np.dtype(dtype)
        if dtype.kind == "M":
            return np.asarray(self, dtype).view(type(self))
        return self.__array__(dtype, copy=copy)

    @classmethod
    def arange(cls, start, /, stop=None, step=1, dtype=None):
        if not (np.isscalar(start) and _get_dtype(start).kind in ["b", "i", "u", "m"]):
            raise TypeError
        if stop is not None and not (
            np.isscalar(stop) and _get_dtype(stop).kind in ["b", "i", "u", "m"]
        ):
            raise TypeError
        if not (np.isscalar(step) and _get_dtype(step).kind in ["b", "i", "u", "m"]):
            raise TypeError
        result = np.asarray(
            np.arange(start, stop, step=step, dtype=_tm64_unit(dtype))
        ).view(cls)
        result._dtype = result.dtype
        return result

    @property
    def dtypeunit(self):
        return _dtypeunit(str(self._dtype))


def _dtypeunit(dy):
    if not isinstance(dy, str):
        dy = str(dy)
    place = dy.find("[") + 1
    if place == 0:
        return dy
    return dy[(place) : (len(dy) - 1)]
