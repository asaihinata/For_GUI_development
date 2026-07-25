import numpy as np

from ..dev import _ArrayCommonMixin

__all__ = ["NPBool"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPBool(_ArrayCommonMixin, np.ndarray):
    _element_type = (bool, np.bool_, np.bool)
    _default_dtype = np.bool_

    def __new__(
        cls,
        data,
        /,
        dtype=np.bool_,
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        if dtype is None:
            obj = np.asarray(data, copy=copy).view(cls)
            resolved = obj.dtype
        else:
            resolved = cls._resolve_dtype(dtype)
            obj = np.asarray(data, dtype=resolved, copy=copy).view(cls)
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

    def __invert__(self):
        result = np.logical_not(np.asarray(self)).view(type(self))
        result._dtype = self.dtypes
        return result

    def __eq__(self, value):
        result = np.equal(np.asarray(self), value).view(type(self))
        result._dtype = result.dtype
        return result

    def __ne__(self, value):
        result = np.not_equal(np.asarray(self), value).view(type(self))
        result._dtype = result.dtype
        return result

    def all(self):
        return bool(np.all(np.asarray(self)))

    def any(self):
        return bool(np.any(np.asarray(self)))

    def inversion(self):
        result = np.logical_not(np.asarray(self)).view(type(self))
        result._dtype = self.dtypes
        return result

    @property
    def TrueCount(self):
        return int(np.count_nonzero(self))

    @property
    def FalseCount(self):
        return int(np.count_nonzero(~self))
