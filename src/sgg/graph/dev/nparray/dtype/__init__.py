'''numpyのdtypeに関するモジュール'''
import numpy as np
__all__=[
'boolDtype',
'bytesDtype',
'complexDtype',
'datetimeDtype',
'floatDtype',
'intDtype',
'integerDtype',
'strDtype',
'timedeltaDtype',
'uintDtype'
]
class Arry:
 def __init__(self,arr,dtype):
  if not isinstance(arr,np.ndarray):
   raise TypeError('np.ndarray型で指定してください')
  self.arr=arr
  self.dt=arr.dtype
  self._set_dtype=dtype
 def __bool__(self):return np.issubdtype(self.dt,self._set_dtype)
class integerDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.integer)
class intDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.int_)
class uintDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.uint)
class floatDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.floating)
class boolDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.bool_)
class complexDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.complexfloating)
class strDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.str_)
class bytesDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.bytes_)
class datetimeDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.datetime64)
class timedeltaDtype(Arry):
 def __init__(self,arr):super().__init__(arr,np.timedelta64)