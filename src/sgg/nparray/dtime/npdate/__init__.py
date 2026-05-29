import numpy as np
from ...base import NPArray
from ..data import serch_dtype
from ..conversion import Formatconversion,conversions
__all__=['NPDate']
class NPDate(NPArray):
 name='NPDate'
 def __init__(self,data,dtype='datetime64[D]'):
  if not isinstance(data,list|tuple|np.ndarray|NPArray|NPDate|Formatconversion):data=[data]
  elif isinstance(data,Formatconversion):data=data.data
  super().__init__(data,serch_dtype(dtype),self.name)
 def __repr__(self):return super().__repr__()
 def astype(self,dtype):
  self.data=self.data.astype(serch_dtype(dtype))
  return self
 @property
 def max(self):return np.max(self.data)
 @property
 def min(self):return np.min(self.data)
 @classmethod
 def arange(cls,start,stop,dtype=None):
  dtype=serch_dtype(dtype)
  sart=conversions(start)
  sop=conversions(stop)
  if sop<sart:sop,sart=sart,sop
  return cls(np.arange(str(sart),str(sop),dtype=dtype),dtype)
 def __add__(self,other):
  if not isinstance(other,np.timedelta64|int):
   raise TypeError('np.timedelta64もしくはint型で指定してください')
  self.data=self.data+other
  return self
 def __sub__(self,other):
  if not isinstance(other,np.timedelta64|int):
   raise TypeError('np.timedelta64もしくはint型で指定してください')
  self.data=self.data-other
  return self
 __radd__=__add__
 __rsub__=__sub__