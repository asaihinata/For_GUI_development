import numpy as np
from ..._arry import Arry
class timedeltaDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.timedelta64)