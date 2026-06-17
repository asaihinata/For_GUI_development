"""マーカーを設定するモジュール"""

from collections.abc import Iterator
from typing import Any, Literal

from matplotlib.markers import MarkerStyle
import numpy as np

from ....nparray import NPArray
from ...typing import Type_Marker

__all__ = ["Marker", "MarkerList"]

class Marker:
    marker_list: list[int | str]
    marker: MarkerStyle
    def __init__(
        self,
        marker: str | int | Type_Marker,
        fill: Literal["full", "left", "right", "bottom", "top", "none"] | None = None,
        cap: Literal["butt", "round", "projecting"] | None = None,
        transform: np.number | None = None,
        join: Literal["miter", "round", "bevel"] | None = None,
    ) -> None: ...
    def __contains__(self, item: Any) -> bool: ...

class MarkerList(NPArray):
    def __init__(
        self,
        marker: str | int | Type_Marker,
        fill: Literal["full", "left", "right", "bottom", "top", "none"] | None = None,
        cap: Literal["butt", "round", "projecting"] | None = None,
        transform: np.number | None = None,
        join: Literal["miter", "round", "bevel"] | None = None,
    ) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, key: int) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
