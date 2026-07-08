import japanize_matplotlib
import numpy as np

from sgg.dev import *
from sgg.graph.element import (RadarElement, polarElement, radar_factory,
                               threeElement, twoElement)
from sgg.graph.style import *
from sgg.graph.typing import *
from sgg.nparray import *

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
