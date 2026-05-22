import numpy as np
from ..base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 def __init__(self,data,dtype=None):
  super().__init__(data,dtype)
 def cussum(self):
  datas,shapes=self._flatten()
  splices=shapes[-1]
  self.data=np.array([j+np.insert(j,0,0)[:-1] for i in range(0,len(datas),splices)for j in [datas[i:i+splices]]])
  return self
 def cumprod(self):
  datas,shapes=self._flatten()
  splices=shapes[-1]
  self.data=np.array([j*np.insert(j,0,1)[:-1] for i in range(0,len(datas),splices)for j in [datas[i:i+splices]]])
  return self