import numpy as np
import numpy.strings as nps

from ...isdtype import strDtype
from ..nparray import NPArray

__all__ = ["NPString"]


class NPString(NPArray):
    def __init__(self, data, dtype=np.str_, depth_limit=None):
        if strDtype(dtype):
            raise TypeError("dtypeには文字列の型を指定してください")
        super().__init__(data, dtype, depth_limit)

    def __iter__(self):
        return super().__iter__()

    def __len__(self):
        return super().__len__()

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __contains__(self, item):
        return super().__contains__(item)

    def __reversed__(self):
        return super().__reversed__()

    def __array__(self, dtype=None, copy=None):
        return super().__array__(dtype, copy)

    def __repr__(self):
        return f"NPString({self.data})"

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if method == "__call__":
            args = [x.data if isinstance(x, NPString) else x for x in args]
            result = ufunc(*args, **kwargs)
            if isinstance(result, np.ndarray):
                return NPString(result)
            return result
        return NotImplemented

    def __add__(self, other):
        self.data = nps.add(self.data, self.___datas(other))
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("int型で指定してください")
        self.data = nps.multiply(self.data, other)
        return self

    __radd__ = __add__
    __rmul__ = __mul__
    __iadd__ = __add__
    __imul__ = __mul__

    def __eq__(self, value):
        return np.equal(self.data, self.___datas(value))

    def __ne__(self, value):
        return np.not_equal(self.data, self.___datas(value))

    def ___datas(self, data):
        return data.data if isinstance(data, NPString) else data

    @property
    def T(self):
        self.data = self.data.T
        return self

    def append(self, val):
        self.data = np.append(self.data, self.___datas(val))
        return self

    def low(self):
        self.data = nps.lower(self.data)
        return self

    def upper(self):
        self.data = nps.upper(self.data)
        return self

    def stringlen(self):
        return np.vectorize(len)(self.data)

    def str_len(self):
        return nps.str_len(self.data)

    def replace(self, old, new):
        self.data = nps.replace(self.data, old, new)
        return self
