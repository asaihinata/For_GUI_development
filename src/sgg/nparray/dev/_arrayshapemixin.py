import numpy as np

__all__ = ["_ArrayCommonMixin"]


class _ArrayCommonMixin(np.ndarray):
    """次元数制約(min_ndim/max_ndim)を持つ配列クラス向けの共通メソッド"""

    def __repr__(self):
        return f"{type(self).__name__}({np.array2string(np.asarray(self), separator=',')},dtype={self.dtype})"

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

    def __iter__(self):
        return iter(np.asarray(self))

    def __reversed__(self):
        result = np.flip(np.asarray(self)).view(type(self))
        result._dtype = self._dtype
        return result

    def __array__(self, dtype=None, /, *, copy=None):
        if dtype is None:
            dtype = self.dtypes
        return super().__array__(dtype, copy=copy)

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

    def __array_function__(self, func, types, args, kwargs):
        return super().__array_function__(func, types, args, kwargs)

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
        for elem in obj.flat:
            if not isinstance(elem, cls._element_type):
                raise TypeError(
                    f"{cls.__name__}の要素は{cls._element_type}のみ許可されています"
                )

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

    def isscalar(self):
        return np.isscalar(self.tolist())

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

    def unique(self):
        return np.unique(np.asarray(self))

    def counts(self):
        count = np.unique_counts(np.asarray(self))
        return count.values, count.counts

    def roll(self, shift, axis=None):
        result = np.roll(np.asarray(self), shift, axis).view(type(self))
        result._dtype = self._dtype
        return result

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

    @property
    def element_type(self):
        return self._element_type

    @property
    def data(self):
        return self.__array__(self.dtypes)

    @property
    def dtypes(self):
        return self._dtype

    @property
    def min_ndim(self):
        return getattr(self, "_min_ndim", None)

    @property
    def max_ndim(self):
        return getattr(self, "_max_ndim", None)
