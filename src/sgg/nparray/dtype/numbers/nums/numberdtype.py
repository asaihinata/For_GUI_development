import numpy as np
from ..._arry import Arry
__all__=['numberDtype']
class numberDtype(Arry):
 def __init__(self,arr):super().__init__(arr,[np.integer,np.floating,np.complexfloating])