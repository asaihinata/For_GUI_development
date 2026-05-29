import numpy as np
from ...base import baseDtype
__all__=['complexDtype']
class complexDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,np.complexfloating)