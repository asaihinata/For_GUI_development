from numpy import _ArrayT,ndarray,timedelta64
from ...base import NPArray
from ..typing import Dtype
class NPDate(NPArray):
 data:ndarray
 def __init__(
self,
data:_ArrayT,
dtype:Dtype|None='datetime64[D]'
)->None:...
 @classmethod
 def arange(
cls,
start,
stop,
dtype:Dtype|None='datetime64[D]'
)->NPDate:...
 def __add__(self,other:timedelta64)->NPDate:...
 def __sub__(self,other:timedelta64)->NPDate:...
 __radd__=__add__
 __rsub__=__sub__