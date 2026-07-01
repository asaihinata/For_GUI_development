import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

__all__ = ["NPBool"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPBool(NDArrayOperatorsMixin, np.ndarray):
    _element_type = (bool, np.bool_)

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

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._dtype = getattr(obj, "_dtype", None)
        self._min_ndim = getattr(obj, "_min_ndim", None)
        self._max_ndim = getattr(obj, "_max_ndim", None)

    @classmethod
    def _resolve_dtype(cls, dtype):
        if dtype is not None:
            return np.dtype(dtype)
        return np.dtype(np.bool_)

    @classmethod
    def _validate_ndim(cls, obj, min_ndim, max_ndim):
        ndim = obj.ndim
        if min_ndim is not None and ndim < min_ndim:
            raise ValueError(
                f"{cls.__name__}の次元数は{min_ndim}以上である必要があります"
            )
        if max_ndim is not None and ndim > max_ndim:
            raise ValueError(
                f"{cls.__name__}の次元数は{max_ndim}以下である必要があります"
            )

    @classmethod
    def _validate_elements(cls, obj):
        if cls._element_type is None:
            return
        for elem in obj.flat:
            if not isinstance(elem, cls._element_type):
                raise TypeError(
                    f"{cls.__name__}の要素は{cls._element_type}のみ許可されています"
                )

    @property
    def data(self):
        return np.asarray(self, dtype=self._dtype)

    @property
    def dtypes(self):
        return self._dtype

    @dtypes.setter
    def dtypes(self, dtype):
        if dtype is not None:
            self._dtype = np.dtype(dtype)
        return self._dtype

    @property
    def min_ndim(self):
        return getattr(self, "_min_ndim", None)

    @property
    def max_ndim(self):
        return getattr(self, "_max_ndim", None)

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

    def __ne__(self, other):
        return NPBool(super().__ne__(other))

    def __eq__(self, other):
        return NPBool(super().__eq__(other))

    def __repr__(self):
        return f"{type(self).__name__}({np.array2string(np.asarray(self), separator=',')},dtype={self.dtype})"

    def __str__(self):
        return self.__repr__()

    def __contains__(self, item):
        return super().__contains__(item)

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
            elif key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return data[key]

    def to_1d(self):
        if self.min_ndim is not None and self.min_ndim > 1:
            raise ValueError(f"min_ndimが{self.min_ndim}のため1次元に変換できません")
        result = np.asarray(self).flatten().view(type(self))
        result._dtype = self._dtype
        return result

    def lengtharange(self):
        shapes = self.shape
        lens = len(shapes)
        if lens == 1:
            raw = np.arange(0, self.size, 1)
        else:
            raw = np.tile(np.arange(0, shapes[lens - 1]), np.prod(shapes[:-1])).reshape(
                shapes
            )
        return np.array(raw, dtype=np.uint64)

    def shapesize(self, shapes):
        if self.shape == shapes:
            return True
        return False

    def tonumpy(self):
        return np.asarray(self)

    def all_None(self):
        return bool(np.all(self.data == None))

    def any_None(self):
        return bool(np.any(self.data == None))

    def all(self):
        return bool(np.all(np.asarray(self)))

    def any(self):
        return bool(np.any(np.asarray(self)))
