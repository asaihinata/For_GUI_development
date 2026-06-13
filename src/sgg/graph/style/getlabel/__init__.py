from numpy import all, array, tile

from ....nparray import NPArray

__all__ = ["getLabel"]


class getLabel(NPArray):
    def __init__(self, label=None):
        if label == None or isinstance(label, str):
            label = array([label])
        super().__init__(label, depth_limit=1)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, val):
        return super().__getitem__(val)

    def __bool__(self):
        return bool(all([x == None for x in self.data]))

    def __repr__(self):
        return f"getLabel({self.data})"

    def loop(self, lenght):
        self.data = tile(self.data, lenght // self.size + 1)[:lenght]
        return self
