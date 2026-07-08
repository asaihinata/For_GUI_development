"""src/widget/graphモジュール全体の型ヒント"""

from typing import Literal, TypeAlias

import numpy as np

from sgg.typing import *

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
Typeget_Arrays_Number: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[np.number]]
Typeget_Arrays_NumStr: TypeAlias = np.ndarray[
    tuple[int, ...], np.dtype[np.number | np.character]
]
Typeget_Arrays: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[Any]]
Typeget_Array_Number: TypeAlias = np.ndarray[tuple[int], np.dtype[np.number]]
Typeget_Array_NumStr: TypeAlias = np.ndarray[
    tuple[int], np.dtype[np.number | np.character]
]
Typeget_Array: TypeAlias = np.ndarray[tuple[int], np.dtype[np.number]]
Typetuple_float64: TypeAlias = tuple[np.float64, np.float64]
