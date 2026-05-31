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
 def __iter__(self):return iter(self.dtype)
 @property
 def dtype(self):return[np.datetime64,np.timedelta64,np.bool_,np.int8,np.int16,np.int32,np.int64,np.uint8,np.uint16,np.uint32,np.uint64,np.float16,np.float32,np.float64,np.floating,np.complexfloating,np.complex64,np.complex128,np.str_,np.bytes_]