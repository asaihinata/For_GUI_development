import numpy as np
from ...base import baseDtype
__all__=['bytesDtype']
class bytesDtype(baseDtype):
 @property
 def dtype(self):return[np.bytes_]
 def __init__(self,arr):super().__init__(arr,self.dtype)