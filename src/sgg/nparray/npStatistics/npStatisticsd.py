'''基本的な統計の計算をするモジュール'''
import numpy as np
from ..npNumber import NPNumber
from ..dtype import integerDtype
from ._math import *
__all__=['NPStatisticsd']
method_list=[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen','weibull','linear',
'median_unbiased',
'normal_unbiased'
]
class NPStatisticsd:
 def __init__(self,data):
  if isinstance(data,NPNumber|np.ndarray):
   self.__data=data.data if isinstance(data,NPNumber) else data
  else:
   raise TypeError('dataにはNPNumberもしくはnp.ndarrayを指定してください')
 def __repr__(self):return f'NPStatisticsd({self.__data})'
 @property
 def data(self):return self.__data
 @property
 def sum(self):return np.sum(self.__data)
 @property
 def ave(self):return np.average(self.__data)
 @property
 def mean(self):return np.mean(self.__data)
 @property
 def min(self):return np.min(self.__data)
 @property
 def max(self):return np.max(self.__data)
 @property
 def var(self):return np.var(self.__data)
 @property
 def std(self):return np.std(self.__data)
 @property
 def pow2(self):return np.power(self.__data,2)
 @property
 def deviation(self):return mdeviation(self.__data)
 @property
 def log(self):return np.log(self.__data)
 @property
 def log10(self):return np.log10(self.__data)
 @property
 def log2(self):return np.log2(self.__data)
 @property
 def log1p(self):return np.log1p(self.__data)
 @property
 def devsq(self):return mdevsq(self.__data)
 @property
 def range(self):return np.array([self.min,self.max])
 @property
 def skew(self):return np.sum((self.__data-self.ave)**3)/(self.n*np.pow(self.std,3))
 @property
 def kurtosis(self):return np.sum((self.__data-self.ave)**4)/(self.n*np.pow(self.var,2))
 def percentile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.percentile(self.__data,q,axis=axis,method=method)
 def quantile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.quantile(self.__data,q,axis=axis,method=method)
 def IQR(self,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.percentile(self.__data,[25,50,75],axis=axis,method=method)
 def outlier(self):return moutlier(self.__data)
 def population(self):return Population(self.__data)
 @property
 def n(self):return self.__data.shape[1]
 @property
 def n1(self):return self.n-1
 @property
 def CV(self):return self.std/self.ave
 def hist_bin_edges(self,bins=10,range=None,weights=None):
  return np.histogram_bin_edges(self.__data,bins=bins,range=range,weights=weights)