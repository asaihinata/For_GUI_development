'''グラフで使用する配列を作成するモジュール'''
from collections.abc import Iterator
from types import NotImplementedType
from typing import Any,Literal
from numpy import ndarray,ufunc,_CopyMode
from numpy._typing import DTypeLike
from ..base import NPArray
__all__=['NPGraph']
class NPGraph(NPArray):
 data:ndarray
 serial_num:ndarray
 def __init__(
self,
data:list|tuple|ndarray,
dtype:DTypeLike=None,
depth_limit:int|None=None,
)->None:...
 def __getitem__(self,key:int)->Any:...
 def __contains__(self,item:Any)->bool:...
 def __iter__(self)->Iterator[Any]:...
 def __len__(self)->int:...
 def __reversed__(self)->NPGraph:'''`numpy.fliplr`を実行する'''
 def __array__(
self,
dtype:DTypeLike|None=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def __array_ufunc__(
self,
ufunc:ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args:Any,
**kwargs:Any
)->Any|NotImplementedType|NPGraph:...
 @property
 def T(self):
  self.data=self.data.T
  return self
 @property
 def serial(self)->ndarray:...
 def gets(self)->tuple[ndarray,ndarray]:...