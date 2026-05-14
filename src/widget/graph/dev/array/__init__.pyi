from collections.abc import Iterator
from typing import Any
import numpy as np
from numpy import _ArrayT,_CopyMode,ndarray
__all__:list[str]=['Array']
class Array:
 dtype:np._DTypeT_co|None
 data:ndarray
 def __init__(
self,
data:_ArrayT,
*,
dtype:np._DTypeT_co|None=None
)->None:...
 def __iter__(self)->Iterator[Any]:...
 def __array__(
self,
dtype:np._DTypeT_co|None=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def tolist(self)->Any:...
 def sort(self)->ndarray:...