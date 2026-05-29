from collections.abc import Iterator
from types import NotImplementedType
from typing import Any,Literal
from numpy import ndarray,timedelta64,ufunc
from ...base import NPArray
from ..typing import Dtype
__all__=['NPDate']
class NPDate(NPArray):
 data:ndarray
 name:str
 def __init__(
self,
data:list|tuple|ndarray,
dtype:Dtype|None='datetime64[D]'
)->None:...
 def __repr__(self)->str:...
 def __iter__(self)->Iterator[Any]:...
 def __array_ufunc__(
self,
ufunc:ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args:Any,
**kwargs:Any
)->Any|NotImplementedType|NPDate:...
 @property
 def T(self)->NPDate:...
 def astype(self,dtype:Dtype)->NPDate:...
 @property
 def max(self)->timedelta64:'''NPDate内の最大の日付を取得する。'''
 @property
 def min(self)->timedelta64:'''NPDate内の最小の日付を取得する。'''
 @classmethod
 def arange(
cls,
start,
stop,
dtype:Dtype|None='datetime64[D]'
)->NPDate:...
 def __add__(self,other:timedelta64|int)->NPDate:...
 def __sub__(self,other:timedelta64|int)->NPDate:...
 __radd__=__add__
 __rsub__=__sub__