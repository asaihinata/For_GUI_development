import numpy as np
from .datalist import Datalist
class Onelist(Datalist):
 def __init__(self,data,dtype=None):
  if not isinstance(data,tuple|list|np.ndarray):
   raise TypeError('dataには配列の型を指定してください')
  if isinstance(data,tuple|list):self.data=np.array(data,dtype=dtype)
  else:self.data=data.astype(dtype)
  if 1<self.data.ndim:
   raise TypeError('一次元の配列を指定してください')
  super().__init__(self.data)