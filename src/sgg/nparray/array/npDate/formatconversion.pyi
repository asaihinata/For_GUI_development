from numpy import _ArrayT

from ..nparray import NPArray
from ._typing import _DATES_UNIT

__all__ = ["Formatconversion"]

class Formatconversion(NPArray):
    def __new__(
        cls,
        data: _ArrayT,
        dtype: _DATES_UNIT = "datetime64[D]",
        yearfirst: bool = ...,
        dayfirst: bool = ...,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Formatconversion:
        """様々な日付のフォーマットを特定の日付フォーマットに変換する"""
