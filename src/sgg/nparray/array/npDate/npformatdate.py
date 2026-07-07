from datetime import date, datetime

from dateutil.parser import parse
import numpy as np

from ..dev import NDArrayOperatorsMixin, _ArrayShapeMixin
from ..npbool import NPBool
from ._types import serchDtype

__all__ = ["NPFormatDate"]
HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


class NPFormatDate(_ArrayShapeMixin, NDArrayOperatorsMixin, np.ndarray):
    _element_type = (np.datetime64, datetime, date)
    _default_dtype = "datetime64[D]"

    # ==========================================================
    # 生成関連
    # ==========================================================
    def __new__(
        cls,
        data,
        dtype="datetime64[D]",
        yearfirst=False,
        dayfirst=False,
        d_ndim=None,
        min_ndim=None,
        max_ndim=None,
    ):
        if not isinstance(data, np.ndarray):
            data = np.array(data)
        if not isinstance(yearfirst, bool):
            yearfirst = False
        if not isinstance(dayfirst, bool):
            dayfirst = False
        dtype = np.dtype(serchDtype(dtype))
        func = np.vectorize(
            lambda strs, yearfirst, dayfirst: str(
                parse(str(strs), yearfirst=yearfirst, dayfirst=dayfirst)
            )
        )
        resolved = cls._resolve_dtype(dtype)
        obj = np.asarray(
            np.array(
                [func(i, yearfirst, dayfirst) for i in np.nditer(data)], dtype=dtype
            ).reshape(data.shape),
            dtype=resolved,
        ).view(cls)
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

    # ==========================================================
    # クラスメソッド(検証・型解決)
    # (_resolve_dtype, _validate_ndim, _validate_elements は
    #  _ArrayShapeMixin が提供するため削除。
    #  _resolve_dtype に渡す前に __new__ 内で serchDtype による
    #  正規化を行っているため,Mixin側の実装のまま挙動が一致する)
    # ==========================================================

    # ==========================================================
    # numpyプロトコル関連
    # (__array_finalize__ は _ArrayShapeMixin が提供するため削除)
    # ==========================================================
    def __array__(self, dtype=np.dtype("datetime64[D]"), copy=None):
        return super().__array__(np.dtype(serchDtype(dtype)), copy=copy)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPFormatDate) else x for x in inputs
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

    def __class_getitem__(cls, item):
        return np.ndarray.__class_getitem__.__func__(cls, item)

    # ==========================================================
    # 特殊メソッド(演算子・組み込み関数)
    # ==========================================================
    def __ne__(self, other):
        return NPBool(np.not_equal(np.asarray(self), other))

    def __eq__(self, other):
        return NPBool(np.equal(np.asarray(self), other))

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

    # ==========================================================
    # プロパティ
    # (element_type, data, dtypes, min_ndim, max_ndim は
    #  _ArrayShapeMixin が提供するため削除)
    # ==========================================================

    # ==========================================================
    # 形状・次元関連
    # (to_1d, roll, rot90 は _ArrayShapeMixin が提供するため削除。
    #  lengtharange, shapesize は _ArrayCommonMixin が提供するため削除)
    # ==========================================================

    # ==========================================================
    # 型・変換関連
    # (tonumpy, typeconversion は Mixin が提供するため削除)
    # ==========================================================

    # ==========================================================
    # 値の検査・集計関連
    # (all_None, any_None, count_nonzero, unique, counts は
    #  Mixin が提供するため削除)
    # ==========================================================