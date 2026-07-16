from datetime import date, datetime

import numpy as np

from sgg.typing import _dt64_unit, _get_dt64_unit

from ..dev import _ArrayShapeMixin, _normalize_axis
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPDate"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPDate(_ArrayShapeMixin, np.ndarray):
    _element_type = np.datetime64
    _default_dtype = np.dtype("datetime64[D]")

    def __new__(
        cls,
        data,
        dtype="datetime64[D]",
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
    ):
        resolved = cls._resolve_dtype(np.dtype(_dt64_unit(dtype)))
        obj = np.asarray(data, dtype=resolved).view(cls)
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

    def __array__(self, dtype="datetime64[D]", copy=None):
        return super().__array__(np.dtype(_dt64_unit(dtype)), copy=copy)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPDate) else x for x in inputs
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

    def __add__(self, value):
        result = np.add(np.asarray(self), value).view(type(self))
        result._dtype = result.dtype
        return result

    def __sub__(self, value):
        result = np.subtract(np.asarray(self), value).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__
    __rsub__ = __sub__
    __isub__ = __sub__

    def __ne__(self, value):
        return NPBool(np.not_equal(np.asarray(self), value))

    def __eq__(self, value):
        return NPBool(np.equal(np.asarray(self), value))

    def __lt__(self, value):
        return NPBool(np.less(np.asarray(self), value))

    def __le__(self, value):
        return NPBool(np.less_equal(np.asarray(self), value))

    def __gt__(self, value):
        return NPBool(np.greater(np.asarray(self), value))

    def __ge__(self, value):
        return NPBool(np.greater_equal(np.asarray(self), value))
    @property
    def year(self):
        return NPNumber(self.astype('datetime64[Y]').astype(int),np.int64) + 1970
    @property
    def month(self):
        return NPNumber(self.astype('datetime64[M]').astype(int),np.uint8) % 12
    @property
    def day(self):
        return NPNumber((self - self.astype('datetime64[M]')).astype(int) + 1,np.uint8)
    def to_datetime(self):
        return self.data.astype(datetime)

    def to_date(self):
        return self.data.astype(date)

    def to_int(self, dtype=None):
        if dtype is None:
            dtype = self.dtypes
        return NPNumber(self.astype(_dt64_unit(dtype)).astype(np.int64), np.int64)

    @classmethod
    def today(cls):
        result = np.asarray(np.datetime64("today")).view(cls)
        result._dtype = np.dtype("datetime64[D]")
        return result

    @classmethod
    def now(cls):
        result = np.asarray(np.datetime64("now")).view(cls)
        result._dtype = np.dtype("datetime64[s]")
        return result

    @classmethod
    def unix(cls, dtype="h"):
        result = np.asarray(np.datetime64(0, _get_dt64_unit(dtype))).view(cls)
        result._dtype = result.dtype
        return result

    def weekday(self):
        dt = self.to_datetime()
        return NPNumber([i.weekday() for i in dt], dtype=np.uint8)

    def diff_today(self, days=False):
        if not isinstance(days, bool):
            days = False
        day = np.busday_count(np.asarray(self), self.today()) + int(days)
        return NPNumber(day, dtype=np.int64)

    def range(self, axis=None):
        if axis is not None:
            axis = _normalize_axis(axis, self.ndim, "range")
        data = np.asarray(self).view(type(self))
        return np.min(data, axis=axis), np.max(data, axis=axis)
