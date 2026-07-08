from numpy import all, array, asarray, tile

from sgg.nparray import NPArray

__all__ = ["getLabel"]


class getLabel(NPArray):
    def __new__(cls, label=None):
        if label == None or isinstance(label, str):
            label = array([label])
        return super().__new__(cls, label, d_ndim=1)

    def __iter__(self):
        return iter(list(self.data.tolist()))

    def __getitem__(self, val):
        return super().__getitem__(val)

    def __bool__(self):
        return bool(all([x == None for x in self.data]))

    def __repr__(self):
        return super().__repr__()

    def loop(self, lenght):
        result = tile(asarray(self), lenght // self.size + 1)[:lenght]
        return result
