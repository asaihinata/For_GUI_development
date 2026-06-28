"""基本的な計算をするモジュール"""

import numpy as np

from ...isdtype import numberdDtype, numberDtype
from ..nparray import NPArray

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
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPNumber(NPArray):
    _element_type = (int, float, np.number)

    def __new__(cls, data, dtype=np.float64, d_ndim=None, min_ndim=None, max_ndim=None):
        if numberDtype(dtype):
            raise TypeError("dtypeには数値型を指定してください")
        return super().__new__(cls, data, dtype, d_ndim, min_ndim, max_ndim)

    def __array_function__(self, func, types, args, kwargs):
        if func in HANDLED_FUNCTIONS:
            return HANDLED_FUNCTIONS[func](*args, **kwargs)
        return super().__array_function__(func, types, args, kwargs)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPNumber) else x for x in inputs
        )
        result = getattr(ufunc, method)(*raw_inputs, **kwargs)

        if result is NotImplemented:
            return NotImplemented

        if isinstance(result, np.ndarray):
            result = result.view(type(self))
            result._dtype = getattr(inputs[0], "_dtype", None)

        return result

    @classmethod
    def __instancecheck__(cls, instance):
        return isinstance(instance, NPNumber)

    def __iter__(self):
        return super().__iter__()

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __contains__(self, item):
        return super().__contains__(item)

    def __reversed__(self):
        return super().__reversed__()

    def __repr__(self):
        return super().__repr__()

    def __abs__(self):
        result = np.abs(np.asarray(self)).view(type(self))
        result._dtype = result.dtype
        return result

    def __add__(self, other):
        result = np.add(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    def __sub__(self, other):
        result = np.subtract(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    def __mul__(self, other):
        result = np.multiply(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    def __truediv__(self, other):
        result = np.true_divide(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    def __floordiv__(self, other):
        result = np.floor_divide(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    def __pow__(self, other):
        result = np.power(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __iadd__ = __add__
    __rsub__ = __sub__
    __isub__ = __sub__
    __rmul__ = __mul__
    __imul__ = __mul__
    __rtruediv__ = __truediv__
    __itruediv__ = __truediv__

    def __mod__(self, other):
        result = np.mod(np.asarray(self), _datas(other)).view(type(self))
        result._dtype = result.dtype
        return result

    def __eq__(self, value):
        return np.equal(np.asarray(self), value)

    def __ne__(self, value):
        return np.not_equal(np.asarray(self), value)

    def __lt__(self, other):
        return np.less(np.asarray(self), other)

    def __le__(self, other):
        return np.less_equal(np.asarray(self), other)

    def __gt__(self, other):
        return np.greater(np.asarray(self), other)

    def __ge__(self, other):
        return np.greater_equal(np.asarray(self), other)

    @property
    def sturgesval(self):
        return 1 + np.log2(self.size)

    def cussum(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = np.array(
            [
                j + np.insert(j, 0, 0)[:-1]
                for i in range(0, len(datas), splices)
                for j in [datas[i : i + splices]]
            ]
        ).view(type(self))
        result._dtype = result.dtype
        return result

    def cumprod(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = np.array(
            [
                j * np.insert(j, 0, 0)[:-1]
                for i in range(0, len(datas), splices)
                for j in [datas[i : i + splices]]
            ]
        ).view(type(self))
        result._dtype = result.dtype
        return result

    def percentile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.asarray(np.percentile(self, q, axis=axis, method=method)).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def quantile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.asarray(np.quantile(self.data, q, axis=axis, method=method)).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def ratio(self, axis=None):
        return (self.data / np.sum(self.data, axis=axis, keepdims=True)) * 100

    def zero_check(self):
        return self.data == 0


def _datas(data):
    if numberdDtype(data):
        return data
    raise TypeError("数値の型を指定してください")
