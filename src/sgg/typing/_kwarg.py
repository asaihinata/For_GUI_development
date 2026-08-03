from typing import Literal, TypedDict

from sgg.typing import ColorTypeN

__all__ = [
    "Dict_2DGraph",
    "Dict_3DGraph",
    "Dict_LinefillGraph",
    "Dict_Polar",
    "Dict_Radar",
]


# 基本的なウィジェットのキーワード引数の型ヒントを保存するオブジェクト
class _Dict_Graph_base(TypedDict):
    key: str | None = ...
    title: str = ...
    size: tuple[int | float, int | float] = (500, 400)
    dpi: int | float = 100
    fg: ColorTypeN = "#000000"
    bg: ColorTypeN = "#ffffff"
    tight_layout: bool = True


class Dict_2DGraph(_Dict_Graph_base):
    alpha: int | float = 1.0
    xlabel: str = ...
    ylabel: str = ...
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    xmajorint: bool = True
    ymajorint: bool = True
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
    xticksdirection: Literal["out", "in", "inout"] = "out"
    yticksdirection: Literal["out", "in", "inout"] = "out"


class Dict_LinefillGraph(_Dict_Graph_base):
    xlabel: str = ...
    ylabel: str = ...
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    xmajorint: bool = True
    ymajorint: bool = True
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
    xticksdirection: Literal["out", "in", "inout"] = "out"
    yticksdirection: Literal["out", "in", "inout"] = "out"


class Dict_3DGraph(_Dict_Graph_base):
    alpha: int | float = 1.0
    xlabel: str = ...
    ylabel: str = ...
    zlabel: str = ...
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xyz: bool = True
    grid_x: bool = False
    grid_y: bool = False
    grid_z: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    xmajorint: bool = True
    ymajorint: bool = True
    zmajorint: bool = True
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
    zticksshow: bool = False
    xticksdirection: Literal["out", "in", "inout"] = "out"
    yticksdirection: Literal["out", "in", "inout"] = "out"
    znumticks: int | float | None = None
    mouse_rotation: bool = True
    elev: int | float = 30
    azim: int | float = 45


class Dict_Polar(_Dict_Graph_base):
    alpha: int | float = 1.0
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    xticksrange: int | float | tuple[int | float, int | float] = 0
    yticksrange: int | float | tuple[int | float, int | float] = 0
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False


class Dict_Radar(_Dict_Graph_base):
    alpha: int | float = 1.0
    graph_grid: ColorTypeN = "#b7b7b7"
    grid_xy: bool = True
    grid_x: bool = False
    grid_y: bool = False
    ticksshow: bool = False
    xticksshow: bool = False
    yticksshow: bool = False
