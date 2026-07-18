from operator import index
from re import compile, fullmatch

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


__VALID_UNITS = {
    "Y",
    "M",
    "W",
    "D",
    "h",
    "m",
    "s",
    "ms",
    "us",
    "ns",
    "ps",
    "fs",
    "as",
    "μs",
}

__DT64_PATTERN = compile(r"^(?:datetime64|M8)\[(?P<unit>\w+)\]$")
__DT64_GENERIC_PATTERN = compile(r"^(?:datetime64|M8)$")


def _dt64_unit(spec):
    if isinstance(spec, np.datetime64):
        return spec
    elif isinstance(spec, bytes):
        spec = spec.decode("ascii")
    elif not isinstance(spec, str):
        return "datetime64[D]"
    spec = spec.strip()
    if spec and spec[0] in "|=<>":
        spec = spec[1:]
    if not spec:
        return "datetime64[D]"
    match = __DT64_PATTERN.match(spec)
    if match:
        unit = match.group("unit")
        if unit not in __VALID_UNITS:
            return "datetime64[D]"
        return f"datetime64[{unit}]"
    if __DT64_GENERIC_PATTERN.match(spec):
        return "datetime64"
    if spec in __VALID_UNITS:
        return f"datetime64[{spec}]"
    return "datetime64[D]"


def _get_dt64_unit(dtype_str, auto="D"):
    if not isinstance(dtype_str, str | bytes):
        return auto
    dtype_str = _dt64_unit(dtype_str)
    if dtype_str[0] in [">", "|", "<", "="]:
        dtype_str = dtype_str[1:]
    m = fullmatch(r"datetime64\[(\w+)\]", dtype_str)
    if m is None:
        return auto
    return m.group(1)
