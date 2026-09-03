from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import numpy as np
from dateutil.parser import parse

import sgg.nparray.dev as snd
from sgg.exceptions import ShapeError

__all__ = ["NPDate"]
_Word = frozenset(
    {
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
    }
)


class NPDate(snd._ArrayCommonMixin):
    """`np.ndarray`を継承したdatetime64型の配列クラス"""

    _element_type = (np.datetime64,)
    _default_dtype = np.dtype("datetime64[D]")

    def __new__(
        cls,
        obj,
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
        resolved = cls._resolve_dtype(
            "datetime64[D]" if dtype is None else snd._dt64_unit(dtype)
        )
        obj = np.asarray(
            np.vectorize(_func, otypes=[resolved])(np.asarray(obj)), copy=copy
        ).view(cls)
        obj._dtype = resolved
        if isinstance(d_ndim, int):
            obj._min_ndim = obj._max_ndim = d_ndim
        else:
            obj._min_ndim = min_ndim
            obj._max_ndim = max_ndim
        cls._validate_ndim(obj, obj._min_ndim, obj._max_ndim)
        return obj

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __iadd__ = __add__

    def __radd__(self, value):
        result = np.asarray(np.add(value, self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __sub__(self, value):
        if isinstance(value, datetime | date):
            return np.subtract(self, np.datetime64(value))
        elif isinstance(value, np.datetime64 | np.timedelta64) or (
            isinstance(value, np.ndarray) and value.dtype.kind in ["M", "m"]
        ):
            return np.subtract(self, value)
        elif isinstance(value, timedelta):
            return np.subtract(self, np.timedelta64(value, self.dtypeunit))
        return NotImplemented

    __isub__ = __sub__

    def __rsub__(self, value):
        if isinstance(value, datetime | date):
            return np.subtract(np.datetime64(value), self)
        elif isinstance(value, np.datetime64) or (
            isinstance(value, np.ndarray) and value.dtype.kind == "M"
        ):
            return np.subtract(value, self)
        return NotImplemented

    def __eq__(self, value):
        return np.equal(self, _to_datetime64(value))

    def __ne__(self, value):
        return np.not_equal(self, _to_datetime64(value))

    def __lt__(self, value):
        return np.less(self, _to_datetime64(value))

    def __le__(self, value):
        return np.less_equal(self, _to_datetime64(value))

    def __gt__(self, value):
        return np.greater(self, _to_datetime64(value))

    def __ge__(self, value):
        return np.greater_equal(self, _to_datetime64(value))

    # 日付
    @property
    def year(self):
        return self.astype("datetime64[Y]").astype(np.int64) + 1970

    @property
    def month(self):
        return np.mod(self.astype("datetime64[M]").astype(np.int8), 12) + 1

    @property
    def day(self):
        return (self - self.astype("datetime64[M]")).astype(np.uint8) + 1

    # 判定
    def isnat(self):
        return np.isnat(self)

    # 変換
    def astype(self, dtype, copy=True):
        if not isinstance(copy, bool):
            copy = True
        try:
            dtype = np.dtype(snd._dt64_unit(dtype))
        except:
            dtype = np.dtype(dtype)
        if dtype.kind == "M":
            return np.asarray(self, dtype=dtype, copy=copy).view(type(self))
        return self.__array__(dtype, copy=copy)

    def to_datetime(self):
        return self.data.astype(datetime)

    def to_date(self):
        return self.data.astype(date)

    def to_str(self):
        result = np.datetime_as_string(self)
        if np.ndim(result) == 0:
            return result
        return result.__array__()

    def to_timezone(self, timezone, /):
        try:
            return self + np.timedelta64(
                datetime.now(ZoneInfo("UTC"))
                .astimezone(ZoneInfo(timezone))
                .utcoffset(),
                snd._get_dt64_unit(self.dtype),
            )
        except:
            return self

    def strftime(self, format):
        return np.vectorize(lambda i, format: i.strftime(format), otypes=[np.str_])(
            self.tolist(), format
        )

    # 範囲
    @classmethod
    def arange(cls, start, stop, /, step=1, dtype=None):
        if dtype is None:
            if isinstance(step, np.timedelta64 | timedelta):
                if isinstance(step, np.timedelta64):
                    dtype = snd._get_dt64_unit(_dtypeunit(step.dtype))
                elif isinstance(step, timedelta):
                    dtype = snd._get_dt64_unit(_dtypeunit(np.timedelta64(step).dtype))
                start = _obj_to_datetime64(start, dtype)
                stop = _obj_to_datetime64(stop, dtype)
            else:
                start = _obj_to_datetime64(start)
                stop = _obj_to_datetime64(stop)
                dtype = np.result_type(start.dtype, stop.dtype)
        if np.asarray(step).dtype.kind not in ["m", "b", "i", "u"]:
            raise TypeError
        if isinstance(step, timedelta):
            step = np.timedelta64(step)
        result = np.asarray(
            np.arange(start, stop, step=step), dtype=snd._dt64_unit(dtype)
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
        dtype = snd._get_dt64_unit(dtype)
        start = _obj_to_datetime64(start, dtype).astype("int64")
        stop = _obj_to_datetime64(stop, dtype).astype("int64")
        if stop < start:
            start, stop = stop, start
        if retstep:
            result, step = np.linspace(
                start, stop, num, endpoint, retstep, np.int64, axis
            )
            result = np.asarray(result, dtype=snd._dt64_unit(dtype)).view(cls)
            result._dtype = result.dtype
            return result, step.astype(snd._tm64_unit(dtype))
        else:
            result = np.linspace(start, stop, num, endpoint, retstep, np.int64, axis)
            result = np.asarray(result, dtype=snd._dt64_unit(dtype)).view(cls)
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
        return self.strftime("%A")

    # 閏年
    def leapyear(self):
        year = self.year
        return np.array((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))

    def leapcount(self):
        year = self.year
        return int(
            np.count_nonzero((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))
        )

    # dtype
    @property
    def dtypeunit(self):
        return _dtypeunit(self._dtype)

    def dtype_range(self):
        iinfo = np.iinfo(np.int64)
        result = np.asarray([iinfo.min + 1, iinfo.max]).view(type(self))
        result._dtype = result.dtype
        return result

    def dtype_max(self):
        result = np.asarray(np.datetime64(np.iinfo(np.int64).max, self.dtypeunit)).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def dtype_min(self):
        result = np.asarray(
            np.datetime64(np.iinfo(np.int64).min + 1, self.dtypeunit)
        ).view(type(self))
        result._dtype = result.dtype
        return result

    @classmethod
    def unit_range(cls, unit):
        iinfo = np.iinfo(np.int64)
        dtype = snd._get_dt64_unit(unit)
        return np.datetime64(iinfo.min + 1, dtype), np.datetime64(iinfo.max, dtype)

    @classmethod
    def unit_max(cls, unit):
        return np.datetime64(np.iinfo(np.int64).max, snd._get_dt64_unit(unit))

    @classmethod
    def unit_min(cls, unit):
        return np.datetime64(np.iinfo(np.int64).min + 1, snd._get_dt64_unit(unit))

    @classmethod
    def full(
        cls,
        fill_value,
        shape,
        dtype=None,
    ):
        snd._to_np_scalar(fill_value)
        if not snd._arrisuint(shape):
            raise ShapeError(shape)
        resolved = cls._resolve_dtype(snd._dt64_unit("D" if dtype is None else dtype))
        result = np.asarray(
            np.full(shape, _obj_to_datetime64(fill_value, resolved)), dtype=resolved
        ).view(cls)
        result._dtype = resolved
        return result


def _func(x):
    if x in _Word:
        return x
    if isinstance(x, str):
        try:
            return np.datetime64(x)
        except:
            try:
                return parse(str(x))
            except:
                return None
    if isinstance(x, np.str_):
        return _func(str(x))
    if isinstance(x, bytes | np.bytes_):
        return _func(x.decode())
    return x


def _obj_to_datetime64(obj, dtype=None):
    if dtype is None:
        if obj in _Word or isinstance(obj, datetime | date | int):
            return np.datetime64(obj)
        elif isinstance(obj, str | np.str_):
            return np.datetime64(_func(obj))
        raise TypeError
    if isinstance(obj, np.datetime64):
        return obj.astype(snd._dt64_unit(dtype))
    dtype = snd._get_dt64_unit(dtype)
    if obj in _Word or isinstance(obj, datetime | date | int | np.integer):
        return np.datetime64(obj, dtype)
    elif isinstance(obj, str | np.str_):
        return np.datetime64(_func(obj), dtype)
    raise TypeError


def _to_datetime64(value):
    if isinstance(value, datetime | date):
        return np.datetime64(value)
    return value


def _dtypeunit(dy):
    if not isinstance(dy, str):
        dy = str(dy)
    place = dy.find("[") + 1
    if place == 0:
        return dy
    return dy[(place) : (len(dy) - 1)]
