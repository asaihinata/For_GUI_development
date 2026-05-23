from numpy import _ArrayT
from ..base import NPArray
from .data import TypeDlike
__all__=['Formatconversion']
class Formatconversion(NPArray):
 def __init__(
self,
data:_ArrayT,
dtype:TypeDlike=None,
yearfirst:bool=...,
dayfirst:bool=...
)->None:...