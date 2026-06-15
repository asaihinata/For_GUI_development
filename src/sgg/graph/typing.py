"""src/widget/graphモジュール全体の型ヒント"""

from typing import Literal, TypeAlias

from numpy import dtype, float64, ndarray
from numpy._typing import NDArray, _AnyShape

from ..typing import *

Type_Solid: TypeAlias = Literal["-", "--", "-.", ":", "None", " ", ""]
Type_Marker: TypeAlias = Literal[
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
Typeget_data: TypeAlias = ndarray[_AnyShape, dtype[Any]]
Typetuple_float64: TypeAlias = tuple[float64, float64]
