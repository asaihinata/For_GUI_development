import numpy as np

from ..nparray import NPArray

__all__ = ["NPBool"]


class NPBool(NPArray):
    _element_type = (bool, np.bool_)

    def __new__(cls, data, dtype=np.bool_, d_ndim=None, min_ndim=None, max_ndim=None):
        return super().__new__(cls, data, dtype, d_ndim, min_ndim, max_ndim)
    @classmethod
    def __instancecheck__(cls, instance):
        return isinstance(instance, NPBool)
    def __ne__(self, other):
        return super().__ne__(other)

    def __eq__(self, other):
        return super().__eq__(other)

    def all(self):
        return np.all(np.asarray(self))

    def any(self):
        return np.any(np.asarray(self))
