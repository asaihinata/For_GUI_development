import numpy as np

from sgg.exceptions import ShapeError

from ..dev import _ArrayShapeMixin, _arrisuint

__all__ = ["NPArray"]

HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPArray(_ArrayShapeMixin, np.ndarray):
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
        if not _arrisuint(shape):
            raise ShapeError(shape)
        result = np.asarray(np.full(shape, fill_value, dtype=dtype)).view(cls)
        if dtype is None:
            result._dtype = result.dtype
        else:
            result._dtype = dtype
        return result

    @classmethod
    def sequential(cls, shape):
        if not _arrisuint(shape):
            raise ShapeError(shape)
        result = np.asarray(
            np.arange(np.prod(shape), dtype=np.uint64).reshape(shape)
        ).view(cls)
        result._dtype = result.dtype
        return result

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

    def __ne__(self, value):
        result = np.asarray(np.not_equal(np.asarray(self), value)).view(type(self))
        result._dtype = np.bool_
        return result

    def __eq__(self, value):
        result = np.asarray(np.equal(np.asarray(self), value)).view(type(self))
        result._dtype = np.bool_
        return result

    def count_nonzero(self, axis=None, keepdims=False):
        if not isinstance(keepdims, bool):
            keepdims = False
        return np.count_nonzero(np.asarray(self), axis=axis, keepdims=keepdims)

    def EType(self):
        result = np.asarray(np.vectorize(type)(self)).view(type(self))
        result._dtype = np.dtype(object)
        return result
