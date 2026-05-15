import numpy as np
from .Datalist import Datalist
class Manylist(Datalist):
 def __init__(self,data,dtype=None):
  if not isinstance(data,tuple|list|np.ndarray):
   raise TypeError('dataには配列の型を指定してください')
  if isinstance(data,tuple|list):self.data=np.array(data,dtype=dtype)
  else:self.data=data.astype(dtype)
  super().__init__(self.data)