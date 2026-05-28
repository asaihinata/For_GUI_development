'''numpyのdtypeに関するモジュール'''
import numpy as np
__all__=['Arry']
class Arry:
 def __init__(self,arr,dtype):
  if not isinstance(arr,np.ndarray):
   raise TypeError('np.ndarray型で指定してください')
  self.arr=arr
  self.dt=arr.dtype
  if isinstance(dtype,list):self.bols=any(np.issubdtype(self.dt,i)for i in dtype)
  else:self.bols=np.issubdtype(self.dt,dtype)
 def __bool__(self):return self.bols
 def __repr__(self):return self.arr
 def __str__(self):return self.arr