import numpy as np
from ...base import baseDtype
__all__=['stringDtype']
class stringDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,[np.str_,np.bytes_])