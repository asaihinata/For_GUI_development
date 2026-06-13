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
    if not isinstance(val, int | float) or not isinstance(mins, int | float):
        return other
    if mins < val:
        return val
    return other


def nums(val, other=None):
    return val if isinstance(val, int | float) else other


def num1s(val=0, mins=1):
    return val if isinstance(val, int | float) and 1 <= val else mins


def num0s(val=0, mins=0):
    return val if isinstance(val, int | float) and 0 <= val else mins


def num0(val=0, mins=0):
    return val if isinstance(val, int | float) and 0 < val else mins


def intsmin(val, mins=0, other=None):
    if not isinstance(val, int) or not isinstance(mins, int):
        return other
    if mins < val:
        return val
    return other


def ints(val=0, other=None):
    return val if isinstance(val, int) else other


def int1s(val=0, mins=1):
    return val if isinstance(val, int) and 1 <= val else mins


def int0s(val=0, mins=0):
    return val if isinstance(val, int) and 0 <= val else mins


def int0(val=0, mins=0):
    return val if isinstance(val, int) and 0 < val else mins


def range_num(val, mins=None, maxs=None, others=None):
    if (not isinstance(mins, int | float)) or (not isinstance(maxs, int | float)):
        return others
    if maxs < mins:
        mins, maxs = maxs, mins
    if mins <= val <= maxs:
        return val
    return others
