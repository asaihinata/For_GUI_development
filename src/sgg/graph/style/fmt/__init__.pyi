"""マーカー,線種,色を一度に設定するモジュール"""

from collections.abc import Iterator
from typing import Literal, TypeAlias

import numpy as np

from ....nparray import NPString

__all__ = ["FMT", "fmtstyle", "FMTLineList", "FMTColorList", "FMTMarkList"]
MarkerType: TypeAlias = Literal[
    ".",
    ",",
    "o",
    "v",
    "^",
    "<",
    ">",
    "1",
    "2",
    "3",
    "4",
    "8",
    "s",
    "p",
    "P",
    "*",
    "h",
    "H",
    "+",
    "x",
    "X",
    "D",
    "d",
    "|",
    "_",
]

class FMT:
    def __init__(
        self,
        marker: MarkerType | None = None,
        solid: Literal["-", "--", "-.", ":"] | None = None,
        color: Literal["b", "g", "r", "c", "m", "y", "k", "w"] | None = None,
    ) -> None: ...
    def __str__(self) -> str: ...
    @property
    def txt(self) -> str: ...

class fmtstyle:
    def __init__(
        self,
        arr: np.typing.ArrayLike,
        style: Literal["color", "marker", "solid"] = "color",
    ) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    @property
    def arr(self) -> np.ndarray: ...

class FMTLineList(NPString):
    def __init__(self, data) -> None: ...

class FMTColorList(NPString):
    def __init__(self, data) -> None: ...

class FMTMarkList(NPString):
    def __init__(self, data) -> None: ...
