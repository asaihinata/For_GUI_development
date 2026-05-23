from numpy import _ArrayT,ndarray,timedelta64
from ...base import NPArray
from ..typing import Dtype
__all__=['NPDate']
class NPDate(NPArray):
 data:ndarray
 def __init__(
self,
data:_ArrayT,
dtype:Dtype|None='datetime64[D]'
)->None:...
 def astype(self,dtype:Dtype)->NPDate:...
 @property
 def max(self)->timedelta64:"""NPDate内の最大の日付を取得する。"""
 @property
 def min(self)->timedelta64:"""NPDate内の最小の日付を取得する。"""
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