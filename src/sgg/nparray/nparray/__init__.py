import numpy as np

from sgg.exceptions import ShapeError

from ..dev import _ArrayCommonMixin, _arrisuint

__all__ = ["NPArray"]


class NPArray(_ArrayCommonMixin):
    """`np.ndarray`を継承した型付き配列クラス"""

    _element_type = None
    _default_dtype = "object"

    def __new__(
        cls,
        data,
        /,
        dtype=None,
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

    def __eq__(self, value):
        result = np.equal(np.asarray(self), value).view(type(self))
        result._dtype = np.bool_
        return result

    def __ne__(self, value):
        result = np.not_equal(np.asarray(self), value).view(type(self))
        result._dtype = np.bool_
        return result

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

    def count_nonzero(self, axis=None, keepdims=False):
        if not isinstance(keepdims, bool):
            keepdims = False
        result = np.asarray(
            np.count_nonzero(self, axis=axis, keepdims=keepdims), np.uint64
        ).view(type(self))
        result._dtype = np.uint64
        return result

    def EType(self):
        result = np.asarray(np.vectorize(type)(self)).view(type(self))
        result._dtype = np.dtype(object)
        return result
