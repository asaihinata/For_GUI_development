from datetime import date, datetime

import numpy as np
from dateutil.parser import parse

from ..dev import _ArrayCommonMixin, _dt64_unit, _get_dt64_unit, _tm64_unit

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
        return np.array(np.equal(np.asarray(self), value),dtype=np.bool_)

    def __ne__(self, value):
        return np.array(np.not_equal(np.asarray(self), value),dtype=np.bool_)

    def __lt__(self, value):
        return np.array(np.less(np.asarray(self), value),dtype=np.bool_)

    def __le__(self, value):
        return np.array(np.less_equal(np.asarray(self), value),dtype=np.bool_)

    def __gt__(self, value):
        return np.array(np.greater(np.asarray(self), value),dtype=np.bool_)

    def __ge__(self, value):
        return np.array(np.greater_equal(np.asarray(self), value),dtype=np.bool_)

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

    # 判定
    def isnat(self):
        return np.array(np.isnat(self),np.bool_)

    # 変換
    def to_datetime(self):
        return self.data.astype(datetime)

    def to_date(self):
        return self.data.astype(date)

    def to_str(self):
        return np.array(np.datetime_as_string(self), dtype=np.str_)

    def strftime(self, format):
        def func(arr,format):return arr.strftime(format)
        return np.array(np.vectorize(func)(self.astype(datetime),format))

    # 範囲
    @classmethod
    def arange(cls, start, stop, /, step=1, *, dtype="D"):
        dtype = _get_dt64_unit(dtype)
        start = _obj_to_datetime64(start, dtype).astype("int64")
        stop = _obj_to_datetime64(stop, dtype).astype("int64")
        if stop < start:
            start, stop = stop, start
        result = np.asarray(np.arange(start, stop, step=step), dtype=_dt64_unit(dtype)).view(cls)
        result._dtype = result.dtype
        return result

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
                axis
            )
            result = np.asarray(samples, dtype=_dt64_unit(dtype)).view(cls)
            result._dtype = result.dtype
            return result, step.astype(_tm64_unit(dtype))
        else:
            result=np.linspace(
                start,
                stop,
                num,
                endpoint,
                retstep,
                np.int64,
                axis
            )
            result = np.asarray(result, dtype=_dt64_unit(dtype)).view(cls)
            result._dtype = result.dtype
            return result

    def range(self):
        return np.min(self), np.max(self)

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

    # 曜日
    def weekday(self):
        m=self.month
        flag=(m<=2)
        y,m=np.where(flag,self.year-1,self.year),np.where(flag,m+12,m)
        return (y+y//4-y//100+y//400+(13*m+8)//5+self.day)%7

    def begin_month_weekday(self):
        m=self.month
        flag=(m<=2)
        y,m=np.where(flag,self.year-1,self.year),np.where(flag,m+12,m)
        return (y+y//4-y//100+y//400+(13*m+8)//5+1)%7

    def end_month_weekday(self):
        dates=NPDate(self.astype("datetime64[M]") + np.timedelta64(1, "M"),"M") - np.timedelta64(1, "D")
        return dates.weekday()

    def diff_today(self, days=False):
        if not isinstance(days, bool):
            days = False
        day = np.busday_count(np.asarray(self), self.today()) + int(days)
        return np.array(day, dtype=np.int64)

    # 閏年
    def leapyear(self):
        year = self.year
        return np.array((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))

    def leapcount(self):
        year = self.year
        return int(np.count_nonzero((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0))))

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
