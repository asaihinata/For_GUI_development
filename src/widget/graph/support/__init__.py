import numpy as np
__all__=['Conectlist','Datalist','Manylist','Onelist']
class Datalist:
 def __init__(self,data):
  self.data=data
  self.ndim,self.shape=self.data.ndim,self.data.shape
 def T(self):return self.data.T
 def sort(self,axis=1):
  if self.ndim==1:return np.sort(self.data)
  if not(-self.ndim<=axis<=self.ndim):axis=1
  return np.sort(self.data,axis=axis)
 def inversion(self):return self.data[::-1]
class Manylist(Datalist):
 def __init__(self,data=None):
  if not isinstance(data,tuple|list|np.ndarray):
   raise TypeError('dataには配列の型を指定してください')
  if isinstance(data,tuple):self.data=np.array(list(data),dtype=object)
  elif isinstance(data,list):self.data=np.array(data,dtype=object)
  else:self.data=data
  super().__init__(self.data)
 def __iter__(self):return iter(self.data.tolist())
 def __len__(self):return len(self.data)
class Onelist(Datalist):
 def __init__(self,data=None):
  if not isinstance(data,tuple|list|np.ndarray):
   raise TypeError('dataには配列の型を指定してください')
  if isinstance(data,tuple):self.data=np.array(list(data),dtype=object)
  elif isinstance(data,list):self.data=np.array(data,dtype=object)
  else:self.data=data
  if 1<self.data.ndim:
   raise TypeError('一次元の配列を指定してください')
  super().__init__(self.data)
 def __iter__(self):return iter(self.data.tolist())
 def __len__(self):return len(self.data)
class Conectlist(Datalist):
 def __init__(self,data=None):
  if not isinstance(data,tuple|list|np.ndarray):
   raise TypeError('dataには配列の型を指定してください')
  if isinstance(data,tuple):self.data=np.array(list(data),dtype=object)
  elif isinstance(data,list):self.data=np.array(data,dtype=object)
  else:self.data=data
  self.data=np.ravel(self.data)
  super().__init__(self.data)
 def __iter__(self):return iter(self.data.tolist())
 def __len__(self):return len(self.data)