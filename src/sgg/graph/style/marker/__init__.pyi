"""マーカーを設定するモジュール"""

from typing import Any, Literal

import numpy as np
from matplotlib.markers import MarkerStyle

from sgg._typing import Type_Marker

__all__ = ["Marker"]

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
    def __contains__(self, value: Any) -> bool: ...
