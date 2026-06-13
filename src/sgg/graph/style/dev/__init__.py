import numpy as np

__all__ = [
    "bol",
    "bols",
    "listchose",
    "list2float",
    "list2number",
    "num0",
    "num0s",
    "num1s",
    "range_zero_one",
]


def range_zero_one(val, out=1.0, endpoint=True):
    if not isinstance(val, np.number):
        return out
    if not isinstance(endpoint, bool):
        endpoint = True
    if endpoint and 0 <= val <= 1:
        return val
    elif not endpoint and 0 <= val < 1:
        return val
    return out


def num1s(val=0, mins=1):
    if isinstance(val, np.number) and 1 <= val:
        return val
    return mins


def num0s(val=0, mins=0):
    if isinstance(val, np.number) and 0 <= val:
        return val
    return mins


def num0(val=0, mins=0):
    if isinstance(val, np.number) and 0 < val:
        return val
    return mins


def list2number(lin=None):
    if (
        isinstance(lin, list | tuple)
        and len(lin) == 2
        and all(isinstance(i, np.number) for i in lin)
    ):
        return True
    return False


def list2float(lin=None):
    if (
        isinstance(lin, list | tuple)
        and len(lin) == 2
        and all(isinstance(i, float) for i in lin)
    ):
        return True
    return False


def bol(vals, other=False):
    if isinstance(vals, bool):
        return vals
    return other


def bols(bools, trus=None, fals=None):
    if isinstance(bools, bool):
        return trus
    return fals


def listchose(val, arr, other=None):
    if isinstance(arr, tuple | list) and other == None:
        other = arr[0]
    elif not isinstance(arr, tuple | list) and other == None:
        other = arr
    if val in arr:
        return val
    return other
