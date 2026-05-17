import numpy as np
from ._data import FMT_COLOR,FMT_MARKER,FMT_SOLID
__all__=['fmtcolor','fmtmarker','fmtsolid']
class fmtcolor:
 def __init__(self,arr:list|tuple|np.ndarray|str)->None:
  if not isinstance(arr,list|tuple|np.ndarray):self.arr=np.array([arr])
  elif isinstance(arr,list|tuple):self.arr=np.array(arr)
  else:self.arr=arr
  self.arr=np.array([i in FMT_COLOR for i in np.nditer(self.arr)]).reshape(self.arr.shape)
 def __iter__(self):return iter(self.arr)
class fmtmarker:
 def __init__(self,arr:list|tuple|np.ndarray|str)->None:
  if not isinstance(arr,list|tuple|np.ndarray):self.arr=np.array([arr])
  elif isinstance(arr,list|tuple):self.arr=np.array(arr)
  else:self.arr=arr
  self.arr=np.array([i in FMT_MARKER for i in np.nditer(self.arr)]).reshape(self.arr.shape)
 def __iter__(self):return iter(self.arr)
class fmtsolid:
 def __init__(self,arr:list|tuple|np.ndarray|str)->None:
  if not isinstance(arr,list|tuple|np.ndarray):self.arr=np.array([arr])
  elif isinstance(arr,list|tuple):self.arr=np.array(arr)
  else:self.arr=arr
  self.arr=np.array([i in FMT_SOLID for i in np.nditer(self.arr)]).reshape(self.arr.shape)
 def __iter__(self):return iter(self.arr)