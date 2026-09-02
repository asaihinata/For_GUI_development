import numpy as np
from numpy._core.fromnumeric import _wrapfunc

from sgg.exceptions import ShapeError

from ._arrcheck import _arrisuint, _to_np_scalar

__all__ = ["_ArrayCommonMixin"]


class _ArrayCommonMixin(np.ndarray):
    """次元数制約(min_ndim/max_ndim)を持つ配列クラス向けの共通メソッド"""

    def __dir__(self):
        return np.sort(super().__dir__()).tolist()

    def __repr__(self):
        return f"{type(self).__name__}({np.array2string(np.asarray(self), separator=",")},dtype={self.dtype})"

    def __str__(self):
        return self.__repr__()

    def __contains__(self, value):
        return super().__contains__(value)

    def __len__(self):
        if self.size == 1:
            return 1
        return super().__len__()

    def __getitem__(self, key):
        size = self.size
        if size == 0:
            raise IndexError("空の配列にはアクセスできません")
        if isinstance(key, int | np.integer):
            obj = self.data.flatten()
            if key == size:
                return obj[size - 1]
            elif -size <= key < size:
                return obj[key]
            else:
                return obj[key % size]
        else:
            return self.__array__()[key]

    def __iter__(self):
        return iter(np.asarray(self))

    def __reversed__(self):
        result = np.flip(np.asarray(self)).view(type(self))
        result._dtype = self._dtype
        return result

    def __array__(self, dtype=None, /, *, copy=None):
        return super().__array__(dtype, copy=copy)

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

    def __array_function__(self, func, types, args, kwargs):
        return super().__array_function__(func, types, args, kwargs)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, self.__class__) else x for x in inputs
        )
        result = getattr(ufunc, method)(*raw_inputs, **dict(kwargs))

        if result is NotImplemented:
            return NotImplemented
        judge = False
        resultdtype = (
            result.dtype if hasattr(result, "dtype") else np.dtype(type(result))
        )
        for dtype in self._element_type:
            if np.issubdtype(resultdtype, dtype):
                judge = True
        if judge and isinstance(result, np.ndarray) and result.dtype:
            result = result.view(type(self))
            result._dtype = getattr(inputs[0], "_dtype", None)

        return result

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._dtype = getattr(obj, "_dtype", None)
        self._min_ndim = getattr(obj, "_min_ndim", None)
        self._max_ndim = getattr(obj, "_max_ndim", None)

    @classmethod
    def _resolve_dtype(cls, dtype):
        if dtype is None:
            return np.dtype(cls._default_dtype)
        return np.dtype(dtype)

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
        objdtype = obj.dtype
        for dtype in cls._element_type:
            if np.issubdtype(objdtype, dtype):
                return
        raise TypeError(
            f"{cls.__name__}の要素は{cls._element_type}のみ許可されています"
        )

    def _toval(self):
        if self.zero_ndim:
            return self.item()
        return self.__array__()

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

    def reshape(self, shape):
        dtype = self.dtype
        result = np.asarray(
            _wrapfunc(self.__array__(), "reshape", shape), dtype=dtype
        ).view(type(self))
        result._dtype = dtype
        return result

    def ravel(self, order="C"):
        result = np.asarray(np.ravel(np.asarray(self), order=order)).view(type(self))
        result._dtype = result.dtype
        return result

    def tonumpy(self, copy=None):
        return self.__array__(copy=copy)

    def to_1d(self):
        if self.min_ndim is not None and self.min_ndim > 1:
            raise ValueError(f"min_ndimが{self.min_ndim}のため1次元に変換できません")
        result = np.asarray(self).flatten().view(type(self))
        result._dtype = self._dtype
        return result

    def typeconversion(self, type, casting="safe"):
        if casting not in ["no", "equiv", "safe", "same_kind", "same_value", "unsafe"]:
            casting = "safe"
        return np.can_cast(np.asarray(self), type, casting=casting)

    def astype(self, dtype, copy=True):
        if not isinstance(copy, bool):
            copy = True
        dtype = np.dtype(dtype)
        if self._element_type is None or dtype in self._element_type:
            return np.asarray(self, dtype).view(type(self))
        return self.__array__(dtype, copy=copy)

    def unique(self):
        return np.unique(np.asarray(self))

    def counts(self):
        count = np.unique_counts(np.asarray(self))
        return count.values, count.counts

    def roll(self, shift, axis=None):
        result = np.roll(np.asarray(self), shift, axis).view(type(self))
        result._dtype = self._dtype
        return result

    @classmethod
    def full(cls, fill_value, shape, dtype=None):
        _to_np_scalar(fill_value)
        if not _arrisuint(shape):
            raise ShapeError(shape)
        return cls(np.full(shape, fill_value), dtype=dtype)

    def rot90(self, k=1, axes=(0, 1)):
        if self.ndim <= 1:
            raise ValueError("配列には2次元以上ではないといけません")
        result = np.rot90(np.asarray(self), k, axes).view(type(self))
        result._dtype = self._dtype
        return result

    def choice(self, size=None, replace=True, p=None, axis=0, shuffle=True, seed=None):
        return np.random.default_rng(seed).choice(
            self, size=size, replace=replace, p=p, axis=axis, shuffle=shuffle
        )

    # property
    @property
    def __array_priority__(self):
        return 1.0

    @property
    def element_type(self):
        return self._element_type

    @property
    def data(self):
        return self.__array__()

    @property
    def min_ndim(self):
        return getattr(self, "_min_ndim", None)

    @property
    def max_ndim(self):
        return getattr(self, "_max_ndim", None)

    @property
    def zero_ndim(self):
        return np.ndim(self) == 0

    @property
    def one_ndim(self):
        return np.ndim(self) == 1

    # dtype
    @property
    def dtypes(self):
        return self._dtype

    @property
    def kinds(self):
        return self.dtype.kind

    @property
    def types(self):
        return self.dtype.type

    @property
    def chars(self):
        return self.dtype.char

    @property
    def nums(self):
        return self.dtype.num

    @property
    def strs(self):
        return self.dtype.str

    @property
    def names(self):
        return self.dtype.name

    @property
    def itemsizes(self):
        return self.dtype.itemsize
