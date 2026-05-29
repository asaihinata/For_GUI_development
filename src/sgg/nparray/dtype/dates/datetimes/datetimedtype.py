import numpy as np
from ...base import baseDtype
__all__=['datetimeDtype']
class datetimeDtype(baseDtype):
 def __init__(self,arr):super().__init__(arr,np.datetime64)