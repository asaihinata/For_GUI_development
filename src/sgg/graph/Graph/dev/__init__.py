import japanize_matplotlib
import numpy as np

from ....dev import *
from ....nparray import *
from ...element import (RadarElement, polarElement, radar_factory, threeElement,
                        twoElement)
from ...style import *
from ...typing import *
from .twoarray import TwoArray


def parameters(vals: Any, do1: Any, do2: Any) -> Any:
    """
    :param vals: Noneかを調べる値を指定する
    :type vals: Any
    :param do1: `vals`がNoneの時に返す値を指定する
    :type do1: Any
    :param do2: `vals`がNoneではない時に返す値を指定する
    :type do2: Any
    """
    return do1 if vals == None else do2
