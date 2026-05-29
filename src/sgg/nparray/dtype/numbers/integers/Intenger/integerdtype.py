import numpy as np
from ....base import baseDtype
__all__=['integerDtype']
class integerDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,np.integer)