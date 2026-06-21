from ..nparray.isdtype import integerDtype, numberDtype

__all__ = [
    "numsmin",
    "nums",
    "num1s",
    "num0s",
    "num0",
    "intsmin",
    "ints",
    "int1s",
    "int0s",
    "int0",
    "range_num",
]


def numsmin(val, mins=0, other=None):
    if not numberDtype(val) or not numberDtype(mins):
        return other
    if mins < val:
        return val
    return other


def nums(val, other=None):
    return val if numberDtype(val) else other


def num1s(val=0, mins=1):
    return val if numberDtype(val) and 1 <= val else mins


def num0s(val=0, mins=0):
    return val if numberDtype(val) and 0 <= val else mins


def num0(val=0, mins=0):
    return val if numberDtype(val) and 0 < val else mins


def intsmin(val, mins=0, other=None):
    if not integerDtype(val) or not integerDtype(mins):
        return other
    if mins < val:
        return val
    return other


def ints(val=0, other=None):
    return val if integerDtype(val) else other


def int1s(val=0, mins=1):
    return val if integerDtype(val) and 1 <= val else mins


def int0s(val=0, mins=0):
    return val if integerDtype(val) and 0 <= val else mins


def int0(val=0, mins=0):
    return val if integerDtype(val) and 0 < val else mins


def range_num(val, mins=None, maxs=None, others=None):
    if not numberDtype(mins) or not numberDtype(max):
        return others
    if maxs < mins:
        mins, maxs = maxs, mins
    if mins <= val <= maxs:
        return val
    return others
