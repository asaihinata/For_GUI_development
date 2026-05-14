import numpy as np
__all__=['Array']
class Array:
 def __init__(self,data,*,dtype=None):
  self.dtype=dtype
  self.data=np.array(data,dtype=self.dtype)
 def __iter__(self):return iter(self.data)
 def __array__(self,dtype=None,copy=None):return np.array(self.data,dtype=dtype,copy=copy)
 def tolist(self):return self.data.tolist()
 def sort(self):return np.sort(self.data)