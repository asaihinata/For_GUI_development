import numpy as np
from ...base import baseDtype
__all__=['stringDtype']
class stringDtype(baseDtype):
 @property
 def dtype(self):return[np.str_,np.bytes_]
 def __init__(self,arr):super().__init__(arr,self.dtype)