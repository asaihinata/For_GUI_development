import numpy as np
from ..base import NPArray
__all__=['NPNumber']
method_list=[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen',
'weibull',
'linear',
'median_unbiased',
'normal_unbiased'
]
class NPNumber(NPArray):
 def __init__(self,data,dtype=None):
  if not isinstance(data,list|tuple|np.ndarray|NPArray|NPNumber):data=[data]
  super().__init__(data,dtype)
 def __add__(self,other):
  if isinstance(other,NPNumber):self.data=self.data+other.data
  else:self.data=self.data+other
  return self
 def __sub__(self,other):
  if isinstance(other,NPNumber):self.data=self.data-other.data
  else:self.data=self.data-other
  return self
 def __mul__(self,other):
  if isinstance(other,NPNumber):self.data=self.data*other.data
  else:self.data=self.data*other
  return self
 def __truediv__(self,other):
  if isinstance(other,NPNumber):self.data=self.data/other.data
  else:self.data=self.data/other
  return self
 __radd__=__add__
 __rsub__=__sub__
 __rmul__=__mul__
 __rtruediv__=__truediv__
 def __mod__(self,other):
  if isinstance(other,NPNumber):self.data=self.data%other.data
  else:self.data=self.data%other
  return self
 def __floordiv__(self,other):
  if isinstance(other,NPNumber):self.data=self.data//other.data
  else:self.data=self.data//other
  return self
 def __pow__(self,other):
  if isinstance(other,NPNumber):self.data=np.power(self.data,other.data)
  else:self.data=np.power(self.data,other)
  return self
 def __repr__(self):return f'NPNumber({self.data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPNumber) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPNumber(result)
   return result
  return NotImplemented
 @property
 def sum(self):return np.sum(self.data)
 @property
 def median(self):return np.median(self.data)
 @property
 def var(self):return np.var(self.data)
 @property
 def max(self):return np.max(self.data)
 @property
 def min(self):return np.min(self.data)
 @property
 def mean(self):return np.mean(self.data)
 @property
 def std(self):return np.std(self.data)
 @property
 def pow2(self):return np.power(self.data,2)
 def asum(self,axis=None,dtype=None):return np.sum(self.data,axis=axis,dtype=dtype)
 def amedian(self,axis=None):return np.median(self.data,axis=axis)
 def avar(self,axis=None,dtype=None):return np.var(self.data,axis=axis,dtype=dtype)
 def amax(self,axis=None):return np.amax(self.data,axis=axis)
 def amin(self,axis=None):return np.amin(self.data,axis=axis)
 def amean(self,axis=None,dtype=None):return np.mean(self.data,axis=axis,dtype=dtype)
 def astd(self,axis=None,dtype=None):return np.std(self.data,axis=axis,dtype=dtype)
 def amod(self,x):return np.mod(self.data,x)
 def adivmod(self,x):return np.divmod(self.data,x)
 def apow(self,x):return np.power(self.data,x)
 def apow2(self):return np.power(self.data,2)
 def pow(self,x):
  self.data=np.power(self.data,x)
  return self
 def cussum(self):
  datas,shapes=self._flatten()
  splices=shapes[-1]
  self.data=np.array([j+np.insert(j,0,0)[:-1] for i in range(0,len(datas),splices)for j in [datas[i:i+splices]]])
  return self
 def cumprod(self):
  datas,shapes=self._flatten()
  splices=shapes[-1]
  self.data=np.array([j*np.insert(j,0,1)[:-1] for i in range(0,len(datas),splices)for j in [datas[i:i+splices]]])
  return self
 def percentile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.percentile(self.data,q,axis=axis,method=method)
 def quantile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.quantile(self.data,q,axis=axis,method=method)