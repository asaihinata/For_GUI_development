'''基本的な計算をするモジュール'''
import numpy as np
from ...base import NPArray
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
 def get_axis(self):return self.axis
 def set_axis(self,axis):self.axis=axis
 def __init__(self,data,dtype=np.float32,axis=None):
  if not isinstance(data,list|tuple|np.ndarray|NPArray|NPNumber):data=[data]
  super().__init__(data,dtype)
  self.axis=axis
 def __repr__(self):return f'{self.data}'
 def __abs__(self):
  self.data=np.abs(self.data,dtype=self.dtype)
  return self
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
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,NPNumber) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return NPNumber(result)
   return result
  return NotImplemented
 def __digits(self,digit):
  if not isinstance(digit,int):
   raise TypeError('digitには整数型を指定してください')
  elif digit<1:
   raise ValueError('digitには1以上の整数を指定してください')
  return np.pow(10,digit)
 @property
 def sum(self):return np.sum(self.data,axis=self.axis,dtype=self.dtype)
 @property
 def median(self):return np.median(self.data,axis=self.axis)
 @property
 def var(self):return np.var(self.data,axis=self.axis,dtype=self.dtype)
 @property
 def max(self):return np.max(self.data,axis=self.axis)
 @property
 def min(self):return np.min(self.data,axis=self.axis)
 @property
 def mean(self):return np.mean(self.data,axis=self.axis,dtype=self.dtype)
 @property
 def std(self):return np.std(self.data,axis=self.axis,dtype=self.dtype)
 @property
 def pow2(self):return np.power(self.data,2,dtype=self.dtype)
 @property
 def deviation(self):return ((10/self.std)*(self.data-self.mean))+50
 @property
 def log(self):return np.log(self.data,dtype=self.dtype)
 @property
 def log10(self):return np.log10(self.data,dtype=self.dtype)
 @property
 def log2(self):return np.log2(self.data,dtype=self.dtype)
 @property
 def log1p(self):return np.log1p(self.data,dtype=self.dtype)
 @property
 def degree(self):return np.degrees(self.data,dtype=self.dtype)
 @property
 def radian(self):return np.radians(self.data,dtype=self.dtype)
 def logx(self,x):
  if not isinstance(x,int|float):
   raise TypeError('xには数値の型を指定してください')
  elif x<0:
   raise ValueError('xには0より大きい値を指定してください')
  return np.log(self.data,dtype=self.dtype)/np.log(x,dtype=self.dtype)
 def mod(self,x):return np.mod(self.data,x,dtype=self.dtype)
 def divmod(self,x):return np.divmod(self.data,x,dtype=self.dtype)
 def pow(self,x):
  self.data=np.power(self.data,x,dtype=self.dtype)
  return self
 def sqrt(self,root=2):
  if root==0:
   raise ZeroDivisionError('rootには0を指定できません')
  roots=1/root
  self.data=np.power(self.data,roots,dtype=self.dtype)
  return self
 def floor(self,digit=None):
  if digit==None:self.data=np.floor(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.floor(self.data*pows)/pows
  return self
 def trunc(self,digit=None):
  if digit==None:self.data=np.trunc(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.trunc(self.data*pows)/pows
  return self
 def ceil(self,digit=None):
  if digit==None:self.data=np.ceil(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.ceil(self.data*pows)/pows
  return self
 def round(self,digit=None):
  if digit==None:self.data=np.round(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.round(self.data*pows)/pows
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
 def sturgesval(self,decimal=None,digit=None):
  if decimal not in ['floor','trunc','ceil','round','none']:decimal='none'
  sturges=1+np.log2(self.size)
  if decimal=='floor':
   if digit==None:return np.floor(sturges)
   else:
    pows=self.__digits(digit)
    return np.floor(sturges*pows)/pows
  elif decimal=='trunc':
   if digit==None:return np.trunc(sturges)
   else:
    pows=self.__digits(digit)
    return np.trunc(sturges*pows)/pows
  elif decimal=='ceil':
   if digit==None:return np.ceil(sturges)
   else:
    pows=self.__digits(digit)
    return np.ceil(sturges*pows)/pows
  elif decimal=='round':
   if digit==None:return np.round(sturges)
   else:
    pows=self.__digits(digit)
    return np.round(sturges*pows)/pows
  return sturges
 def ratio(self,axis=None):return(self.data/np.sum(self.data,axis=axis,keepdims=True))*100