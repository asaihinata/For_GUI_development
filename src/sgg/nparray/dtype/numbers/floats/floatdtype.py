import numpy as np
from ...base import baseDtype
__all__=['floatDtype']
class floatDtype(baseDtype):
 @property
 def dtype(self):return[np.float16,np.float32,np.float64,np.floating]
 def __init__(self,arr):super().__init__(arr,self.dtype)