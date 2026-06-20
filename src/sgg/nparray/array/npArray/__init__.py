from numpy import (all as alls, any as anys, arange, array, concatenate, expand_dims,
                   flip, isscalar, ndarray, prod, ravel, sort, tile)

__all__ = ["NPArray", "is_array_like", "change_array_like"]


def is_array_like(obj):
    if isinstance(obj, ndarray | list | tuple | range):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


def change_array_like(obj):
    if isinstance(obj, ndarray | list | tuple | range):
        return True
    elif isscalar(obj):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


class NPArray:
    def __init__(self, data, dtype=None, depth_limit=None):
        self.__dtype = dtype
        if not is_array_like(data):
            raise TypeError(
                "dataには配列もしくは__array__を持っているオブジェクトを指定してください"
            )
        self.__data = array(data, dtype=self.__dtype)
        if isinstance(depth_limit, int) and depth_limit < self.__data.ndim:
            raise TypeError("配列の深さが制限の深さに達しました")

    # 親クラス,子クラス共通の特殊メソッド
    def __iter__(self):
        if self.ndim == 1:
            return iter([self.__data])
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, item):
        return item in self.__data

    def __reversed__(self):
        self.__data = flip(self.__data)
        return self

    def __array__(self, dtype=None, copy=None):
        return array(self.__data, dtype=dtype, copy=copy)

    # 以下の特殊メソッドはそれぞれの子クラス毎に処理を変更する必要がある
    def __repr__(self):
        return f"NPArray({self.__data})"

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if method == "__call__":
            args = [x.data if isinstance(x, NPArray) else x for x in args]
            result = ufunc(*args, **kwargs)
            if isinstance(result, ndarray):
                return NPArray(result)
            return result
        return NotImplemented

    def _flatten(self):
        return ravel(self.__data), self.shape

    @property
    def nbytes(self):
        return self.__data.nbytes

    @property
    def ndim(self):
        return self.__data.ndim

    @property
    def shape(self):
        return self.__data.shape

    @property
    def size(self):
        return self.__data.size

    @property
    def T(self):
        self.__data = self.__data.T
        return self

    @property
    def dtype(self):
        return self.__dtype

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, datas):
        if not is_array_like(datas):
            raise TypeError("dataには配列の型を指定してください")
        self.__data = array(datas, dtype=self.__dtype)
        return self

    def shapesize(self, shapes):
        if self.shape == shapes:
            return True
        return False

    def astype(self, dtype):
        self.__data = self.__data.astype(dtype)
        self.__dtype = dtype
        return self

    def tolist(self):
        return self.__data.tolist()

    def tonp(self, dtype="none"):
        if dtype == "none":
            return self.__data
        return self.__data.astype(dtype)

    def sort(self):
        self.__data = sort(self.__data)
        return self

    def first_pop(self):
        if self.__data.ndim == 1:
            self.__data = concatenate((self.__data, self.__data[0]), axis=0)
        else:
            self.__data = concatenate(
                (self.__data, [[i[0]] for i in self.__data]), axis=1
            )
        return self

    def first_element(self):
        return self.__data[0]

    def dimension(self):
        return True if self.ndim == 1 else False

    def dimensions(self):
        return True if 2 <= self.ndim else False

    def lengtharange(self, start=0, dtype=None):
        def aranges(start, size, dtype):
            return arange(start, size, 1, dtype=dtype)

        shapes = self.shape
        lens = len(shapes)
        if lens == 1:
            return aranges(start, start + self.size, dtype)
        else:
            return tile(
                aranges(start, start + shapes[lens - 1], dtype), prod(shapes[:-1])
            ).reshape(shapes)

    def flatten(self):
        self.__data = ravel(self.__data)
        return self

    def reshape(self, size):
        self.__data = self.__data.reshape(size)
        return self

    def deep_add(self, val):
        if not isinstance(val, int):
            raise TypeError("valにはint型を指定してください")
        elif val <= 0:
            raise ValueError("valには1以上の整数を指定してください")
        for _ in range(val):
            self.__data = expand_dims(self.__data, axis=0)
        return self

    def min_deep(self, val):
        if not isinstance(val, int):
            raise TypeError("valにはint型を指定してください")
        elif val <= 0:
            raise ValueError("valには1以上の整数を指定してください")
        if self.ndim < val:
            for _ in range(val - self.ndim):
                self.__data = expand_dims(self.__data, axis=0)
        return self

    def get(self, val):
        if isinstance(val, int):
            data, size = self.__data.flatten(), self.size
            if val == size:
                return data[val - 1]
            elif val < size:
                return data[val]
            elif size < val:
                return data[val % size]
        else:
            return self.__data[val]

    def clear(self):
        self.__data = array([])
        return self

    def all_None(self):
        return bool(alls(self.__data == None))

    def any_None(self):
        return bool(anys(self.__data == None))
