'''numpyのdtypeに関するモジュール'''
import numpy as np
__all__=['baseDtype']
class baseDtype:
 def __init__(self,arr,dtype):
  if isinstance(arr,np.ndarray):self.dt=arr.dtype
  else:self.dt=arr
  if isinstance(dtype,list):self.bols=any(np.issubdtype(self.dt,i)for i in dtype)
  else:self.bols=np.issubdtype(self.dt,dtype)
 def __bool__(self):return self.bols