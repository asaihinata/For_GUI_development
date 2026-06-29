"""
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,redやgreenなどのカラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
"""
from re import compile, findall

from matplotlib.colors import to_hex, to_rgb, to_rgba
import numpy as np
from numpy import array, fromiter, nditer, uint8
from numpy.lib.mixins import NDArrayOperatorsMixin

from ._data import Get_color

__all__ = ["NPColor"]
_HEX6_RE = compile(r"^#[0-9a-f]{6}$")
_HEX3_RE = compile(r"^#[0-9a-f]{3}$")
_RGB_RE = compile(r"^rgb\((\d+),(\d+),(\d+)\)$")
_HSV_RE = compile(r"^hsv\((\d+),(\d+),(\d+)\)$")


HANDLED_FUNCTIONS = {}


def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func

    return decorator


def is_array_like(obj):
    if isinstance(obj, np.ndarray | list | tuple | range):
        return True
    elif hasattr(obj, "__array__"):
        return True
    return False


class NPColor(NDArrayOperatorsMixin, np.ndarray):
    _element_type = None

    def __new__(cls, color, dtype=object, d_ndim=None, min_ndim=None, max_ndim=None):
        if isinstance(color, str):
            color = [cls.__get_val(color)]
        elif is_array_like(color):
            color = [cls.__get_val(str(i)) for i in nditer(array(color))]
        else:
            raise TypeError("colorの値が不正です")
        resolved = cls._resolve_dtype(dtype)
        obj = np.asarray(color, dtype=resolved).view(cls)
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

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        raw_inputs = tuple(
            np.asarray(x) if isinstance(x, NPColor) else x for x in inputs
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

    @classmethod
    def __instancecheck__(cls, instance):
        return isinstance(instance, NPColor)

    @classmethod
    def __get_val(cls, color):
        colorname = Get_color.gets(color)
        if colorname is not None:
            return colorname[1]
        colors = _check(color)
        if colors is not None:
            return to_hex(colors / 255)
        raise ValueError("値が不正です")

    def tohex(self):
        self.data = array([to_hex(i) for i in self.data])
        return self

    def torgba(self):
        self.data = array([to_rgba(i, alpha=1) for i in self.data])
        return self

    def torgb(self):
        self.data = array([to_rgb(i) for i in self.data])
        return self


def _check(name):
    if name[0] == "#":
        if _HEX6_RE.match(name):
            val = findall(_HEX6_RE, name)[0][1:]
            return fromiter(
                (int(val[i : i + 2], 16) for i in range(0, len(val), 2)), dtype=uint8
            )
        if _HEX3_RE.match(name):

            def sets(t):
                return f"{t}{t}"

            val = findall(_HEX3_RE, name)[0][1:]
            return fromiter(
                (int(sets(val[i : i + 1]), 16) for i in range(0, len(val))), dtype=uint8
            )
    if _RGB_RE.match(name):
        return array(findall(_RGB_RE, name)[0], dtype=uint8)
    if _HSV_RE.match(name):
        return array(findall(_HSV_RE, name)[0], dtype=uint8)
