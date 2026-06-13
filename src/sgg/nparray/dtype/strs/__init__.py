import numpy as np

from ..base import baseDtype

__all__ = ["bytesDtype", "strDtype", "stringDtype"]


class bytesDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, np.bytes_)


class strDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, np.str_)


class stringDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, [np.str_, np.bytes_])
