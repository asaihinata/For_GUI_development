import numpy as np

from sgg.nparray import NPString

__all__ = ["getLabel"]


class getLabel(NPString):
    def __new__(cls, label=None):
        if label == None or isinstance(label, str):
            label = np.array([label], np.str_)
        return super().__new__(cls, label, d_ndim=1)

    def __iter__(self):
        return super().__iter__()

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __bool__(self):
        return bool(np.all([x == None for x in self.data]))

    def __repr__(self):
        return super().__repr__()

    def loop(self, lenght):
        result = np.tile(np.asarray(self), lenght // self.size + 1)[:lenght]
        return result
