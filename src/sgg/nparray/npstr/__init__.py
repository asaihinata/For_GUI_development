"""基本的な文字列の操作をするモジュール"""

import numpy as np
import numpy.strings as nps
from numpy.dtypes import StringDType

from ..dev import _ArrayCommonMixin, _int_co_check

__all__ = ["NPString"]


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
        return np.array(nps.equal(self, value), dtype=np.bool_)

    def __ne__(self, value):
        return np.array(nps.not_equal(self, value), dtype=np.bool_)

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

    def len_max(self):
        return np.max(nps.str_len(self))

    def len_min(self):
        return np.min(nps.str_len(self))

    def stringlen(self):
        return np.array(np.vectorize(len)(self), dtype=np.uint64)

    def str_len(self):
        return np.array(nps.str_len(self), dtype=np.uint64)

    def replace(self, old, new):
        result = nps.replace(np.asarray(self), old, new).view(type(self))
        result._dtype = result.dtype
        return result

    def slices(self, start=None, stop=np._NoValue, step=None):
        result = np.asarray(nps.slice(self, start, stop, step)).view(type(self))
        result._dtype = result.dtype
        return result

    def strip(self, char=None):
        result = np.asarray(nps.strip(self, char)).view(type(self))
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
        return np.array(nps.endswith(self, suffix, start, end), dtype=np.bool_)

    def startswith(self, prefix, start=0, end=None):
        return np.array(nps.startswith(self, prefix, start, end), dtype=np.bool_)

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
        return np.array(nps.istitle(self), dtype=np.bool_)

    def isnumeric(self):
        return np.array(nps.isnumeric(self), dtype=np.bool_)

    def isdecimal(self):
        return np.array(nps.isdecimal(self), dtype=np.bool_)

    def isalnum(self):
        return np.array(nps.isalnum(self), dtype=np.bool_)

    def isspace(self):
        return np.array(nps.isspace(self), dtype=np.bool_)

    def isupper(self):
        return np.array(nps.isupper(self), dtype=np.bool_)

    @classmethod
    def randombytes(cls, length, seed=None):
        if not isinstance(length, int):
            raise TypeError("lengthにはint型を指定してください")
        if length < 1:
            raise ValueError("lengthには1以上の整数を指定してください")
        return cls(np.random.default_rng(seed).bytes(length), dtype=np.bytes_)
