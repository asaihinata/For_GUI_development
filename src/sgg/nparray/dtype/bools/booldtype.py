import numpy as np
from .._arry import Arry
class boolDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.bool_)