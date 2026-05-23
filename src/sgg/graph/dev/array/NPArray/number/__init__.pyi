from numpy import _ArrayT
from numpy._typing import DTypeLike
from ..base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 def __init__(
self,
data:_ArrayT,
dtype:DTypeLike|None=None
)->None:...
 def cussum(self)->NPNumber:'''一つ前の元の値との和を求める。'''
 def cumprod(self)->NPNumber:'''一つ前の元の値との積を求める。'''