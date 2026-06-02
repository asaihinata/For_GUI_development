import numpy as np
__all__=['NPArray']
class NPArray:
 def __init__(self,data,dtype=None,depth_limit=None):
  if(
     'NPArray' not in [i.__name__ for i in self.__class__.__mro__] and
     not isinstance(data,list|tuple|np.ndarray|NPArray)
    ):
   raise TypeError('dataには配列の型を指定してください')
  self.dtype=dtype
  self.data=np.array(data,dtype=self.dtype)
  if isinstance(depth_limit,int) and depth_limit<self.data.ndim:
   raise TypeError('配列の深さが制限の深さに達しました')
 def __iter__(self):return iter(self.data)
 def __repr__(self):return f'NPArray({self.data})'
 def __len__(self):return len(self.data)
 def __getitem__(self,key):return self.get(key)
 def __contains__(self,item):return item in self.data
 def __array__(self,dtype=None,copy=None):return np.array(self.data,dtype=dtype,copy=copy)
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPArray) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPArray(result)
   return result
  return NotImplemented
 def _flatten(self):return np.ravel(self.data),self.shape
 def astype(self,dtype):
  self.data=self.data.astype(dtype)
  return self
 def tolist(self):return self.data.tolist()
 def sort(self):
  self.data=np.sort(self.data)
  return self
 def first_pop(self):
  if self.data.ndim==1:self.data=np.concatenate((self.data,self.data[0]),axis=0)
  else:self.data=np.concatenate((self.data,[[i[0]]for i in self.data]),axis=1)
  return self
 def first_element(self):return self.data[0]
 @property
 def nbytes(self):return self.data.nbytes
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
 def lengtharange(self,start=0,dtype=None):
  def aranges(start,size,dtype):return np.arange(start,size,1,dtype=dtype)
  shapes=self.shape
  lens=len(shapes)
  if lens==1:
   return aranges(start,start+self.size,dtype)
  else:
   return np.tile(aranges(start,start+shapes[lens-1],dtype),np.prod(shapes[:-1])).reshape(shapes)
 def flatten(self):
  self.data=np.ravel(self.data)
  return self
 def get(self,val):
  if not isinstance(val,int):
   raise TypeError('valにはint型を指定してください')
  data,size=self.data.flatten(),self.size
  if val==size:return data[val-1]
  elif val<size:return data[val]
  elif size<val:return data[val%size]
 def reshape(self,size):
  self.data=self.data.reshape(size)
  return self
 def clear(self):
  self.data=np.array([],dtype=self.dtype)
  return self
 def all_None(self):return np.all(self.data==None)
 def any_None(self):return np.any(self.data==None)