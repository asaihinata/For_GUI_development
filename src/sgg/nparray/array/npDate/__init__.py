from datetime import date, datetime

import numpy as np

from sgg.typing import serchDtype

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPDate"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPDate(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = (np.datetime64, datetime, date)
    _default_dtype = "datetime64[D]"

    def __new__(
        cls,
        data,
        dtype="datetime64[D]",
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
    ):
        resolved = cls._resolve_dtype(serchDtype(dtype))
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
        return super().__array__(np.dtype(serchDtype(dtype)), copy=copy)

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

    def __add__(self, other):
        result = super().__add__(other)
        result._dtype = result.dtype
        return result

    def __sub__(self, other):
        result = super().__sub__(other)
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __rsub__ = __sub__

    def __ne__(self, value):
        return NPBool(np.not_equal(np.asarray(self), value))

    def __eq__(self, value):
        return NPBool(np.equal(np.asarray(self), value))

    def todatetime(self):
        return self.data.astype(datetime)

    def todate(self):
        return self.data.astype(date)

    @classmethod
    def today(cls):
        return NPDate([np.datetime64("today")], dtype="datetime64[D]")

    @classmethod
    def now(cls):
        return NPDate([np.datetime64("now")], dtype="datetime64[h]")

    def weekday(self):
        dt = self.todatetime()
        return NPNumber([i.weekday() for i in dt], dtype=np.uint8)

    def diff_today(self, days=False):
        if not isinstance(days, bool):
            days = False
        day = np.busday_count(np.asarray(self), self.today()) + int(days)
        return NPNumber(day, dtype=np.int64)
