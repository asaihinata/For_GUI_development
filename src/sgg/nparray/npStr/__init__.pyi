'''基本的な文字列操作をするモジュール'''
from collections.abc import Iterator
from types import NotImplementedType
from typing import Any,Literal
from _typeshed import Incomplete
from numpy import _CopyMode,str_,ndarray,ufunc
from numpy._typing import DTypeLike
from ..base import NPArray
__all__=['NPString']
class NPString(NPArray):
 data:ndarray
 name:str
 def __init__(
self,
data:list|tuple|ndarray,
dtype:DTypeLike=str_,
depth_limit:int|None=None
)->None:'''
 :param data: データの配列を指定する。
 :type data: list|tuple|ndarray
 :param dtype: numpyの配列で指定する型を指定する。
 :type dtype: DTypeLike|None
 :param depth_limit: 配列の最大の深さを指定する。
 :type depth_limit: int|None'''
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
)->Any|NotImplementedType|NPString:...
 def __add__(self,other:ndarray|NPString)->NPString:...
 def __mul__(self,other:int)->NPString:''':raises TypeError: `other`に`int`型以外で指定した場合に発生させる'''
 __radd__=__add__
 __rmul__=__mul__
 def __eq__(self,value:ndarray|NPString)->ndarray[Incomplete]:...
 def __ne__(self,value:ndarray|NPString)->ndarray[Incomplete]:...
 @property
 def T(self)->NPString:...
 def append(self,val:ndarray|NPString)->NPString:...
 def low(self)->NPString:'''アルファベットを小文字にする。'''
 def upper(self)->NPString:'''アルファベットを大文字にする。'''