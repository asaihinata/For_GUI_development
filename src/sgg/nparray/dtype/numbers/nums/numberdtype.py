import numpy as np
from ...base import baseDtype
__all__=['numberDtype']
class numberDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,[np.integer,np.floating,np.complexfloating])