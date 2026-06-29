"""基本的な数値の操作をするモジュール"""

from __future__ import annotations

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

from ...isdtype import numberdDtype, numberDtype

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


class NPNumber(NDArrayOperatorsMixin, np.ndarray):
    _element_type = (int, float, complex, np.number)

    def __new__(
        cls, input_array, dtype=np.float64, d_ndim=None, min_ndim=None, max_ndim=None
    ):
        resolved = cls._resolve_dtype(dtype)
        if numberDtype(resolved):
            raise TypeError("dtypeには数値型を指定してください")
        obj = np.asarray(input_array, dtype=resolved).view(cls)
        cls._validate_elements(obj)
        obj._dtype = resolved
        if isinstance(d_ndim, int):
            cls._validate_ndim(obj, d_ndim, d_ndim)
            obj._min_ndim=obj._max_ndim = d_ndim
        else:
            cls._validate_ndim(obj, min_ndim, max_ndim)
            obj._min_ndim = min_ndim
            obj._max_ndim = max_ndim
        return obj

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._dtype = getattr(obj, "_dtype", None)
        self._min_ndim = getattr(obj, "_min_ndim", None)
        self._max_ndim = getattr(obj, "_max_ndim", None)

    @classmethod
    def _resolve_dtype(cls, dtype):
        if dtype is not None:
            return np.dtype(dtype)
        return np.dtype(np.float64)

    @classmethod
    def _validate_ndim(cls, obj, min_ndim, max_ndim):
        ndim = obj.ndim
        if min_ndim is not None and ndim < min_ndim:
            raise ValueError(
                f"{cls.__name__}の次元数は{min_ndim}以上である必要があります"
            )
        if max_ndim is not None and ndim > max_ndim:
            raise ValueError(
                f"{cls.__name__}の次元数は{max_ndim}以下である必要があります"
            )

    @classmethod
    def _validate_elements(cls, obj):
        if cls._element_type is None:
            return
        for elem in obj.flat:
            if not isinstance(elem, cls._element_type):
                raise TypeError(
                    f"{cls.__name__}の要素は{cls._element_type}のみ許可されています"
                )

    @property
    def data(self):
        return np.asarray(self)

    @property
    def dtypes(self):
        return self._dtype

    @dtypes.setter
    def dtypes(self, dtype):
        if dtype is not None:
            self._dtype = np.dtype(dtype)
        return self._dtype

    @property
    def min_ndim(self):
        return getattr(self, "_min_ndim", None)

    @property
    def max_ndim(self):
        return getattr(self, "_max_ndim", None)

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

    @classmethod
    def __instancecheck__(cls, instance):
        return isinstance(instance, NPNumber)

    def __repr__(self):
        return f"{type(self).__name__}({np.array2string(np.asarray(self), separator=',')},dtype={self.dtype})"

    def __str__(self):
        return self.__repr__()

    def __contains__(self, item):
        return super().__contains__(item)

    def __len__(self):
        return super().__len__()

    def __iter__(self):
        if self.ndim == 1:
            return iter([self.data])
        return iter(self.data)

    def __reversed__(self):
        result = np.flip(np.asarray(self)).view(type(self))
        result._dtype = self._dtype
        return result

    def __getitem__(self, key):
        size = self.size
        if size == 0:
            raise IndexError("空の配列にはアクセスできません")
        data = self.data.flatten()
        if isinstance(key, int):
            if key == size:
                return data[size - 1]
            elif key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return self.data.flatten()[key]

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

    def to_1d(self):
        if self.min_ndim is not None and self.min_ndim > 1:
            raise ValueError(f"min_ndimが{self.min_ndim}のため1次元に変換できません")
        result = np.asarray(self).flatten().view(type(self))
        result._dtype = self._dtype
        return result

    def lengtharange(self):
        shapes = self.shape
        lens = len(shapes)
        if lens == 1:
            raw = np.arange(0, self.size, 1, dtype=np.uint64)
        else:
            raw = np.tile(
                np.arange(0, shapes[lens - 1], dtype=np.uint64), np.prod(shapes[:-1])
            ).reshape(shapes)
        result = raw.view(type(self))
        result._dtype = np.dtype("uint64")
        return result

    def shapesize(self, shapes):
        if self.shape == shapes:
            return True
        return False

    def tonumpy(self):
        return np.asarray(self)

    def all_None(self):
        return bool(np.all(self.data == None))

    def any_None(self):
        return bool(np.any(self.data == None))

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
        result = np.percentile(self.data, q, axis=axis, method=method).view(type(self))
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
