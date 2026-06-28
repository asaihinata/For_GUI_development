from datetime import date, datetime, timezone

import numpy as np

from ..nparray import NPArray
from ..npnumber import NPNumber
from ._typing import serchDtype
from .formatconversion import Formatconversion

__all__ = ["NPDate"]


class NPDate(NPArray):
    _element_type = (Formatconversion, np.datetime64, datetime, date)

    def __new__(
        cls, data, dtype="datetime64[D]", d_ndim=None, min_ndim=None, max_ndim=None
    ):
        return super().__new__(cls, data, serchDtype(dtype), d_ndim, min_ndim, max_ndim)

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

    @classmethod
    def today(cls):
        return NPDate([np.datetime64("today")], dtype="datetime64[D]")

    @classmethod
    def now(cls):
        return NPDate([np.datetime64("now")], dtype="datetime64[h]")
