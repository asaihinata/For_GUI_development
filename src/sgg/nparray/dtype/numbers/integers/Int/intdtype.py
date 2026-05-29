import numpy as np
from ....base import baseDtype
__all__=['intDtype']
class intDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,[np.int_,np.int8,np.int16])