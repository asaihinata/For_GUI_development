import numpy as np
from ....base import baseDtype
__all__=['intDtype']
class intDtype(baseDtype):
 @property
 def dtype(self):return[np.int8,np.int16,np.int32,np.int64]
 def __init__(self,arr):super().__init__(arr,self.dtype)