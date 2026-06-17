"""基本的な計算をするモジュール"""

import numpy as np

from ..dtype import numberDtype
from ..npArray import NPArray

__all__ = ["NPNumber"]
method_list = [
    "inverted_cdf",
    "averaged_inverted_cdf",
    "closest_observation",
    "interpolated_inverted_cdf",
    "hazen",
    "weibull",
    "linear",
    "median_unbiased",
    "normal_unbiased",
]


class NPNumber(NPArray):
    def __init__(self, data, dtype=np.float64, depth_limit=None):
        if not numberDtype(dtype):
            raise TypeError("dtypeには数値型を指定してください")
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
        return f"NPNumber({self.data})"

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if method == "__call__":
            args = [x.data if isinstance(x, NPNumber) else x for x in args]
            result = ufunc(*args, **kwargs)
            if isinstance(result, np.ndarray):
                return NPNumber(result)
            return result
        return NotImplemented

    def __abs__(self):
        self.data = np.abs(self.data)
        return self

    def __add__(self, other):
        self.data = self.data + __datas(other)
        return self

    def __sub__(self, other):
        self.data = self.data - __datas(other)
        return self

    def __mul__(self, other):
        self.data = self.data * __datas(other)
        return self

    def __truediv__(self, other):
        self.data = self.data / __datas(other)
        return self

    def __floordiv__(self, other):
        self.data = self.data // __datas(other)
        return self

    def __pow__(self, other):
        self.data = np.power(self.data, __datas(other))
        return self

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __iadd__ = __add__
    __isub__ = __sub__
    __imul__ = __mul__
    __itruediv__ = __truediv__

    def __eq__(self, value):
        return np.equal(self.data, __datas(value))

    def __ne__(self, value):
        return np.not_equal(self.data, __datas(value))

    def __lt__(self, other):
        return np.less(self.data, __datas(other))

    def __le__(self, other):
        return np.less_equal(self.data, __datas(other))

    def __gt__(self, other):
        return np.greater(self.data, __datas(other))

    def __ge__(self, other):
        return np.greater_equal(self.data, __datas(other))

    def __mod__(self, other):
        self.data = self.data % __datas(other)
        return self

    def __neg__(self):
        self.data = -self.data
        return self

    def __pos__(self):
        self.data = +self.data
        return self

    @property
    def T(self):
        self.data = self.data.T
        return self

    def sum(self):
        return np.sum(self.data)

    def median(self):
        return np.median(self.data)

    def var(self):
        return np.var(self.data)

    def max(self):
        return np.max(self.data)

    def min(self):
        return np.min(self.data)

    def mean(self):
        return np.mean(self.data)

    def std(self):
        return np.std(self.data)

    def pow2(self):
        return np.power(self.data, 2)

    def deviation(self):
        data = self.data
        return ((10 / np.std(data)) * (self.data - np.mean(data))) + 50

    def log(self):
        return np.log(self.data)

    def log10(self):
        return np.log10(self.data)

    def log2(self):
        return np.log2(self.data)

    def log1p(self):
        return np.log1p(self.data)

    def degree(self):
        return np.degrees(self.data)

    def radian(self):
        return np.radians(self.data)

    def sturgesval(self):
        return 1 + np.log2(self.size)

    def logx(self, x):
        if not isinstance(x, int | float):
            raise TypeError("xには数値の型を指定してください")
        elif x < 0:
            raise ValueError("xには0より大きい値を指定してください")
        return np.log(self.data, dtype=self.dtype) / np.log(x, dtype=self.dtype)

    def mod(self, x):
        return np.mod(self.data, x)

    def divmod(self, x):
        return np.divmod(self.data, x)

    def pow(self, x):
        self.data = np.power(self.data, x)
        return self

    def sqrt(self, root=2):
        if root == 0:
            raise ZeroDivisionError("rootには0を指定できません")
        roots = 1 / root
        self.data = np.power(self.data, roots)
        return self

    def floor(self, digit=None):
        if digit == None:
            self.data = np.floor(self.data)
        else:
            pows = __digits(digit)
            self.data = np.floor(self.data * pows) / pows
        return self

    def trunc(self, digit=None):
        if digit == None:
            self.data = np.trunc(self.data)
        else:
            pows = __digits(digit)
            self.data = np.trunc(self.data * pows) / pows
        return self

    def ceil(self, digit=None):
        if digit == None:
            self.data = np.ceil(self.data)
        else:
            pows = __digits(digit)
            self.data = np.ceil(self.data * pows) / pows
        return self

    def round(self, digit=None):
        if digit == None:
            self.data = np.round(self.data)
        else:
            pows = __digits(digit)
            self.data = np.round(self.data * pows) / pows
        return self

    def cussum(self):
        datas, shapes = self._flatten()
        splices = shapes[-1]
        self.data = np.array(
            [
                j + np.insert(j, 0, 0)[:-1]
                for i in range(0, len(datas), splices)
                for j in [datas[i : i + splices]]
            ]
        )
        return self

    def cumprod(self):
        datas, shapes = self._flatten()
        splices = shapes[-1]
        self.data = np.array(
            [
                j * np.insert(j, 0, 1)[:-1]
                for i in range(0, len(datas), splices)
                for j in [datas[i : i + splices]]
            ]
        )
        return self

    def percentile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.percentile(self.data, q, axis=axis, method=method)

    def quantile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        return np.quantile(self.data, q, axis=axis, method=method)

    def ratio(self, axis=None):
        return (self.data / np.sum(self.data, axis=axis, keepdims=True)) * 100

    def zero_check(self):
        return self.data == 0

    def ints(self):
        self.data = self.data.astype(int)
        return self

    def floats(self):
        self.data = self.data.astype(float)
        return self


def __digits(digit):
    if not isinstance(digit, int):
        raise TypeError("digitには整数型を指定してください")
    elif digit < 1:
        raise ValueError("digitには1以上の整数を指定してください")
    return np.pow(10, digit)


def __datas(data):
    if isinstance(data, np.ndarray):
        if not numberDtype(data):
            raise TypeError("numpy.ndarrayの型を数値の型にしてください")
        return data
    elif not isinstance(data, np.ndarray | NPNumber | int | float | complex):
        raise TypeError("NPNumber型か数値の型を指定してください")
    return data.data if isinstance(data, NPNumber) else data
