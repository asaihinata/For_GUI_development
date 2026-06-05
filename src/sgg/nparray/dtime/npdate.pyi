from collections.abc import Iterator
from datetime import tzinfo
from types import NotImplementedType
from typing import Any,Literal,overload
import numpy as np
from numpy._typing import DTypeLike
from ..base import NPArray
from .data import Dtype_ALL
__all__=['NPDate']
class NPDate(NPArray):
 data:np.ndarray
 def __init__(
self,
data:list|tuple|np.ndarray,
dtype:Dtype_ALL|None='datetime64[D]',
depth_limit:int|None=None
)->None:'''
 :param data: データの配列を指定する。
 :type data: list|tuple|np.ndarray
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
copy:bool|np._CopyMode|None=None
)->np.ndarray:...
 def __repr__(self)->str:...
 def __array_ufunc__(
self,
ufunc:np.ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args:Any,
**kwargs:Any
)->Any|NotImplementedType|NPDate:...
 @property
 def T(self)->NPDate:...
 def astype(self,dtype:Dtype_ALL)->NPDate:...
 @property
 def max(self)->np.timedelta64:'''NPDate内の最大の日付を取得する。'''
 @property
 def min(self)->np.timedelta64:'''NPDate内の最小の日付を取得する。'''
 def __add__(self,other:np.timedelta64|int)->NPDate:...
 def __sub__(self,other:np.timedelta64|int)->NPDate:...
 __radd__=__add__
 __rsub__=__sub__
 @classmethod
 def today(cls,unit=None)->NPDate:'''今日の日付を返す。'''
 def tostr(
self,
unit:Literal['auto','Y','M','D','h','m','s','ms','us','μs','ns','ps','fs','as']|None=None,
timezone:Literal['naive','UTC','local']|tzinfo='naive',
casting:Literal['no','equiv','safe','same_kind','same_value','unsafe']='same_kind'
):'''配列内の日付を`str`型に変換する。'''
 def todatetime(self):'''配列内の日付を`datetime.datetime`に変換する。'''
 def weekday(self):'''その日付の曜日を求める。'''
 @overload
 def diff_today(
self,
days:bool=...
):'''今日の日付の差を求める。

 :param days: 今日を含めるか指定する。
 :type days: bool'''
 @overload
 def diff_today(
self,
days:bool=True
):'''今日の日付の差(今日を含む)を求める。

 :param days: 今日を含めるか指定する。
 :type days: bool'''
 @overload
 def diff_today(
self,
days:bool=False
):'''今日の日付の差(今日を含めない)を求める。

 :param days: 今日を含めるか指定する。
 :type days: bool'''