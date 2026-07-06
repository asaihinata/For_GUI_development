from datetime import date, datetime

import numpy as np

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin
from ..npbool import NPBool
from ..npnumber import NPNumber
from ._typing import serchDtype
from .npformatdate import NPFormatDate

__all__ = ["NPDate"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPDate(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = (NPFormatDate, np.datetime64, datetime, date)
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

    @classmethod
    def today(cls):
        return NPDate([np.datetime64("today")], dtype="datetime64[D]")

    @classmethod
    def now(cls):
        return NPDate([np.datetime64("now")], dtype="datetime64[h]")


    def __array__(self, dtype=np.dtype("datetime64[D]"), copy=None):
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

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

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

    def __ne__(self, other):
        return NPBool(np.not_equal(np.asarray(self), other))

    def __eq__(self, other):
        return NPBool(np.equal(np.asarray(self), other))

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
            elif -size <= key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return data[key]
        raise TypeError("keyにはintまたはsliceを指定してください")

    def todatetime(self):
        return self.data.astype(datetime)

    def todate(self):
        return self.data.astype(date)

    def weekday(self):
        dt = self.todatetime()
        return NPNumber([i.weekday() for i in dt], dtype=np.uint8)

    def diff_today(self, days=False):
        if not isinstance(days, bool):
            days = False
        day = np.busday_count(np.asarray(self), self.today()) + int(days)
        return NPNumber(day, dtype=np.int64)
