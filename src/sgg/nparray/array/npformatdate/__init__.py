from datetime import date, datetime

import numpy as np
from dateutil.parser import parse

from sgg.typing import serchDtype

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin
from ..npbool import NPBool

__all__ = ["NPFormatDate"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPFormatDate(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = (np.datetime64, datetime, date)
    _default_dtype = "datetime64[D]"

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
        resolved = cls._resolve_dtype(dtype)
        obj = np.asarray(
            np.array(
                [func(i, yearfirst, dayfirst) for i in np.nditer(data)], dtype=dtype
            ).reshape(data.shape),
            dtype=resolved,
        ).view(cls)
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
        if func in HANDLED_FUNCTIONS:
            return HANDLED_FUNCTIONS[func](*args, **kwargs)
        return super().__array_function__(func, types, args, kwargs)

    def __ne__(self, value):
        return NPBool(np.not_equal(np.asarray(self), value))

    def __eq__(self, value):
        return NPBool(np.equal(np.asarray(self), value))
