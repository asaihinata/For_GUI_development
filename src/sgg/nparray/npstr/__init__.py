"""基本的な文字列の操作をするモジュール"""

from re import sub

import numpy as np
import numpy.strings as nps
from numpy.dtypes import StringDType

from ..dev import _ArrayCommonMixin, _int_co_check

__all__ = ["NPString"]


class NPString(_ArrayCommonMixin):
    """`np.ndarray`を継承した文字列型の配列クラス"""

    _element_type = (str, np.str_, bytes, np.bytes_, StringDType)
    _default_dtype = np.str_

    def __new__(
        cls,
        obj,
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
        result = np.asarray(nps.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__

    def __mul__(self, i):
        _int_co_check(i)
        result = self.__array__(copy=False)
        if isinstance(self.dtypes, StringDType):
            result = np.asarray(nps.multiply(result, np.maximum(i, 0))).view(type(self))
        else:
            result = nps.multiply(result, np.maximum(i, 0)).view(type(self))
        result._dtype = result.dtype
        return result

    __rmul__ = __mul__
    __imul__ = __mul__

    def __mod__(self, value):
        result = np.asarray(nps.mod(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __imod__ = __mod__

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

    def find(self, sub, start=0, end=None):
        result = nps.find(self, sub, start=start, end=end)
        if np.isscalar(result):
            return np.int64(result.item())
        return result.__array__(np.int64)

    def rfind(self, sub, start=0, end=None):
        result = nps.rfind(self, sub, start=start, end=end)
        if np.isscalar(result):
            return np.int64(result.item())
        return result.__array__(np.int64)

    def count(self, sub, start=0, end=None):
        result = nps.count(self, sub, start=start, end=end)
        if np.isscalar(result):
            return np.uint64(result)
        return result.__array__(np.uint64)

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

    # 判定
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

    # 正規表現
    def sub(self, pattern, repl):
        return np.vectorize(lambda s: sub(pattern, repl, s))(self)

    @classmethod
    def randombytes(cls, length, seed=None):
        if not isinstance(length, int):
            raise TypeError("lengthにはint型を指定してください")
        if length < 1:
            raise ValueError("lengthには1以上の整数を指定してください")
        return cls(np.random.default_rng(seed).bytes(length), dtype=np.bytes_)
