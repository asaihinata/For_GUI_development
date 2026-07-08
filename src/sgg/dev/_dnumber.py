from sgg.nparray.isdtype import integerDtype, numberDtype

__all__ = [
    "int0",
    "int0s",
    "int1s",
    "ints",
    "intsmin",
    "num0",
    "num0s",
    "num1s",
    "nums",
    "numsmin",
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


def num1s(val, mins=1):
    return val if numberDtype(val) and 1 <= val else mins


def num0s(val, mins=0):
    return val if numberDtype(val) and 0 <= val else mins


def num0(val, mins=0):
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
    if not numberDtype(mins) or not numberDtype(maxs):
        return others
    if maxs < mins:
        mins, maxs = maxs, mins
    if mins <= val <= maxs:
        return val
    return others
