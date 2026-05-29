import numpy as np
from ...base import baseDtype
__all__=['bytesDtype']
class bytesDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,np.bytes_)