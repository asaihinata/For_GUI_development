import numpy as np
__all__=['NPArray']
class NPArray:
 def __init__(self,data,dtype=None,depth_limit=None):
  self.__dtype=dtype
  if(
     'NPArray' not in [i.__name__ for i in self.__class__.__mro__] and
     not isinstance(data,list|tuple|np.ndarray|NPArray)
    ):
   raise TypeError('dataには配列の型を指定してください')
  self.__data=np.array(data,dtype=self.__dtype)
  if isinstance(depth_limit,int) and depth_limit<self.__data.ndim:
   raise TypeError('配列の深さが制限の深さに達しました')
 # 親クラス,子クラス共通の特殊メソッド
 def __iter__(self):
  if self.ndim==1:return iter([self.__data])
  return iter(self.__data)
 def __len__(self):return len(self.__data)
 def __getitem__(self,key):return self.get(key)
 def __contains__(self,item):return item in self.__data
 def __reversed__(self):
  self.__data=np.flip(self.__data)
  return self
 def __array__(self,dtype=None,copy=None):return np.array(self.__data,dtype=dtype,copy=copy)
 # 以下の特殊メソッドはそれぞれの子クラス毎に処理を変更する必要がある
 def __repr__(self):return f'NPArray({self.__data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPArray) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPArray(result)
   return result
  return NotImplemented
 def _flatten(self):return np.ravel(self.__data),self.shape
 def astype(self,dtype):
  self.__data=self.__data.astype(dtype)
  return self
 def tolist(self):return self.__data.tolist()
 def tonp(self,dtype='none'):
  if dtype=='none':return self.__data
  return self.__data.astype(dtype)
 def sort(self):
  self.__data=np.sort(self.__data)
  return self
 def first_pop(self):
  if self.__data.ndim==1:self.__data=np.concatenate((self.__data,self.__data[0]),axis=0)
  else:self.__data=np.concatenate((self.__data,[[i[0]]for i in self.__data]),axis=1)
  return self
 def first_element(self):return self.__data[0]
 @property
 def nbytes(self):return self.__data.nbytes
 @property
 def ndim(self):return self.__data.ndim
 @property
 def shape(self):return self.__data.shape
 @property
 def size(self):return self.__data.size
 @property
 def T(self):
  self.__data=self.__data.T
  return self
 @property
 def dtype(self):return self.__dtype
 @property
 def data(self):return self.__data
 @data.setter
 def data(self,data):
  if(
     'NPArray' not in [i.__name__ for i in self.__class__.__mro__] and
     not isinstance(data,list|tuple|np.ndarray|NPArray)
    ):
   raise TypeError('dataには配列の型を指定してください')
  self.__data=np.array(data,dtype=self.__dtype)
  return self.__data
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
  self.__data=np.ravel(self.__data)
  return self
 def reshape(self,size):
  self.__data=self.__data.reshape(size)
  return self
 def deep_add(self,val):
  if not isinstance(val,int):
   raise TypeError('valにはint型を指定してください')
  elif val<=0:
   raise ValueError('valには1以上の整数を指定してください')
  for _ in range(val):self.__data=np.expand_dims(self.__data,axis=0)
  return self
 def min_deep(self,val):
  if not isinstance(val,int):
   raise TypeError('valにはint型を指定してください')
  elif val<=0:
   raise ValueError('valには1以上の整数を指定してください')
  if self.ndim<val:
   for _ in range(val-self.ndim):self.__data=np.expand_dims(self.__data,axis=0)
  return self
 def get(self,val):
  if not isinstance(val,int):
   raise TypeError('valにはint型を指定してください')
  data,size=self.__data.flatten(),self.size
  if val==size:return data[val-1]
  elif val<size:return data[val]
  elif size<val:return data[val%size]
 def clear(self):
  self.__data=np.array([],dtype=self.__dtype)
  return self
 def all_None(self):return np.all(self.__data==None)
 def any_None(self):return np.any(self.__data==None)