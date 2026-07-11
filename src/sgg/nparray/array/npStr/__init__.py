"""基本的な文字列の操作をするモジュール"""

import numpy as np
import numpy.strings as nps

from ..dev import _ArrayShapeMixin, _int_co_check, _normalize_axis
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPString"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPString(_ArrayShapeMixin, np.ndarray):
    _element_type = (str, np.character, np.str_, np.bytes_)
    _default_dtype = np.str_

    def __new__(cls, data, dtype=np.str_, d_ndim=None, min_ndim=None, max_ndim=None):
        resolved = cls._resolve_dtype(dtype)
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

    def __array__(self, dtype=np.str_, copy=None):
        return super().__array__(dtype, copy=copy)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPString) else x for x in inputs
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

    def __add__(self, value):
        result = nps.add(np.asarray(self), value).view(type(self))
        result._dtype = result.dtype
        return result

    def __mul__(self, i):
        _int_co_check(i)
        result = nps.multiply(np.asarray(self), np.maximum(i, 0)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__
    __rmul__ = __mul__
    __imul__ = __mul__

    def __ne__(self, value):
        return NPBool(nps.not_equal(np.asarray(self), value))

    def __eq__(self, value):
        return NPBool(nps.equal(np.asarray(self), value))

    def append(self, val):
        result = np.asarray(nps.add(self, val)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def low(self):
        result = nps.lower(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def lower(self):
        result = nps.lower(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def up(self):
        result = nps.upper(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def upper(self):
        result = nps.upper(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def max(self, axis=None):
        if axis is not None:
            axis=_normalize_axis(axis,self.ndim,"max")
        return np.max(nps.str_len(self.data), axis=axis)

    def min(self, axis=None):
        if axis is not None:
            axis=_normalize_axis(axis,self.ndim,"min")
        return np.min(nps.str_len(self.data), axis=axis)

    def stringlen(self,axis=None):
        if axis is None:
            return NPNumber(np.vectorize(len)(self), dtype=np.uint64)
        def _lenfunc(a):
            return np.vectorize(len)(a)
        return NPNumber(np.apply_along_axis(_lenfunc,_normalize_axis(axis,self.ndim,"stringlen"),self.data), dtype=np.uint64)

    def str_len(self,axis=None):
        if axis is None:
            return NPNumber(nps.str_len(self), dtype=np.uint64)
        def _lenfunc(a):
            return nps.str_len(a)
        return NPNumber(np.apply_along_axis(_lenfunc,_normalize_axis(axis,self.ndim,"str_len"),self.data), dtype=np.uint64)

    def replace(self, old, new):
        result = nps.replace(np.asarray(self), old, new).view(type(self))
        result._dtype = result.dtype
        return result

    def center(self, width, fillchar=" "):
        result = nps.center(np.asarray(self), width, fillchar).view(type(self))
        result._dtype = result.dtype
        return result

    def left(self, width, fillchar=" "):
        result = nps.ljust(np.asarray(self), width, fillchar).view(type(self))
        result._dtype = result.dtype
        return result

    def right(self, width, fillchar=" "):
        result = nps.rjust(np.asarray(self), width, fillchar).view(type(self))
        result._dtype = result.dtype
        return result

    def zerofill(self, width):
        result = nps.zfill(np.asarray(self), width).view(type(self))
        result._dtype = result.dtype
        return result

    def expandtabs(self, tabsize=4):
        result = nps.expandtabs(np.asarray(self), tabsize).view(type(self))
        result._dtype = result.dtype
        return result

    def endswith(self, suffix, start=0, end=None):
        return NPBool(nps.endswith(np.asarray(self), suffix, start, end))
