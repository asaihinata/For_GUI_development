"""numpyの時間に関するdtype"""

import numpy as np

from ..base import baseDtype

__all__ = ["datetimeDtype", "timedeltaDtype"]


class datetimeDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, np.datetime64)


class timedeltaDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, np.timedelta64)
