from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import numpy as np
from dateutil.parser import parse

from ..dev import _ArrayCommonMixin, _dt64_unit, _get_dt64_unit, _tm64_unit
from ..nptimedelta import NPTimedelta

__all__ = ["NPDate"]
_Word = [
    "NAT",
    b"NAT",
    "NaT",
    b"NaT",
    "nat",
    b"nat",
    "NOW",
    b"NOW",
    "now",
    b"now",
    "TODAY",
    b"TODAY",
    "today",
    b"today",
]


class NPDate(_ArrayCommonMixin):
    _element_type = np.datetime64
    _default_dtype = np.dtype("datetime64[D]")

    def __new__(
        cls,
        data,
        /,
        dtype="datetime64[D]",
        *,
        localtime=False,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        def _func(x):
            try:
                if x in _Word:
                    return x
                elif isinstance(x, str | np.str_):
                    return parse(x)
                else:
                    return x
            except:
                return None

        if not isinstance(copy, bool):
            copy = True
        resolved = cls._resolve_dtype(_dt64_unit(dtype))
        date = np.vectorize(_func, otypes=[resolved])(np.asarray(data))
        if localtime:
            try:
                date = date + _local_utc_difference(dtype)
            except OverflowError as e:
                raise OverflowError(e)
        obj = np.asarray(date, copy=copy).view(cls)
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

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __iadd__ = __add__

    def __sub__(self, value):
        if isinstance(value, datetime | date):
            result = np.subtract(self.__array__(), np.datetime64(value))
            if np.ndim(result) == 0:
                return result
            return np.array(result)
        elif isinstance(value, np.ndarray | np.datetime64) and value.dtype.kind == "M":
            result = np.subtract(self, value)
            if np.ndim(result) == 0:
                return result
            return np.array(result)
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __isub__ = __sub__

    def __eq__(self, value):
        return np.array(np.equal(self, _to_datetime64(value)), dtype=np.bool_)

    def __ne__(self, value):
        return np.array(np.not_equal(self, _to_datetime64(value)), dtype=np.bool_)

    def __lt__(self, value):
        return np.array(np.less(self, _to_datetime64(value)), dtype=np.bool_)

    def __le__(self, value):
        return np.array(np.less_equal(self, _to_datetime64(value)), dtype=np.bool_)

    def __gt__(self, value):
        return np.array(np.greater(self, _to_datetime64(value)), dtype=np.bool_)

    def __ge__(self, value):
        return np.array(np.greater_equal(self, _to_datetime64(value)), dtype=np.bool_)

    def __int__(self):
        return int(self.astype(int).item())

    def __float__(self):
        return float(self.astype(float).item())

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
        return np.array(
            (self - self.astype("datetime64[M]")).astype(np.uint8) + 1, np.uint8
        )

    # 判定
    def isnat(self):
        return np.array(np.isnat(self), np.bool_)

    # 変換
    def astype(self, dtype, copy=True):
        if not isinstance(copy, bool):
            copy = True
        try:
            dtype = np.dtype(_dt64_unit(dtype))
        except:
            dtype = np.dtype(dtype)
        if dtype.kind == "M":
            return NPDate(
                np.asarray(self),
                dtype=dtype,
                min_ndim=self.min_ndim,
                max_ndim=self.max_ndim,
                copy=copy,
            )
        return self.__array__(dtype, copy=copy)

    def to_datetime(self):
        return self.data.astype(datetime)

    def to_date(self):
        return self.data.astype(date)

    def to_str(self):
        return np.array(np.datetime_as_string(self), dtype=np.str_)

    def to_timezone(self, timezone, /):
        try:
            return self + np.timedelta64(
                datetime.now(ZoneInfo("UTC"))
                .astimezone(ZoneInfo(timezone))
                .utcoffset(),
                _get_dt64_unit(self.dtype),
            )
        except:
            return self

    def strftime(self, format):
        def func(arr, format):
            return arr.strftime(format)

        return np.array(np.vectorize(func)(self.tolist(), format))

    # 範囲
    @classmethod
    def arange(cls, start, stop, /, step=1, *, dtype="D"):
        dtype = _get_dt64_unit(dtype)
        start = _obj_to_datetime64(start, dtype).astype("int64")
        stop = _obj_to_datetime64(stop, dtype).astype("int64")
        if stop < start:
            start, stop = stop, start
        if isinstance(step, timedelta):
            step = np.timedelta64(step)
        dtype = _dt64_unit(dtype)
        result = np.asarray(
            np.arange(start, stop, step=step), dtype=_dt64_unit(dtype)
        ).view(cls)
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
            result, step = np.linspace(
                start, stop, num, endpoint, retstep, np.int64, axis
            )
            result = np.asarray(result, dtype=_dt64_unit(dtype)).view(cls)
            result._dtype = result.dtype
            return result, step.astype(_tm64_unit(dtype))
        else:
            result = np.linspace(start, stop, num, endpoint, retstep, np.int64, axis)
            result = np.asarray(result, dtype=_dt64_unit(dtype)).view(cls)
            result._dtype = result.dtype
            return result

    def range(self):
        return np.min(self), np.max(self)

    # 日付差
    def diff_today(self, days=False):
        if not isinstance(days, bool):
            days = False
        return self.astype("datetime64[D]") - np.datetime64("today", "D") + int(days)

    def diff_tfyear(self):
        return self - self.astype("datetime64[Y]").astype("datetime64[D]")

    def diff_teyear(self):
        return (self.astype("datetime64[Y]") + 1).astype("datetime64[D]") - 1 - self

    def diff_tfmonth(self):
        return self - self.astype("datetime64[M]").astype("datetime64[D]")

    def diff_temonth(self):
        return (self.astype("datetime64[M]") + 1).astype("datetime64[D]") - 1 - self

    @classmethod
    def today(cls, localtime=False):
        result = np.asarray(np.datetime64("today"), dtype="datetime64[D]").view(cls)
        dtype = result.dtype
        if localtime:
            result = result + _local_utc_difference(dtype)
        result._dtype = dtype
        return result

    @classmethod
    def utctoday(cls):
        result = np.asarray(np.datetime64("today"), dtype="datetime64[D]").view(cls)
        result._dtype = result.dtype
        return result

    @classmethod
    def now(cls, localtime=False):
        result = np.asarray(np.datetime64("now"), dtype="datetime64[s]").view(cls)
        dtype = result.dtype
        if localtime:
            result = result + _local_utc_difference(dtype)
        result._dtype = dtype
        return result

    @classmethod
    def utcnow(cls):
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
        m = self.month
        flag = m <= 2
        y, m = np.where(flag, self.year - 1, self.year), np.where(flag, m + 12, m)
        return (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + self.day) % 7

    def begin_month_weekday(self):
        m = self.month
        flag = m <= 2
        y, m = np.where(flag, self.year - 1, self.year), np.where(flag, m + 12, m)
        return (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + 1) % 7

    def end_month_weekday(self):
        dates = NPDate(
            self.astype("datetime64[M]") + np.timedelta64(1, "M"), "M"
        ) - np.timedelta64(1, "D")
        return dates.weekday()

    def week_name(self):
        week = self.weekday()
        return np.array(
            np.select(
                [week == i for i in range(7)],
                [
                    "Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                ],
                default="",
            ),
            dtype=np.str_,
        )

    # 閏年
    def leapyear(self):
        year = self.year
        return np.array((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))

    def leapcount(self):
        year = self.year
        return int(
            np.count_nonzero((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))
        )

    @property
    def dtypeunit(self):
        dy = str(self._dtype)
        place = dy.find("[") + 1
        if place == 0:
            return dy
        return dy[(place) : (len(dy) - 1)]


def _obj_to_datetime64(obj, dtype):
    if isinstance(obj, str):
        return np.datetime64(
            obj if obj in ["TODAY", "today", "NOW", "now"] else parse(obj), dtype
        )
    elif isinstance(obj, np.str_):
        obj = str(obj)
        return np.datetime64(
            obj if obj in ["TODAY", "today", "NOW", "now"] else parse(obj), dtype
        )
    elif isinstance(obj, np.datetime64):
        return obj.astype(_dt64_unit(dtype))
    elif isinstance(obj, datetime | date):
        return np.datetime64(obj).astype(_dt64_unit(dtype))
    else:
        raise TypeError


def _to_datetime64(value):
    if isinstance(value, datetime | date):
        return np.datetime64(value)
    return value


def _local_utc_difference(dtype):
    return np.timedelta64(
        datetime.now().astimezone().utcoffset(), _get_dt64_unit(dtype)
    )
