import numpy as np
from ..base import baseDtype
__all__=['timedeltaDtype']
class timedeltaDtype(baseDtype):
 @property
 def dtype(self):return[np.timedelta64]
 def __init__(self,arr):super().__init__(arr,self.dtype)