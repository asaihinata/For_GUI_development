import numpy as np
from ..._arry import Arry
__all__=['complexDtype']
class complexDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.complexfloating)