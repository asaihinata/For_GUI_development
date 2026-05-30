import numpy as np
from ...base import baseDtype
__all__=['datetimeDtype']
class datetimeDtype(baseDtype):
 @property
 def dtype(self):return[np.datetime64]
 def __init__(self,arr):super().__init__(arr,self.dtype)