from matplotlib.patches import StepPatch

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Step"]

class Step(_2Gset):
    def update(
        self,
        data: TypeArraysLikeNumber,
        linewidth: int | float,
        range: (
            int
            | float
            | list[int | float, int | float]
            | tuple[int | float, int | float]
        ),
        fill: bool,
        baseline: int | float,
        orientation: Literal["horizontal", "vertical"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
        label: str | list[str] | None,
    ) -> None:
        """階段グラフを再表示させる"""

    def get(self) -> list[StepPatch]:
        """`matplotlib.patches.StepPatch`の配列を返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
