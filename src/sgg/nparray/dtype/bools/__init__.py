import numpy as np

from ..base import baseDtype

__all__ = ["boolDtype"]


class boolDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, np.bool_)
