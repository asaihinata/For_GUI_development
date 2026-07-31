"""基本的な文字列の操作をするモジュール"""

import numpy as np
import numpy.strings as nps
from numpy.dtypes import StringDType

from ..dev import _ArrayCommonMixin, _int_co_check
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPString"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPString(_ArrayCommonMixin, np.ndarray):
    _element_type = (str, np.str_, bytes, np.bytes_, StringDType)
    _default_dtype = np.str_

    def __new__(
        cls,
        data,
        /,
        dtype=np.str_,
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(data, copy=copy).view(cls)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(dtype)
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
        result = np.asarray(nps.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    def __mul__(self, i):
        _int_co_check(i)
        if isinstance(self.dtypes, StringDType):
            result = np.asarray(nps.multiply(np.asarray(self), np.maximum(i, 0))).view(
                type(self)
            )
        else:
            result = nps.multiply(np.asarray(self), np.maximum(i, 0)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__
    __rmul__ = __mul__
    __imul__ = __mul__

    def __eq__(self, value):
        return NPBool(nps.equal(self, value))

    def __ne__(self, value):
        return NPBool(nps.not_equal(self, value))

    def append(self, val):
        result = np.asarray(nps.add(self, val)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def low(self):
        result = np.asarray(nps.lower(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def lower(self):
        result = np.asarray(nps.lower(self)).view(type(self))
        result._dtype = result.dtype
        return result

    @property
    def up(self):
        result = np.asarray(nps.upper(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def upper(self):
        result = np.asarray(nps.upper(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def max(self):
        return np.max(nps.str_len(self.data))

    def min(self):
        return np.min(nps.str_len(self.data))

    def stringlen(self):
        return NPNumber(np.vectorize(len)(self), dtype=np.uint64)

    def str_len(self):
        return NPNumber(nps.str_len(self), dtype=np.uint64)

    def replace(self, old, new):
        result = np.asarray(nps.replace(self, old, new)).view(type(self))
        result._dtype = result.dtype
        return result

    def center(self, width, fillchar=" "):
        result = np.asarray(nps.center(self, width, fillchar)).view(type(self))
        result._dtype = result.dtype
        return result

    def left(self, width, fillchar=" "):
        result = np.asarray(nps.ljust(self, width, fillchar)).view(type(self))
        result._dtype = result.dtype
        return result

    def right(self, width, fillchar=" "):
        result = np.asarray(nps.rjust(self, width, fillchar)).view(type(self))
        result._dtype = result.dtype
        return result

    def zerofill(self, width):
        result = nps.zfill(np.asarray(self), width).view(type(self))
        result._dtype = result.dtype
        return result

    def expandtabs(self, tabsize=8):
        result = np.asarray(nps.expandtabs(self, tabsize)).view(type(self))
        result._dtype = result.dtype
        return result

    def endswith(self, suffix, start=0, end=None):
        return NPBool(nps.endswith(self, suffix, start, end))

    def capitalize(self):
        result = np.asarray(nps.capitalize(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def title(self):
        result = np.asarray(nps.title(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def decode(self, encoding=None, errors=None):
        if not np.issubdtype(self.dtypes, np.bytes_):
            raise TypeError
        result = np.asarray(nps.decode(self, encoding, errors)).view(type(self))
        result._dtype = result.dtype
        return result

    def encode(self, encoding=None, errors=None):
        if self.dtype.kind not in {"U", "T"}:
            raise TypeError
        result = np.asarray(nps.encode(self, encoding, errors)).view(type(self))
        result._dtype = result.dtype
        return result

    def istitle(self):
        return NPBool(nps.istitle(self))

    def isnumeric(self):
        return NPBool(nps.isnumeric(self))

    def isdecimal(self):
        return NPBool(nps.isdecimal(self))

    def isalnum(self):
        return NPBool(nps.isalnum(self))

    def isspace(self):
        return NPBool(nps.isspace(self))

    def isupper(self):
        return NPBool(nps.isupper(self))

    @classmethod
    def randombytes(cls, length, seed=None):
        if not isinstance(length, int):
            raise TypeError("lengthにはint型を指定してください")
        if length < 1:
            raise ValueError("lengthには1以上の整数を指定してください")
        return cls(np.random.default_rng(seed).bytes(length), dtype=np.bytes_)
