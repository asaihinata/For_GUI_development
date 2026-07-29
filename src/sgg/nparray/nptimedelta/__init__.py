
import numpy as np

from ..dev import _ArrayCommonMixin, _tm64_unit
from ..npbool import NPBool

__all__ = ["NPTimedelta"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPTimedelta(_ArrayCommonMixin, np.ndarray):
    _element_type = np.timedelta64
    _default_dtype = np.dtype("timedelta64[D]")

    def __new__(
        cls,
        data,
        /,
        dtype="timedelta64[D]",
        *,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
        copy=True,
    ):
        if not isinstance(copy, bool):
            copy = True
        resolved = cls._resolve_dtype(_tm64_unit(dtype))
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
            np.asarray(x) if isinstance(x, NPTimedelta) else x for x in inputs
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

    def __add__(self, value):
        result = np.asarray(np.add(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    def __sub__(self, value):
        result = np.asarray(np.subtract(self, value)).view(type(self))
        result._dtype = result.dtype
        return result

    __radd__ = __add__
    __rsub__ = __sub__

    def __eq__(self, value):
        return NPBool(np.equal(np.asarray(self), value))

    def __ne__(self, value):
        return NPBool(np.not_equal(np.asarray(self), value))

    def __lt__(self, value):
        return NPBool(np.less(np.asarray(self), value))

    def __le__(self, value):
        return NPBool(np.less_equal(np.asarray(self), value))

    def __gt__(self, value):
        return NPBool(np.greater(np.asarray(self), value))

    def __ge__(self, value):
        return NPBool(np.greater_equal(np.asarray(self), value))
