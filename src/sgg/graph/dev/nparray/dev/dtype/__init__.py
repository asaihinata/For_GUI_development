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
 def __init__(self,arr):
  if not isinstance(arr,np.ndarray):
   raise TypeError('np.ndarray型で指定してください')
  self.arr=arr
  self.dt=arr.dtype
class integerDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.integer)
 def __bool__(self):return self.bool
class intDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.int_)
 def __bool__(self):return self.bool
class uintDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.uint)
 def __bool__(self):return self.bool
class floatDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.floating)
 def __bool__(self):return self.bool
class boolDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.bool_)
 def __bool__(self):return self.bool
class complexDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.complexfloating)
 def __bool__(self):return self.bool
class strDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.str_)
 def __bool__(self):return self.bool
class bytesDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.bytes_)
 def __bool__(self):return self.bool
class datetimeDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.datetime64)
 def __bool__(self):return self.bool
class timedeltaDtype(Arry):
 def __init__(self,arr):super().__init__(arr)
 @property
 def bool(self):return np.issubdtype(self.dt,np.timedelta64)
 def __bool__(self):return self.bool