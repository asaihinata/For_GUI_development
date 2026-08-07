from datetime import date, datetime

import numpy as np
from dateutil.parser import parse

from ..dev import (_ArrayCommonMixin, _dt64_unit, _get_dt64_unit,
                   _normalize_axis, _tm64_unit)
from ..npbool import NPBool
from ..npnumber import NPNumber
from ..npstr import NPString

__all__ = ["NPDate"]

_pass_str_list = ["TODAY", "today", "NOW", "now"]


class NPDate(_ArrayCommonMixin, np.ndarray):
    _element_type = np.datetime64
    _default_dtype = np.dtype("datetime64[D]")

    def __new__(
        cls,
        data,
        /,
        dtype="datetime64[D]",
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        resolved = cls._resolve_dtype(_dt64_unit(dtype))
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
        return super().__array_function__(func, types, args, kwargs)

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __iadd__ = __add__

    def __sub__(self, value):
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __isub__ = __sub__

    def __eq__(self, value):
        return NPBool(np.equal(np.asarray(self), value))

    def __ne__(self, value):
        return NPBool(np.not_equal(np.asarray(self), value))

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
        return NPNumber(self.astype("datetime64[Y]").astype(np.int64), np.int64) + 1970

    @property
    def month(self):
        return NPNumber(
            np.mod(self.astype("datetime64[M]").astype(np.int64), 12) + 1, np.uint8
        )

    @property
    def day(self):
        return NPNumber((self - self.astype("datetime64[M]")).astype(int) + 1, np.uint8)

    def isnat(self):
        return np.asarray(np.isnat(self)).view(type(self))

    def to_datetime(self):
        return self.data.astype(datetime)

    def to_date(self):
        return self.data.astype(date)

    def to_str(self):
        return NPString(np.datetime_as_string(self), dtype=np.str_)

    @classmethod
    def arange(cls, start, stop, /, step=1, *, dtype="D", device=None, like=None):
        dtype = _dt64_unit(dtype)
        start = _obj_to_datetime64(start, dtype).astype("int64")
        stop = _obj_to_datetime64(stop, dtype).astype("int64")
        if stop < start:
            start, stop = stop, start
        return cls(
            np.arange(start, stop, step=step, dtype=dtype, device=device, like=like),
            dtype=dtype,
        )

    @classmethod
    def linspace(
        cls,
        start,
        stop,
        /,
        num=50,
        endpoint=True,
        retstep=False,
        dtype="D",
        axis=0,
        *,
        device=None,
    ):
        dtype = _get_dt64_unit(dtype)
        start = _obj_to_datetime64(start, dtype).astype("int64")
        stop = _obj_to_datetime64(stop, dtype).astype("int64")
        if stop < start:
            start, stop = stop, start
        if retstep:
            samples, step = np.linspace(
                start,
                stop,
                num,
                endpoint,
                retstep,
                np.int64,
                axis,
                device=device,
            )
            return cls(samples, dtype), step.astype(_tm64_unit(dtype))
        else:
            return cls(
                np.linspace(
                    start,
                    stop,
                    num,
                    endpoint,
                    dtype=np.int64,
                    axis=axis,
                    device=device,
                ),
                dtype,
            )

    @classmethod
    def today(cls):
        result = np.asarray(np.datetime64("today"), dtype="datetime64[D]").view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def now(cls):
        result = np.asarray(np.datetime64("now"), dtype="datetime64[s]").view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def unix(cls):
        result = np.asarray(np.datetime64(0, "s")).view(cls)
        result._dtype = result.dtype
        return result

    def strftime(self, format):
        return NPString(
            [i.strftime(format) for i in self.to_datetime().flatten()], dtype=np.str_
        ).reshape(self.shape)

    def weekday(self):
        return NPNumber(
            [i.weekday() for i in self.to_datetime().flatten()], dtype=np.uint8
        ).reshape(self.shape)

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

    def leapyear(self):
        year = np.asarray(self.year)
        return NPBool((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))

    def leapcount(self):
        year = np.asarray(self.year)
        return NPBool(
            (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0))
        ).TrueCount

    def cleanNaT(self):
        flat, dtype = self.flat, self.dtype
        result = np.asarray(flat[~np.isnat(flat)], dtype=dtype).view(type(self))
        result._dtype = dtype
        return result


def _obj_to_datetime64(obj, dtype):
    if isinstance(obj, str):
        return np.datetime64(obj if obj in _pass_str_list else parse(obj), dtype)
    elif isinstance(obj, np.str_):
        obj = str(obj)
        return np.datetime64(obj if obj in _pass_str_list else parse(obj), dtype)
    elif isinstance(obj, np.datetime64):
        return obj.astype(_dt64_unit(dtype))
    elif isinstance(obj, datetime | date):
        return np.datetime64(obj).astype(_dt64_unit(dtype))
    else:
        raise TypeError
