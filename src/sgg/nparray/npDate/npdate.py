from datetime import datetime
from datetime import timezone as tz
import numpy as np
from ..npArray import NPArray
from .conversion import Formatconversion
from .data import Dtype_SHORT,serch_dtype
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
 def __array__(self,dtype=None,copy=None):return super().__array__(serch_dtype(dtype),copy)
 def __repr__(self):return f'NPDate({self.data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPDate) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPDate(result)
   return result
  return NotImplemented
 @classmethod
 def today(cls,unit=None):
  if unit not in Dtype_SHORT:unit='D'
  return cls([np.datetime64('today',unit)])
 @property
 def T(self):
  self.data=self.data.T
  return self
 def astype(self,dtype):
  self.data=self.data.astype(serch_dtype(dtype))
  return self
 @property
 def max(self):return np.max(self.data)
 @property
 def min(self):return np.min(self.data)
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
 def tostr(self,unit=None,timezone='naive',casting='same_kind'):
  unit=unit if unit in Dtype_SHORT or unit=='auto' else None
  timezone=timezone if timezone in ['naive','UTC','local'] or isinstance(timezone,tz) else 'naive'
  if casting not in ['no','equiv','safe','same_kind','same_value','unsafe']:
   casting='same_kind'
  return np.datetime_as_string(self.data,unit=unit,timezone=timezone,casting=casting)
 def todatetime(self):return self.data.astype('M8[D]').astype(datetime)
 def weekday(self):
  dt=self.todatetime()
  return np.array([i.weekday()for i in dt],dtype=np.uint8)
 def diff_today(self,days=False):
  if not isinstance(days,bool):days=False
  return np.busday_count(self.data,self.today())+int(days)