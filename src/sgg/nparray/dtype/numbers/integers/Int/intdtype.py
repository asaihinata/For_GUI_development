import numpy as np
from ...._arry import Arry
__all__=['intDtype']
class intDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.int_)