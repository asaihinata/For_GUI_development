from ....typing import *
from .._2gset import _2Gset

__all__ = ["Boxplot"]

class Boxplot(_2Gset):
    def update(
        self,
        data: n_array,
        width: int | float,
        whis: int | float,
        label: labeltype,
        legend: bool,
        fill: bool,
        notch: bool,
        showfliers: bool,
        orientation: Literal["horizontal", "vertical"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        xlabel: str,
        ylabel: str,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """箱ひげ図を再表示させる"""

    def get(self) -> list[dict[str, Any]]:
        """`matplotlib.axes.Axes.boxplot`の戻り値の配列を返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
