import numpy as np
from ..._arry import Arry
__all__=['strDtype']
class strDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.str_)