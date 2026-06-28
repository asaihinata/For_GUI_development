from datetime import date, datetime

from dateutil.parser import parse
import numpy as np

from ..nparray import NPArray
from ._typing import serchDtype

__all__ = ["Formatconversion"]


class Formatconversion(NPArray):
    _element_type = (np.datetime64, datetime, date)

    def __new__(
        cls,
        data,
        dtype="datetime64[D]",
        yearfirst=False,
        dayfirst=False,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
    ):
        if not isinstance(data, np.ndarray):
            data = np.array(data)
        if not isinstance(yearfirst, bool):
            yearfirst = False
        if not isinstance(dayfirst, bool):
            dayfirst = False
        dtype = np.dtype(serchDtype(dtype))
        func = np.vectorize(
            lambda strs, yearfirst, dayfirst: str(
                parse(str(strs), yearfirst=yearfirst, dayfirst=dayfirst)
            )
        )
        return super().__new__(
            cls,
            np.array(
                [func(i, yearfirst, dayfirst) for i in np.nditer(data)], dtype=dtype
            ).reshape(data.shape),
            dtype,
            d_ndim,
            min_ndim,
            max_ndim,
        )
