from collections.abc import Iterator
from types import NotImplementedType
from typing import Literal,TypeAlias
from numpy import _ArrayT,_CopyMode,_ScalarT,dtype,ndarray,ufunc
from numpy._typing import DTypeLike
from ...typing import Any,ndarray
_Array1D:TypeAlias=ndarray[tuple[int],dtype[_ScalarT]]
__all__=['NPArray']
class NPArray:
 dtype:DTypeLike
 data:ndarray
 name:str
 def __init__(
self,
data:_ArrayT,
dtype:DTypeLike|None=None
)->None:...
 def __repr__(self)->str:...
 def __iter__(self)->Iterator[Any]:...
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
)->NPArray|Any|NotImplementedType:...
 def tolist(self)->Any|list:'''list型に変換する。

 :return:
 :rtype: Any|list'''
 def sort(self)->NPArray:'''`data`にソートを実行する。

 :return:
 :rtype: NPArray'''
 def first_pop(self)->NPArray:'''配列の最初の要素のコピーをその配列の末尾に追加する。

 :return:
 :rtype: NPArray'''
 @property
 def T(self)->NPArray:...
 @property
 def ndim(self)->int:...
 @property
 def shape(self)->tuple[int,...]:...
 @property
 def size(self)->int:...
 def astype(
self,
dtype:DTypeLike|None
)->NPArray:'''`dtype`で指定された型に変更します。'''
 def lengtharange(
self,
start:int=0,
dtype:DTypeLike|None=None
)->ndarray:...
 def _flatten(self)->tuple[_Array1D,tuple[int,...]]:...
 def flatten(self)->NPArray:...
 def dimension(self)->bool:'''`data`の次元が1次元か判定する。'''
 def dimensions(self)->bool:'''`data`の次元が多次元か判定する。'''