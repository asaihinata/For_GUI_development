from numbers import Number

import numpy as np

__all__ = [
    "_is_int",
    "_is_number",
    "int0",
    "int0s",
    "int1s",
    "ints",
    "intsmin",
    "list2number",
    "num0",
    "num0s",
    "num1s",
    "nums",
    "range_num",
    "range_zero_one",
]


def _is_number(value):
    if isinstance(value, Number):
        return True
    if isinstance(value, np.generic):
        return np.issubdtype(value.dtype, np.number)
    return False


def _is_int(value):
    if isinstance(value, int):
        return True
    if isinstance(value, np.generic):
        return np.issubdtype(value.dtype, np.integer)
    return False


def nums(val, other=None):
    return val if _is_number(val) else other


def num1s(val, mins=1):
    return val if _is_number(val) and 1 <= val else mins


def num0s(val, mins=0):
    return val if _is_number(val) and 0 <= val else mins


def num0(val, mins=0):
    return val if _is_number(val) and 0 < val else mins


def intsmin(val, mins=0, other=None):
    if _is_number(mins) and _is_number(val) and mins < val:
        return val
    return other


def ints(val=0, other=None):
    return val if _is_int(val) else other


def int1s(val=0, mins=1):
    return val if _is_int(val) and 1 <= val else mins


def int0s(val=0, mins=0):
    return val if _is_int(val) and 0 <= val else mins


def int0(val=0, mins=0):
    return val if _is_int(val) and 0 < val else mins


def range_num(val, mins=None, maxs=None, others=None):
    if not _is_number(mins) and not _is_number(maxs):
        return others
    if maxs < mins:
        mins, maxs = maxs, mins
    if mins <= val <= maxs:
        return val
    return others


def range_zero_one(val, out=1.0, endpoint=True):
    if not isinstance(val, np.number | Number):
        return out
    if not isinstance(endpoint, bool):
        endpoint = True
    if endpoint and 0 <= val <= 1:
        return val
    elif not endpoint and 0 <= val < 1:
        return val
    return out


def list2number(lin):
    lin = np.asarray(lin)
    if np.issubdtype(lin.dtype, np.number) and lin.shape == (2,):
        return True
    return False
