import numpy as np

from ..dev import NDArrayOperatorsMixin

__all__ = ["is_array_like", "change_array_like", "NPArray"]


def is_array_like(obj):
    if isinstance(obj, np.ndarray | list | tuple | range):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


def change_array_like(obj):
    if isinstance(obj, np.ndarray | list | tuple | range):
        return True
    elif np.isscalar(obj):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPArray(NDArrayOperatorsMixin, np.ndarray):
    __element_type = None

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

    def __array__(self, dtype=None, copy=None):
        return super().__array__(dtype, copy=copy)

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
        return np.dtype("object")

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
        if cls.__element_type is None:
            return
        for elem in obj.flat:
            if not isinstance(elem, cls.__element_type):
                raise TypeError(
                    f"{cls.__name__}の要素は{cls.__element_type}のみ許可されています"
                )

    @property
    def element_type(self):
        return self.__element_type

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

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

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

    def __ne__(self, other):
        result = np.asarray(super().__ne__(other)).view(type(self))
        result._dtype = np.bool
        return result

    def __eq__(self, other):
        result = np.asarray(super().__eq__(other)).view(type(self))
        result._dtype = np.bool
        return result

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
            elif -size <= key < size:
                return data[key]
            else:
                return data[key % size]
        elif isinstance(key, slice):
            return data[key]
        raise TypeError("keyにはintまたはsliceを指定してください")

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

    def typeconversion(self, type, casting="safe"):
        if casting not in ["no", "equiv", "safe", "same_kind", "same_value", "unsafe"]:
            casting = "safe"
        return np.can_cast(np.asarray(self), type, casting=casting)

    def count_nonzero(self, axis=None, keepdims=False):
        if not isinstance(keepdims, bool):
            keepdims = False
        return np.count_nonzero(np.asarray(self), axis=axis, keepdims=keepdims)

    def unique(self):
        return np.unique(np.asarray(self))

    def counts(self):
        count = np.unique_counts(np.asarray(self))
        return count.values, count.counts

    def roll(self, shift, axis=None):
        if not isinstance(shift, int | float):
            raise TypeError("shiftには数値の型を指定してください")
        result = np.roll(np.asarray(self), shift, axis).view(type(self))
        result._dtype = self._dtype
        return result

    def rot90(self, k=1, axes=(0, 1)):
        if self.ndim <= 1:
            raise ValueError(f"配列には2次元以上ではないといけません")
        result = np.rot90(np.asarray(self), k, axes).view(type(self))
        result._dtype = self._dtype
        return result
