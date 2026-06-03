'''グラフで使用する配列を作成するモジュール'''
import numpy as np
from ..base import NPArray
__all__=['NPGraph']
class NPGraph(NPArray):
 def __init__(self,data,dtype=None,depth_limit=None):
  super().__init__(data,dtype,depth_limit)
  self.serial_num=self.lengtharange()
 def __iter__(self):return super().__iter__()
 def __len__(self):return super().__len__()
 def __getitem__(self,key):return super().__getitem__(key)
 def __contains__(self,item):return super().__contains__(item)
 def __reversed__(self):return super().__reversed__()
 def __array__(self,dtype=None,copy=None):return super().__array__(dtype,copy)
 def __repr__(self):return f'NPGraph(\ndata={self.data},\nserial={self.serial_num}\n)'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPGraph) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPGraph(result)
   return result
  return NotImplemented
 @property
 def T(self):
  self.data=self.data.T
  return self
 @property
 def serial(self):return self.serial_num
 def gets(self):return self.data,self.serial_num