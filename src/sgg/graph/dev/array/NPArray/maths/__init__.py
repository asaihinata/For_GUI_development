'''基本的な計算をするモジュール'''
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
 def get_axis(self):return self.axis
 def set_axis(self,axis):self.axis=axis
 def __init__(self,data,dtype=None,axis=None):
  if not isinstance(data,list|tuple|np.ndarray|NPArray|NPNumber):data=[data]
  super().__init__(data,dtype)
  self.axis=axis
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
 def __repr__(self):return f'NPNumber({self.data})'
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
 def floor(self,digit=None):
  if digit==None:
   self.data=np.floor(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.floor(self.data*pows)/pows
  return self
 def trunc(self,digit=None):
  if digit==None:
   self.data=np.trunc(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.trunc(self.data*pows)/pows
  return self
 def ceil(self,digit=None):
  if digit==None:
   self.data=np.ceil(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.ceil(self.data*pows)/pows
  return self
 def round(self,digit=None):
  if digit==None:
   self.data=np.round(self.data)
  else:
   pows=self.__digits(digit)
   self.data=np.round(self.data*pows)/pows
  return self
 def afloor(self,digit=None):
  if digit==None:return np.floor(self.data)
  else:
   pows=self.__digits(digit)
   return np.floor(self.data*pows)/pows
 def atrunc(self,digit=None):
  if digit==None:return np.trunc(self.data)
  else:
   pows=self.__digits(digit)
   return np.trunc(self.data*pows)/pows
 def aceil(self,digit=None):
  if digit==None:return np.ceil(self.data)
  else:
   pows=self.__digits(digit)
   return np.ceil(self.data*pows)/pows
 def around(self,digit=None):
  if digit==None:return np.round(self.data)
  else:
   pows=self.__digits(digit)
   return np.round(self.data*pows)/pows
 def asum(self,axis=None,dtype=None):return np.sum(self.data,axis=axis,dtype=dtype)
 def amedian(self,axis=None):return np.median(self.data,axis=axis)
 def avar(self,axis=None,dtype=None):return np.var(self.data,axis=axis,dtype=dtype)
 def amax(self,axis=None):return np.amax(self.data,axis=axis)
 def amin(self,axis=None):return np.amin(self.data,axis=axis)
 def amean(self,axis=None,dtype=None):return np.mean(self.data,axis=axis,dtype=dtype)
 def astd(self,axis=None,dtype=None):return np.std(self.data,axis=axis,dtype=dtype)
 def amod(self,x):return np.mod(self.data,x,dtype=self.dtype)
 def adivmod(self,x):return np.divmod(self.data,x,dtype=self.dtype)
 def apow(self,x):return np.power(self.data,x,dtype=self.dtype)
 def apow2(self):return np.power(self.data,2,dtype=self.dtype)
 def alog(self):return np.log(self.data,dtype=self.dtype)
 def alogx(self,x):
  if not isinstance(x,int|float):
   raise TypeError('xには数値の型を指定してください')
  elif x<0:
   raise ValueError('xには0より大きい値を指定してください')
  return np.log(self.data,dtype=self.dtype)/np.log(x,dtype=self.dtype)
 def alog10(self):return np.log10(self.data,dtype=self.dtype)
 def alog2(self):return np.log2(self.data,dtype=self.dtype)
 def alog1p(self):return np.log1p(self.data,dtype=self.dtype)
 def pow(self,x):
  self.data=np.power(self.data,x,dtype=self.dtype)
  return self
 def sqrtroot(self,root):
  roots=1/root
  self.data=np.power(self.data,roots,dtype=self.dtype)
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
  def floor(data,digit=None):
   if digit==None:return np.floor(data)
   else:
    pows=self.__digits(digit)
    return np.floor(data*pows)/pows
  def trunc(data,digit=None):
   if digit==None:return np.trunc(data)
   else:
    pows=self.__digits(digit)
    return np.trunc(data*pows)/pows
  def ceil(data,digit=None):
   if digit==None:return np.ceil(data)
   else:
    pows=self.__digits(digit)
    return np.ceil(data*pows)/pows
  def round(data,digit=None):
   if digit==None:return np.round(data)
   else:
    pows=self.__digits(digit)
    return np.round(data*pows)/pows
  if decimal not in ['floor','trunc','ceil','round','none']:decimal='none'
  sturges=1+np.log2(self.size)
  if decimal=='floor':return floor(sturges,digit)
  elif decimal=='trunc':return trunc(sturges,digit)
  elif decimal=='ceil':return ceil(sturges,digit)
  elif decimal=='round':return round(sturges,digit)
  return sturges