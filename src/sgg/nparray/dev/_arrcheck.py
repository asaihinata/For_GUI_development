from operator import index

import numpy as np
from numpy._core.multiarray import normalize_axis_index
from numpy._core.overrides import set_module

from sgg.exceptions import *

__all__ = [
    "_arrisuint",
    "_int_co_check",
    "_normalize_axis",
    "_to_np_scalar",
]


def _arrisuint(arr):
    arr = np.asarray(arr)
    kind = arr.dtype.kind
    if kind == "u":
        return True
    elif kind == "i":
        return np.all(0 < arr)
    else:
        return False


def _int_co_check(obj):
    if not np.asarray(obj).dtype.kind in ["b", "i", "u"]:
        raise TypeError(f'"{obj}"には整数型を指定してください')


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


def _to_np_scalar(value):
    obj = np.asarray(value)
    if obj.ndim == 0:
        return obj[()]
    raise ValueError(f"{value}がスカラー値ではありません")
