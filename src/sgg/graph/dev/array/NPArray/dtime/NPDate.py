from ..base import NPArray
from .data import serch_dtype
from .Formatconversion import Formatconversion
class NPDate(NPArray):
 def __init__(self,data,dtype='datetime64[ms]'):
  if isinstance(data,Formatconversion):data=data.data
  super().__init__(data,dtype=serch_dtype(dtype))
  self.datelist=self.data