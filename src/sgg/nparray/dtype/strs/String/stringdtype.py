import numpy as np
from ..._arry import Arry
__all__=['stringDtype']
class stringDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.strings)