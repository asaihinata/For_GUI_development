import numpy as np
from ..base import baseDtype
__all__=['numberDtype']
class numberDtype(baseDtype):
 @property
 def dtype(self):return[np.int8,np.int16,np.int32,np.int64,np.uint8,np.uint16,np.uint32,np.uint64,np.float16,np.float32,np.float64,np.floating,np.complexfloating,np.complex64,np.complex128]
 def __init__(self,arr):super().__init__(arr,self.dtype)