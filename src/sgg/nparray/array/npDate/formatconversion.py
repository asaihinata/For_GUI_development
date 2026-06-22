from dateutil.parser import parse
from numpy import array, ndarray, nditer, vectorize

from ..nparray import NPArray, is_array_like
from ._typing import serchDtype

__all__ = ["Formatconversion"]


class Formatconversion(NPArray):
    def __init__(self, data, dtype="datetime64[D]", yearfirst=False, dayfirst=False):
        if not is_array_like(data):
            raise TypeError(
                f"dataには配列もしくは__array__を持つオブジェクトを指定してください"
            )
        if not isinstance(data, ndarray):
            data = array(data)
        if not isinstance(yearfirst, bool):
            yearfirst = False
        if not isinstance(dayfirst, bool):
            dayfirst = False
        dtype = serchDtype(dtype)
        func = vectorize(
            lambda strs, yearfirst, dayfirst: str(
                parse(str(strs), yearfirst=yearfirst, dayfirst=dayfirst)
            )
        )
        datas = array([func(i, yearfirst, dayfirst) for i in nditer(data)], dtype=dtype)
        datas = datas.reshape(data.shape)
        super().__init__(datas, dtype)

    def __repr__(self):
        return f"Formatconversion({self.data})"
