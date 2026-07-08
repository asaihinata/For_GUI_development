import numpy as np

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin

__all__ = ["NPBool"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPBool(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = (bool, np.bool_, np.bool)
    _default_dtype = np.bool_

    def __new__(cls, data, dtype=np.bool_, d_ndim=None, min_ndim=None, max_ndim=None):
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

    def __array__(self, dtype=np.bool_, copy=None):
        return super().__array__(dtype, copy=copy)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPBool) else x for x in inputs
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

    def __invert__(self):
        result = np.logical_not(np.asarray(self)).view(type(self))
        result._dtype = self._dtype
        return result

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

    def all(self):
        return bool(np.all(np.asarray(self)))

    def any(self):
        return bool(np.any(np.asarray(self)))

    def inversion(self):
        result = np.logical_not(np.asarray(self)).view(type(self))
        result._dtype = self._dtype
        return result
