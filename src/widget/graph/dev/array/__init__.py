import numpy as np
__all__=['NPArray']
class NPArray:
 def __init__(self,data,*,dtype=None):
  self.dtype=dtype
  self.data=np.array(data,dtype=self.dtype)
 def __iter__(self):return iter(self.data)
 def __array__(self,dtype=None,copy=None):return np.array(self.data,dtype=dtype,copy=copy)
 def tolist(self):return self.data.tolist()
 def sort(self):
  self.data=np.sort(self.data)
  return self
 def first_pop(self):
  if self.data.ndim==1:self.data=np.concatenate((self.data,self.data[0]),axis=0)
  else:self.data=np.concatenate((self.data,[[i[0]]for i in self.data]),axis=1)
  return self
 @property
 def ndim(self):return self.data.ndim
 @property
 def shape(self):return self.data.shape
 @property
 def size(self):return self.data.size
 @property
 def T(self):
  self.data=self.data.T
  return self
 def dimension(self):return True if self.ndim==1 else False
 def dimensions(self):return True if 2<=self.ndim else False
 def _flatten(self):return np.ravel(self.data),self.shape
 def flatten(self):
  self.data=np.ravel(self.data)
  return self
 def cussum(self):
  datas,shapes=self._flatten()
  splices=shapes[-1]
  self.data=np.array([j+np.insert(j,0,0)[:-1] for i in range(0,len(datas),splices)for j in [datas[i:i+splices]]])
  return self
 @classmethod
 def arange(cls,start,stop=None,step=None,dtype=None):
  if stop is None:start,stop=0,start
  cls.data=np.arange(start,stop,step,dtype)
  return cls
 @classmethod
 def linspace(cls,start,stop,num=50,endpoint=True,dtype=None):
  cls.data=np.linspace(start,stop,num=num,endpoint=endpoint,dtype=dtype)
  return cls