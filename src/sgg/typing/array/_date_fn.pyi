from typing import Literal

from ._date import DateUnitSet, MDateUnitSet

__all__ = ["_dt64_unit", "_get_dt64_unit"]

def _dt64_unit(spec: Literal[DateUnitSet]) -> str: ...
def _get_dt64_unit(dtype_str: Literal[MDateUnitSet], auto: str = "D") -> str: ...
