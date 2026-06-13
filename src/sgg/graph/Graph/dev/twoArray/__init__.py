"""グラフ用の配列作成モジュール"""

from itertools import product

from numpy import append, array, concatenate

__all__ = ["TwoArray"]


class TwoArray:
    def __init__(self, x, y, xdtype=object, ydtype=object):
        self.__x = array(x, dtype=xdtype)
        self.__y = array(y, dtype=ydtype)
        if self.__x.ndim == 1:
            self.__x = array([x], dtype=xdtype)
        if self.__y.ndim == 1:
            self.__y = array([y], dtype=ydtype)
        data = []
        self.__data = [
            (
                [concatenate([[xs], [ys]])]
                if len(data) == 0
                else append(data, [concatenate([[xs], [ys]])], axis=0)
            )
            for xs, ys in product(self.__x, self.__y)
        ]

    def __repr__(self):
        return f"TwoArray({self.__data})"

    def __iter__(self):
        for i in self.__data:
            yield i[0]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def data(self):
        return self.__data
