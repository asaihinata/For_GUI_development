'''numpyのdtypeに関するモジュール'''
import numpy as np
__all__=['Arry']
class Arry:
 def __init__(self,arr,dtype):
  if not isinstance(arr,np.ndarray):
   raise TypeError('np.ndarray型で指定してください')
  self.arr=arr
  self.dt=arr.dtype
  self._set_dtype=dtype
 def __bool__(self):return np.issubdtype(self.dt,self._set_dtype)