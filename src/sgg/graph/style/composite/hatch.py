"""塗りつぶし領域の領域内のマーカーを設定するモジュール"""

from re import compile

import numpy as np

from sgg.nparray import NPBool, NPString

__all__ = ["Hatch"]


class Hatch(NPString):

    def __new__(cls, hatch):
        if hatch in ["", None]:
            hatch = [""]
        elif isinstance(hatch, str):
            hatch = [hatch]
        datas = super().__new__(cls, hatch, max_ndim=1)
        if not NPBool(
            [np.vectorize(lambda x=i: bool(compile(r"^[/\\|\-+xo*O.]+$").fullmatch(x)))]
            for i in np.nditer(datas)
        ).all():
            raise ValueError("指定できない値が含まれています")
        return datas

    def __getitem__(self, key):
        return super().__getitem__(key)
