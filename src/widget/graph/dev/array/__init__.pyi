from collections.abc import Iterator
from typing import Any
from numpy import _ArrayT,_CopyMode,_DTypeT_co,ndarray
__all__:list[str]=['Array']
class Array:
 dtype:_DTypeT_co|None
 data:ndarray
 def __init__(
self,
data:_ArrayT,
*,
dtype:_DTypeT_co|None=None
)->None:...
 def __iter__(self)->Iterator[Any]:...
 def __array__(
self,
dtype:_DTypeT_co|None=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def tolist(self)->Any:...
 def sort(self)->ndarray:...