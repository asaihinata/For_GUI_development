'''基本的な文字列操作をするモジュール'''
from types import NotImplementedType
from typing import Any,Literal
from _typeshed import Incomplete
from numpy import _ArrayT,_CopyMode,float64,ndarray,ufunc
from numpy._typing import DTypeLike
from ..base import NPArray
__all__=['NPString']
class NPString(NPArray):
 data:ndarray
 name:str
 def __init__(
self,
data:_ArrayT,
dtype:DTypeLike=float64,
axis:int|None=None
)->None:...
 def __repr__(self)->str:...
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
)->ndarray|NPString|Any|NotImplementedType:...
 def __add__(self,other:ndarray|NPString)->NPString:...
 def __mul__(self,other:int)->NPString:''':raises TypeError: `other`に`int`型以外で指定した場合に発生させる'''
 __radd__=__add__
 __rmul__=__mul__
 def __eq__(self,value:ndarray|NPString)->ndarray[Incomplete]:...
 def __ne__(self,value:ndarray|NPString)->ndarray[Incomplete]:...
 def append(self,val:ndarray|NPString)->NPString:...
 def low(self)->NPString:'''アルファベットを小文字にする。'''
 def upper(self)->NPString:'''アルファベットを大文字にする。'''