"""基本的な数値の操作をするモジュール"""

import numpy as np

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin
from ..npbool import NPBool

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


class NPNumber(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = (int, float, complex, np.number)
    _default_dtype = np.float64

    def __new__(cls, data, dtype=np.float64, d_ndim=None, min_ndim=None, max_ndim=None):
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

    def __array__(self, dtype=np.float64, copy=None):
        return super().__array__(dtype, copy=copy)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPNumber) else x for x in inputs
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

    def __lt__(self, value):
        return NPBool(super().__lt__(value))

    def __le__(self, value):
        return NPBool(super().__le__(value))

    def __gt__(self, value):
        return NPBool(super().__gt__(value))

    def __ge__(self, value):
        return NPBool(super().__ge__(value))

    def __getitem__(self, key: int | slice):
        size = self.size
        if size == 0:
            raise IndexError("空の配列にはアクセスできません")
        data = self.data.flatten()
        if isinstance(key, int):
            if key == size:
                return data[size - 1]
            elif -size <= key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return data[key]
        raise TypeError("keyにはintまたはsliceを指定してください")

    @property
    def sturgesval(self):
        return 1 + np.log2(self.size)

    def cussum(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    j + np.insert(j, 0, 0)[:-1]
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def cusdiff(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    j - np.insert(j, 0, 0)[:-1]
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def cusprod(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    j * np.insert(j, 0, 0)[:-1]
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def cusdiv(self):
        datas = np.ravel(self)
        splices = self.shape[-1]
        result = (
            np.array(
                [
                    np.insert(j, 0, 0)[:-1] / j
                    for i in range(0, len(datas), splices)
                    for j in [datas[i : i + splices]]
                ]
            )
            .view(type(self))
            .reshape(self.shape)
        )
        result._dtype = result.dtype
        return result

    def percentile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.percentile(np.asarray(self), q, axis=axis, method=method).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def quantile(self, q, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.quantile(np.asarray(self), q, axis=axis, method=method).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def IQR(self, axis=None, method="linear"):
        if method not in method_list:
            method = "linear"
        result = np.percentile(
            np.asarray(self), [25, 50, 75], axis=axis, method=method
        ).view(type(self))
        result._dtype = np.float64
        return result

    def ratio(self, axis=None):
        result = np.asarray((self / np.sum(self, axis=axis, keepdims=True)) * 100).view(
            type(self)
        )
        result._dtype = result.dtype
        return result

    def zero_check(self):
        return NPBool(self.data == 0)
