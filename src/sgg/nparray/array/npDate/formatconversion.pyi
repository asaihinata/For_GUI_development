from numpy import _ArrayT

from ..nparray import NPArray
from ._typing import _DATES_UNIT

__all__ = ["Formatconversion"]

class Formatconversion(NPArray):
    def __init__(
        self,
        data: _ArrayT,
        dtype: _DATES_UNIT = "datetime64[D]",
        yearfirst: bool = ...,
        dayfirst: bool = ...,
    ) -> None:
        """様々な日付のフォーマットを特定の日付フォーマットに変換する"""

    def __repr__(self) -> str: ...
