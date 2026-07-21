from operator import index
from re import compile

import numpy as np
from numpy._core.multiarray import normalize_axis_index
from numpy._core.overrides import set_module

from sgg.exceptions import *

__all__ = [
    "_arrisuint",
    "_dt64_unit",
    "_get_dt64_unit",
    "_int_co_check",
    "_intarraylike_check",
    "_normalize_axis",
    "_scalar_check",
    "change_array_like",
    "is_array_like",
]


def _int_co_check(obj):
    obj = np.asanyarray(obj)
    if not np.issubdtype(obj.dtype, np.integer):
        raise TypeError(f"{obj.dtype}には整数型を指定してください")


def _scalar_check(element):
    return np.isscalar(element)


def _intarraylike_check(obj):
    try:
        arr = np.asarray(obj)
    except Exception:
        return False
    if arr.dtype.kind in "iub":
        return True
    if arr.dtype.kind == "f":
        return arr.size > 0 and np.all(np.mod(arr, 1) == 0) and np.all(np.isfinite(arr))
    if arr.dtype.kind == "O":
        try:
            arr.astype(np.int64)
            return True
        except ValueError, TypeError:
            return False
    return False


def _arrisuint(arr):
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)
    if np.issubdtype(arr.dtype, np.integer):
        return np.all(arr > 0) and np.all(np.equal(np.mod(arr, 1), 0))
    else:
        return False


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


@set_module("numpy.lib.array_utils")
def _normalize_axis(axis, ndim, argname=None, allow_duplicate=False):
    if not isinstance(axis, tuple | list):
        try:
            axis = [index(axis)]
        except TypeError:
            pass
    axis = tuple(normalize_axis_index(ax, ndim, argname) for ax in axis)
    if not allow_duplicate and len(set(axis)) != len(axis):
        if argname:
            raise ValueError(f"引数{argname}で軸が重複しています")
        else:
            raise ValueError("軸が繰り返しです")
    return axis


_VALID_UNITS = frozenset(
    {"Y", "M", "W", "D", "h", "m", "s", "ms", "us", "ns", "ps", "fs", "as"}
)
_UNIT_ALIASES = {"μs": "us"}
_DTYPE_PATTERN = compile(r"^(?:datetime64|[|=<>]?M8)(?:\[(?P<unit>[^\[\]]+)\])?$")


def _to_str(value):
    if isinstance(value, bytes):
        return value.decode("ascii")
    if isinstance(value, str):
        return value
    try:
        return str(np.dtype(value))
    except TypeError:
        pass
    raise TypeError(f"{value}にはstrまたはbytesを指定してください")


def _normalize_unit(unit: str):
    return _UNIT_ALIASES.get(unit, unit)


def _get_dt64_unit(value):
    s = _to_str(value).strip()
    m = _DTYPE_PATTERN.match(s)
    if m is not None:
        unit = m.group("unit")
        return _normalize_unit(unit) if unit is not None else ""
    normalized = _normalize_unit(s)
    if normalized in _VALID_UNITS:
        return normalized
    raise ValueError(f"認識できないdatetime64の単位/dtype文字列です: {value!r}")


def _dt64_unit(value):
    if isinstance(value, np.datetime64):
        return value
    unit = _get_dt64_unit(value)
    return f"datetime64[{unit}]" if unit else "datetime64"
