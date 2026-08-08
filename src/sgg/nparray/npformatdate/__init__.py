from datetime import date, datetime

import numpy as np
from dateutil.parser import parse
from numpy.strings import isnumeric

from ..dev import _ArrayCommonMixin, _dt64_unit

__all__ = ["NPFormatDate"]


class NPFormatDate(_ArrayCommonMixin, np.ndarray):
    _element_type = np.datetime64
    _default_dtype = "datetime64[D]"

    def __new__(
        cls,
        data,
        /,
        dtype="datetime64[D]",
        *,
        yearfirst=False,
        dayfirst=False,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        data = np.asarray(data, dtype=np.str_)
        if not isinstance(yearfirst, bool):
            yearfirst = False
        if not isinstance(dayfirst, bool):
            dayfirst = False
        func = np.vectorize(
            lambda strs, yearfirst, dayfirst: _conversion(strs, yearfirst, dayfirst)
        )
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(
                np.array(
                    [func(i, yearfirst, dayfirst) for i in np.nditer(data)],
                    dtype=resolved,
                    copy=copy,
                ).reshape(data.shape)
            ).view(cls)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(np.dtype(_dt64_unit(dtype)))
            obj = np.asarray(
                np.array(
                    [func(i, yearfirst, dayfirst) for i in np.nditer(data)],
                    dtype=resolved,
                    copy=copy,
                ).reshape(data.shape)
            ).view(cls)
        data = np.asanyarray(data, dtype=np.str_)
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
            np.asarray(x) if isinstance(x, NPFormatDate) else x for x in inputs
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

    def __sub__(self, value):
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__
    __rsub__ = __sub__
    __isub__ = __sub__

    def to_datetime(self):
        return self.data.astype(datetime)

    def to_date(self):
        return self.data.astype(date)

    # 日付
    @property
    def year(self):
        return np.array(self.astype("datetime64[Y]").astype(np.int64), np.int64) + 1970

    @property
    def month(self):
        return np.array(
            np.mod(self.astype("datetime64[M]").astype(np.int64), 12) + 1, np.uint8
        )

    @property
    def day(self):
        return np.array((self - self.astype("datetime64[M]")).astype(int) + 1, np.uint8)

    def weekday(self):
        m = self.month
        flag = m <= 2
        y, m = np.where(flag, self.year - 1, self.year), np.where(flag, m + 12, m)
        return (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + self.day) % 7

    def diff_today(self, days=False):
        if not isinstance(days, bool):
            days = False
        day = np.busday_count(np.asarray(self), self.today()) + int(days)
        return np.array(day, dtype=np.int64)

    def range(self):
        return np.min(self), np.max(self)


def _conversion(strs, yearfirst, dayfirst):
    if isnumeric(strs):
        strs = np.datetime64("today", "D") + np.int64(strs)
    return parse(str(strs), yearfirst=yearfirst, dayfirst=dayfirst)
