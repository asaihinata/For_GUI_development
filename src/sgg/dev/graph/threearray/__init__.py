"""グラフ用の配列作成モジュール"""

from itertools import product

import numpy as np

__all__ = ["ThreeArray"]


class ThreeArray:
    def __init__(self, x, y, z):
        self.__x = np.asanyarray(x, dtype=np.float64)
        self.__y = np.asanyarray(y, dtype=np.float64)
        self.__z = np.asanyarray(z, dtype=np.float64)
        if self.__x.ndim == 1:
            self.__x = np.asanyarray([x], dtype=np.float64)
        if self.__y.ndim == 1:
            self.__y = np.asanyarray([y], dtype=np.float64)
        if self.__z.ndim == 1:
            self.__z = np.asanyarray([z], dtype=np.float64)
        data = []
        self.__data = [
            (
                [np.concatenate([[xs], [ys], [zs]])]
                if len(data) == 0
                else np.append(data, [np.concatenate([[xs], [ys], [zs]])], axis=0)
            )
            for xs, ys, zs in product(self.__x, self.__y, self.__z)
        ]

    def __repr__(self):
        return f"ThreeArray({self.__data})"

    def __iter__(self):
        for i in self.__data:
            yield i[0][0], i[0][1], i[0][2]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @property
    def data(self):
        return self.__data
