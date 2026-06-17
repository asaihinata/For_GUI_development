from matplotlib.mlab import GaussianKDE

from ....typing import *
from .._2gset import _2Gset

__all__ = ["Violinplot"]

class Violinplot(_2Gset):
    def update(
        self,
        data: n_array,
        x: o_array,
        y: o_array,
        orientation: Literal["vertical", "horizontal"],
        width: int | float,
        showextrema: bool,
        showmeans: bool,
        showmedians: bool,
        points: int | float,
        bw_method: (
            Literal["scott", "silverman"] | float | Callable[[GaussianKDE], float]
        ),
        side: Literal["both", "low", "high"],
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """バイオリングラフを再表示させる"""

    def get(self) -> list[dict[str, Collection]]:
        """`matplotlib.axes.Axes.violinplot`のバイオリンプロットの各コンポーネントの辞書型が入った配列を返す"""

    def getdata(self) -> Typeget_data:
        """`data`のデータを取得する"""
