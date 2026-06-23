from matplotlib.collections import QuadMesh

from ....typing import *
from .._2gset import _2Gset

__all__ = []

class Hist2d(_2Gset):
    def update(
        self,
        x: o_array,
        y: o_array,
        max: int | float,
        min: int | float,
        xmax: int | float,
        xmin: int | float,
        ymax: int | float,
        ymin: int | float,
        bins: int | TupleInt2 | ArrayLike | tuple[ArrayLike, ArrayLike],
        density: bool,
        fg: ColorType,
        bg: ColorType,
        alpha: int | float,
        graph_grid: ColorType,
        title: str,
    ) -> None:
        """2次元ヒストグラムを再表示させる

        :raises TypeError: `x`もしくは`y`もしくはその両方が二次元配列以上の多次元配列の場合に発生させる
        :raises TypeError: `x`と`y`の要素の数が同じではない時に発生させる"""

    def get(self) -> list[ndarray, ndarray, ndarray, QuadMesh]:
        """`matplotlib.axes.Axes.hist2d`の戻り値を配列で返す"""

    def getx(self) -> Typeget_data:
        """`x`のデータを取得する"""

    def gety(self) -> Typeget_data:
        """`y`のデータを取得する"""
