"""
色データを保管,色データを取得するモジュール

color.csvはhttps://drafts.csswg.org/css-color-4/#named-colorsを元に作成
"""

from pathlib import Path

from numpy import ndarray, str_, where

from ...readfile import Getcsv
from ..npArray import NPArray

__all__ = ["Get_color"]


class Get_color(NPArray):
    """色データを取得する"""

    colordata = Getcsv(Path(__file__).parent / "color.csv").get_numpy()

    def __init__(self):
        """色データを取得する"""
        super().__init__(self.colordata, dtype=str_)

    def __repr__(self):
        return f"Get_color({self.data})"

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if method == "__call__":
            args = [x.data if isinstance(x, Get_color) else x for x in args]
            result = ufunc(*args, **kwargs)
            if isinstance(result, ndarray):
                return Get_color(result)
            return result
        return NotImplemented

    @classmethod
    def gets(cls, colorname):
        cds = Get_color.colordata
        c, _ = where(colorname == cds)
        if c.size == 0:
            return None
        return cds[c][0]
