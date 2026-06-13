import numpy as np

from ..base import baseDtype

__all__ = [
    "complexDtype",
    "floatDtype",
    "intDtype",
    "integerDtype",
    "numberDtype",
    "uintDtype",
]


class complexDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, np.complexfloating, np.complex64, np.complex128)


class floatDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, [np.float16, np.float32, np.float64, np.floating])


class intDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, [np.int8, np.int16, np.int32, np.int64])


class integerDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(
            arr,
            [
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.uint8,
                np.uint16,
                np.uint32,
                np.uint64,
            ],
        )


class numberDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(
            arr,
            [
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.uint8,
                np.uint16,
                np.uint32,
                np.uint64,
                np.float16,
                np.float32,
                np.float64,
                np.floating,
                np.complexfloating,
                np.complex64,
                np.complex128,
            ],
        )


class uintDtype(baseDtype):
    def __init__(self, arr):
        super().__init__(arr, [np.uint, np.uint8, np.uint16, np.uint32, np.uint64])
