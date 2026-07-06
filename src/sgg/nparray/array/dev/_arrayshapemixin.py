"""
np.ndarrayサブクラス間で共通するメソッドをまとめたMixinモジュール

このモジュールのMixinは`np.ndarray`のサブクラスに対して使用することを前提とする。
継承先クラスは`_dtype`属性(インスタンス変数)を持つ必要がある。
"""

import numpy as np

__all__ = ["_ArrayCommonMixin", "_ArrayShapeMixin"]


class _ArrayCommonMixin:
    """全ての配列クラスに共通する,形状に依存しない基本メソッド"""

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


class _ArrayShapeMixin(_ArrayCommonMixin):
    """次元数制約(min_ndim/max_ndim)を持つ配列クラス向けの共通メソッド"""

    @classmethod
    def _resolve_dtype(cls, dtype):
        if dtype is not None:
            return np.dtype(dtype)
        return np.dtype(cls._default_dtype)

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

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._dtype = getattr(obj, "_dtype", None)
        self._min_ndim = getattr(obj, "_min_ndim", None)
        self._max_ndim = getattr(obj, "_max_ndim", None)

    @property
    def element_type(self):
        return self._element_type

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

    @property
    def min_ndim(self):
        return getattr(self, "_min_ndim", None)

    @property
    def max_ndim(self):
        return getattr(self, "_max_ndim", None)

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
            raise ValueError("配列には2次元以上ではないといけません")
        result = np.rot90(np.asarray(self), k, axes).view(type(self))
        result._dtype = self._dtype
        return result
