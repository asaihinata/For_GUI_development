import numpy as np
from ...base import baseDtype
__all__=['strDtype']
class strDtype(baseDtype):
 @property
 def dtype(self):return[np.str_]
 def __init__(self,arr):super().__init__(arr,self.dtype)