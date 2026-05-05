from typing import TypeAlias,TypeVar
import numpy as np
class LIST:pass
class Number:pass
_T=TypeVar('_T')
Numberlike:TypeAlias=(
 bool|
 np.bool|
 float|
 int|
 Number|
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