from typing import TypeAlias
from matplotlib.typing import ColorType
import numpy as np
__all__=['ColorType','NumberNone','Numberlike']
NumberNone:TypeAlias=int|float|None
Numberlike:TypeAlias=(
 bool|
 np.bool|
 float|
 int|
 np.float16|
 np.float32|
 np.float64|
 np.int16|
 np.int32|
 np.int64|
 np.int8|
 np.uint16|
 np.uint32|
 np.uint64|
 np.uint8
)