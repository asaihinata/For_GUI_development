from collections.abc import Iterator
from types import NotImplementedType
from typing import Any,Literal
from numpy import ndarray,timedelta64,ufunc,_CopyMode
from numpy._typing import DTypeLike
from ..base import NPArray
from .data import Dtype
__all__=['NPDate']
class NPDate(NPArray):
 data:ndarray
 def __init__(
self,
data:list|tuple|ndarray,
dtype:Dtype|None='datetime64[D]',
depth_limit:int|None=None
)->None:'''
 :param data: データの配列を指定する。
 :type data: list|tuple|ndarray
 :param dtype: numpyの配列で指定する型を指定する。
 :type dtype: DTypeLike|None
 :param depth_limit: 配列の最大の深さを指定する。
 :type depth_limit: int|None'''
 def __iter__(self)->Iterator[Any]:...
 def __getitem__(self,key:int)->Any:...
 def __contains__(self,item:Any)->bool:...
 def __iter__(self)->Iterator[Any]:...
 def __len__(self)->int:...
 def __reversed__(self)->NPDate:'''`numpy.fliplr`を実行する'''
 def __array__(
self,
dtype:DTypeLike|None=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def __repr__(self)->str:...
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