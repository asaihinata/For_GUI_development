from collections.abc import Iterator
from typing import Any, overload

from matplotlib.typing import ColorType
import numpy as np

__all__ = ["Color"]

class Color:
    __dict__: dict[str, Any]
    color: np.ndarray
    @overload
    def __init__(
        self,
        color: (
            ColorType
            | str
            | list[ColorType]
            | tuple[ColorType, ...]
            | np.ndarray[ColorType]
        ),
        keep_alpha: bool = ...,
    ) -> None: ...
    def tohex(self, keep_alpha: bool = False) -> Color: ...
    def torgba(self, alpha: int | float | None = None) -> Color: ...
    def torgb(self) -> Color: ...
    def __iter__(self) -> Iterator[ColorType]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, val: int | slice) -> Any: ...
    @classmethod
    def colorname(cls) -> list[str]:
        """CSS4で指定できる色名の配列を返す"""

    @classmethod
    def colorhex(cls) -> list[str]:
        """CSS4で指定できる色名の16進数の配列を返す"""
