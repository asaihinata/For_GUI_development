import japanize_matplotlib
import numpy as np

from sgg.dev import *
from sgg.graph.element import (RadarElement, polarElement, radar_factory,
                               threeElement, twoElement)
from sgg.graph.style import *
from sgg.nparray import *

from .threearray import ThreeArray
from .twoarray import TwoArray


def parameters(vals, do1, do2):
    """
    :param vals: Noneかを調べる値を指定する
    :type vals: Any
    :param do1: `vals`がNoneの時に返す値を指定する
    :type do1: Any
    :param do2: `vals`がNoneではない時に返す値を指定する
    :type do2: Any
    """
    return do1 if vals == None else do2


def lengtharange(data):
    data = np.array(data)
    shapes = data.shape
    lens = len(shapes)
    if lens == 1:
        raw = np.arange(0, data.size, 1)
    else:
        raw = np.tile(np.arange(0, shapes[lens - 1]), np.prod(shapes[:-1])).reshape(
            shapes
        )
    return np.array(raw, dtype=np.uint64)
