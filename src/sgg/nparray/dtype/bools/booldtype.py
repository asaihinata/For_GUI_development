import numpy as np
from ..base import baseDtype
__all__=['boolDtype']
class boolDtype(baseDtype):
 @property
 def dtype(self):return[np.bool_]
 def __init__(self,arr):super().__init__(arr,self.dtype)