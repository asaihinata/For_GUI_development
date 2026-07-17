from typing import Literal

# dialogのアイコン
type Type_icon = Literal["error", "info", "question", "warning"]
# グラフウィジェット
type Type_Solid = Literal["-", "--", "-.", ":", "None", " ", ""]
type Type_Marker = Literal[
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
    "*",
    "h",
    "H",
    "+",
    "x",
    "D",
    "d",
    "|",
    "_",
    "P",
    "X",
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    "None",
    "none",
    " ",
    "",
]
# 色
type ColorType = str
type ColorTypeN = str | None
