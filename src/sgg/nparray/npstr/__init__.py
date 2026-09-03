"""基本的な文字列の操作をするモジュール"""

from re import sub

import numpy as np
import numpy.strings as nps
from numpy.dtypes import StringDType

from sgg.dev import _tonparray

from ..dev import _ArrayCommonMixin

__all__ = ["NPString"]


class NPString(_ArrayCommonMixin):
    """`np.ndarray`を継承した文字列型の配列クラス"""

    _element_type = (np.str_, np.bytes_, StringDType())
    _default_dtype = np.str_

    def __new__(
        cls,
        obj,
        /,
        dtype=None,
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(obj, copy=copy).view(cls)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(dtype)
            obj = np.asarray(obj, dtype=resolved, copy=copy).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        if isinstance(d_ndim, int):
            obj._min_ndim = obj._max_ndim = d_ndim
        else:
            obj._min_ndim = min_ndim
            obj._max_ndim = max_ndim
        cls._validate_ndim(obj, obj._min_ndim, obj._max_ndim)
        return obj

    def __add__(self, value):
        if not isinstance(self._dtype, StringDType) and not np.issubdtype(
            self._dtype, _tonparray(value).dtype
        ):
            raise TypeError
        result = np.asarray(nps.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __iadd__ = __add__

    def __add__(self, value):
        if not isinstance(self._dtype, StringDType) and not np.issubdtype(
            self._dtype, _tonparray(value).dtype
        ):
            raise TypeError
        result = np.asarray(nps.add(value, self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __mul__(self, i):
        if np.asarray(i).dtype.kind in ["b", "i", "u"]:
            result = nps.multiply(np.asarray(self), np.maximum(i, 0))
            if np.issubdtype(self._dtype, StringDType()):
                result = np.asarray(result)
            result = result.view(type(self))
            result._dtype = result.dtype
            return result
        return NotImplemented

    __imul__ = __mul__

    def __mod__(self, value):
        result = np.asarray(nps.mod(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __imod__ = __mod__

    def __eq__(self, value):
        return nps.equal(self, value)

    def __ne__(self, value):
        return nps.not_equal(self, value)

    def append(self, val, /):
        result = self.__add__(val)
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
        result = np.vectorize(len)(self)
        if self.zero_ndim:
            return result
        return result.__array__()

    def str_len(self):
        return nps.str_len(self)

    def replace(self, old, new):
        result = np.asarray(nps.replace(self.__array__(), old, new)).view(type(self))
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

    def expandtabs(self, tabsize=8):
        result = np.asarray(nps.expandtabs(self, tabsize)).view(type(self))
        result._dtype = result.dtype
        return result

    def endswith(self, suffix, start=0, end=None):
        return nps.endswith(self, suffix, start, end)

    def startswith(self, prefix, start=0, end=None):
        return nps.startswith(self, prefix, start, end)

    def capitalize(self):
        result = np.asarray(nps.capitalize(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def title(self):
        result = np.asarray(nps.title(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def find(self, sub, start=0, end=None):
        return nps.find(self, sub, start=start, end=end)

    def rfind(self, sub, start=0, end=None):
        return nps.rfind(self, sub, start=start, end=end)

    def count(self, sub, start=0, end=None):
        return nps.count(self, sub, start=start, end=end)

    def decode(self, encoding=None, errors=None):
        if not np.issubdtype(self._dtype, np.bytes_):
            raise TypeError
        result = np.asarray(nps.decode(self, encoding, errors)).view(type(self))
        result._dtype = result.dtype
        return result

    def encode(self, encoding=None, errors=None):
        if self._dtype.kind not in ["U", "T"]:
            raise TypeError
        result = np.asarray(nps.encode(self, encoding, errors)).view(type(self))
        result._dtype = result.dtype
        return result

    # 判定
    def istitle(self):
        return nps.istitle(self)

    def isnumeric(self):
        return nps.isnumeric(self)

    def isdecimal(self):
        return nps.isdecimal(self)

    def isalnum(self):
        return nps.isalnum(self)

    def isspace(self):
        return nps.isspace(self)

    def isupper(self):
        return nps.isupper(self)

    # 正規表現
    def sub(self, pattern, repl):
        result = np.asarray(np.vectorize(lambda s: sub(pattern, repl, s))(self)).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    @classmethod
    def randombytes(cls, length, seed=None):
        if not isinstance(length, int):
            raise TypeError("lengthにはint型を指定してください")
        if length < 1:
            raise ValueError("lengthには1以上の整数を指定してください")
        return cls(np.random.default_rng(seed).bytes(length), dtype=np.bytes_)
