import numpy as np
from ....base import baseDtype
__all__=['uintDtype']
class uintDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,[np.uint,np.uint8,np.uint16,np.uint32,np.uint64])