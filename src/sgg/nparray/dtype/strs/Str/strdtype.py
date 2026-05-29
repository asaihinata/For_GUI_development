import numpy as np
from ...base import baseDtype
__all__=['strDtype']
class strDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,np.str_)