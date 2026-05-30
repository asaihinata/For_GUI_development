import numpy as np
from ...base import baseDtype
__all__=['complexDtype']
class complexDtype(baseDtype):
 @property
 def dtype(self):return[np.complexfloating,np.complex64,np.complex128]
 def __init__(self,arr):super().__init__(arr,self.dtype)