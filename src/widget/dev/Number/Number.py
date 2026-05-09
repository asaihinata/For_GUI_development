from math import ceil,floor
from sys import getsizeof
import numpy as np
__all__=['Number']
class Number:
 def __init__(self,val):
  if not isinstance(val,bool|float|int|Number|np.float16|np.float32|np.float64|np.int16|np.int32|np.int64|np.int8|np.uint16|np.uint32|np.uint64|np.uint8):
   raise TypeError('valに数値を指定してください')
  if isinstance(val,Number):self.val=val.val
  elif isinstance(val,bool):self.val=int(val)
  else:self.val=val
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,Number)
 def __getattribute__(self,name):return super().__getattribute__(name)
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.val)
 def __int__(self):return int(self.val)
 def __float__(self):return float(self.val)
 def __str__(self):return str(self.val)
 def __len__(self):return len(str(self.val))
 def len(self):return len(str(self.val))
 def __bool__(self):
  if 0<=self.val:return True
  return False
 def __format__(self,format_spec):return format(self.val,format_spec)
 def format(self,format_spec):return format(self.val,format_spec)
 def types(self):return type(self.val)
 def __add__(self,val):
  self.val=self.val+self._maths_(val)
  return self
 def __sub__(self,val):
  self.val=self.val-self._maths_(val)
  return self
 def __mul__(self,val):
  self.val=self.val*self._maths_(val)
  return self
 def __pow__(self,val):
  self.val=self.val**self._maths_(val)
  return self
 def __ipow__(self,val):
  self.val**=self._maths_(val)
  return self
 def __truediv__(self,val):
  self.val=self.val/self._maths_(val)
  return self
 def __floordiv__(self,val):
  self.val=self.val//self._maths_(val)
  return self
 def __radd__(self,val):
  self.val=self._maths_(val)+self.val
  return self
 def __rsub__(self,val):
  self.val=self._maths_(val)-self.val
  return self
 def __rmul__(self,val):
  self.val=self._maths_(val)*self.val
  return self
 def __rtruediv__(self,val):
  self.val=self._maths_(val)/self.val
  return self
 def __rmod__(self,val):
  self.val=self._maths_(val)%self.val
  return self
 def __rpow__(self,val):
  self.val=self._maths_(val)**self.val
  return self
 def __rfloordiv__(self,val):
  self.val=self._maths_(val)//self.val
  return self
 def __iadd__(self,val):
  self.val+=self._maths_(val)
  return self
 def __isub__(self,val):
  self.val-=self._maths_(val)
  return self
 def __imul__(self,val):
  self.val*=self._maths_(val)
  return self
 def __itruediv__(self,val):
  self.val/=self._maths_(val)
  return self
 def __abs__(self):
  if self.val<0:self.val=abs(self.val)
  return self
 def __eq__(self,val):return self.val==(val.val if isinstance(val,Number) else val)
 def __ne__(self,val):return self.val!=(val.val if isinstance(val,Number) else val)
 def __lt__(self,val):return self.val<self._maths_(val)
 def __le__(self,val):return self.val<=self._maths_(val)
 def __gt__(self,val):return self.val>self._maths_(val)
 def __ge__(self,val):return self.val>=self._maths_(val)
 def __round__(self,n=0):
  self.val=round(self.val,self._maths_(n))
  return self
 def __ceil__(self):
  self.val=ceil(self.val)
  return self
 def __floor__(self):
  self.val=floor(self.val)
  return self
 def __neg__(self):
  self.val=-self.val
  return self
 def __pos__(self):return self
 def _maths_(self,val):
  if isinstance(val,Number):return val.val
  elif isinstance(val,int|float):return val
  raise TypeError('数値の型を指定してください')
 def value(self):return self.val