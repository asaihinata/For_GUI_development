"""基本的な文字列の操作をするモジュール"""

import numpy as np
import numpy.strings as nps

from ...isdtype import strDtype
from ..nparray import NPArray
from ..npnumber import NPNumber

__all__ = ["NPString"]


class NPString(NPArray):
    _element_type = (str, np.character, np.str_, np.bytes_)

    def __new__(cls, data, dtype=np.str_, d_ndim=None, min_ndim=None, max_ndim=None):
        if strDtype(dtype):
            raise TypeError("dtypeには文字列の型を指定してください")
        return super().__new__(cls, data, dtype, d_ndim, min_ndim, max_ndim)
    @classmethod
    def __instancecheck__(cls,instance):
        return isinstance(instance,NPNumber)
    def __add__(self, other):
        result = np.add(np.asarray(self), other).view(type(self))
        result._dtype = result.dtype
        return result

    def __mul__(self, i):
        if not isinstance(i, int):
            raise TypeError("int型で指定してください")
        result = nps.multiply(np.asarray(self), i).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__
    __rmul__ = __mul__
    __imul__ = __mul__

    def __eq__(self, value):
        return super().__eq__(value)

    def __ne__(self, value):
        return super().__ne__(value)

    def append(self, val):
        result = nps.add(np.asarray(self), val).view(type(self))
        result._dtype = result.dtype
        return result

    def low(self):
        result = nps.lower(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def upper(self):
        result = nps.upper(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def stringlen(self):
        return NPNumber(np.vectorize(len)(self), dtype=np.uint64)

    def str_len(self):
        return NPNumber(nps.str_len(self), dtype=np.uint64)

    def replace(self, old, new):
        result = nps.replace(self.data, old, new).view(type(self))
        result._dtype = result.dtype
        return result
