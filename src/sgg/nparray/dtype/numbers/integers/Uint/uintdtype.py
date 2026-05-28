import numpy as np
from ...._arry import Arry
__all__=['uintDtype']
class uintDtype(Arry):
 def __init__(self,arr):super().__init__(arr,[np.uint,np.uint8,np.uint16,np.uint32,np.uint64])