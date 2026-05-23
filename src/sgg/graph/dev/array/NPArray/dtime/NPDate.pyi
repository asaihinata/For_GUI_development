from numpy import _ArrayT
from ..base import NPArray
from .data import TypeDlike
class NPDate(NPArray):
 def __init__(
self,
data:_ArrayT,
dtype:TypeDlike='datetime64[ms]'
)->None:...