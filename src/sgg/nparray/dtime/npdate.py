import numpy as np
from ..base import NPArray
from .conversion import Formatconversion,conversions
from .data import serch_dtype
__all__=['NPDate']
class NPDate(NPArray):
 def __init__(self,data,dtype='datetime64[D]',depth_limit=None):
  if isinstance(data,Formatconversion):data=data.data
  super().__init__(data,serch_dtype(dtype),depth_limit)
 def __iter__(self):return super().__iter__()
 def __len__(self):return super().__len__()
 def __getitem__(self,key):return super().__getitem__(key)
 def __contains__(self,item):return super().__contains__(item)
 def __reversed__(self):return super().__reversed__()
 def __array__(self,dtype=None,copy=None):return super().__array__(dtype,copy)
 def __repr__(self):return f'NPDate({self.__data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPDate) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPDate(result)
   return result
  return NotImplemented
 @property
 def T(self):
  self.__data=self.__data.T
  return self
 def astype(self,dtype):
  self.__data=self.__data.astype(serch_dtype(dtype))
  return self
 @property
 def max(self):return np.max(self.__data)
 @property
 def min(self):return np.min(self.__data)
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
  self.__data=self.__data+other
  return self
 def __sub__(self,other):
  if not isinstance(other,np.timedelta64|int):
   raise TypeError('np.timedelta64もしくはint型で指定してください')
  self.__data=self.__data-other
  return self
 __radd__=__add__
 __rsub__=__sub__