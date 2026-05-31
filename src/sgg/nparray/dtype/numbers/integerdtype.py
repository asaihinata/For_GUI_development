import numpy as np
from ..base import baseDtype
__all__=['integerDtype']
class integerDtype(baseDtype):
 @property
 def dtype(self):return[np.int8,np.int16,np.int32,np.int64,np.uint8,np.uint16,np.uint32,np.uint64]
 def __init__(self,arr):super().__init__(arr,np.integer)