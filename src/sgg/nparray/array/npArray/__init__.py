import numpy as np

from sgg.exceptions import ShapeError

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin, _arrisuint

__all__ = ["NPArray"]

HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPArray(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = None
    _default_dtype = "object"

    def __new__(cls, data, dtype=None, d_ndim=None, min_ndim=None, max_ndim=None):
        if dtype is None:
            obj = np.asarray(data).view(cls)
            resolved = obj.dtype
        else:
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

    @classmethod
    def full(cls, fill_value, shape, dtype=None):
        if _arrisuint(shape):
            return np.full(shape, fill_value, np.dtype(dtype))
        else:
            raise ShapeError(shape)

    @classmethod
    def sequential(cls, shape):
        if _arrisuint(shape):
            return np.asarray(
                np.arange(np.prod(shape), dtype=np.uint64).reshape(shape)
            ).view(cls)
        else:
            raise ShapeError(shape)

    def __array__(self, dtype=None, copy=None):
        return super().__array__(dtype, copy=copy)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPArray) else x for x in inputs
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

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

    def __ne__(self, value):
        result = np.asarray(np.not_equal(np.asarray(self), value)).view(type(self))
        result._dtype = np.bool_
        return result

    def __eq__(self, value):
        result = np.asarray(np.equal(np.asarray(self), value)).view(type(self))
        result._dtype = np.bool_
        return result

    def __repr__(self):
        return f"{type(self).__name__}({np.array2string(np.asarray(self), separator=',')},dtype={self.dtype})"

    def __str__(self):
        return self.__repr__()

    def __contains__(self, value):
        return super().__contains__(value)

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
            elif -size <= key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return data[key]
        raise TypeError("keyにはintまたはsliceを指定してください")

    def count_nonzero(self, axis=None, keepdims=False):
        if not isinstance(keepdims, bool):
            keepdims = False
        return np.count_nonzero(np.asarray(self), axis=axis, keepdims=keepdims)

    def EType(self):
        return np.asarray(np.vectorize(type)(self))
