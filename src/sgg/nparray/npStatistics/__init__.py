'''基本的な統計の計算をするモジュール'''
import numpy as np
from ..npNumber import NPNumber
from ._math import *
__all__=['NPStatistics']
method_list=[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen','weibull','linear',
'median_unbiased',
'normal_unbiased'
]
class NPStatistics:
 def __init__(self,data=None,x=None,y=None):
  if data is None and x is None and y is None:
   raise TypeError('dataもしくはx,yにNPNumberもしくはnp.ndarrayを指定してください')
  elif x is None or y is None:
   if isinstance(data,NPNumber|np.ndarray):
    if data.ndim!=2:
     raise ValueError('dataには2次元配列で指定してください')
    else:
     self.data=np.array(data) if isinstance(data,NPNumber) else data
     self.x,self.y=self.data
   else:
    raise TypeError('dataにはNPNumberもしくはnp.ndarrayを指定してください')
  elif x is not None or y is not None:
   if isinstance(x,NPNumber|np.ndarray):
    if x.ndim!=1:
     raise ValueError('xには1次元配列で指定してください')
   else:
    raise TypeError('xにはNPNumberもしくはnp.ndarrayを指定してください')
   if isinstance(y,NPNumber|np.ndarray):
    if y.ndim!=1:
     raise ValueError('yには1次元配列で指定してください')
   else:
    raise TypeError('yにはNPNumberもしくはnp.ndarrayを指定してください')
   self.x=np.array(x) if isinstance(x,NPNumber) else x
   self.y=np.array(y) if isinstance(y,NPNumber) else y
   self.data=np.vstack((self.x,self.y))
 def __repr__(self):return f'NPStatistics({self.data})'
 ########
 #  x  #
 ########
 @property
 def xn(self):return self.x.size
 @property
 def xsum(self):return np.sum(self.x)
 @property
 def xave(self):return np.average(self.x)
 @property
 def xmin(self):return np.min(self.x)
 @property
 def xmax(self):return np.max(self.x)
 @property
 def xmean(self):return np.mean(self.x)
 @property
 def xvar(self):return np.var(self.x)
 @property
 def xstd(self):return np.std(self.x)
 @property
 def xpow2(self):return np.power(self.x,2)
 @property
 def xdeviation(self):return mdeviation(self.x)
 @property
 def xlog(self):return np.log(self.x)
 @property
 def xlog10(self):return np.log10(self.x)
 @property
 def xlog2(self):return np.log2(self.x)
 @property
 def xlog1p(self):return np.log1p(self.x)
 @property
 def xdevsq(self):return mdevsq(self.x)
 @property
 def xrange(self):return np.array([self.xmin,self.xmax])
 @property
 def xskew(self):return np.sum((self.x-self.xave)**3)/(self.xn*np.pow(self.xstd,3))
 @property
 def xkurtosis(self):return np.sum((self.x-self.xave)**4)/(self.xn*np.pow(self.xvar,2))
 # 四分位範囲
 def xpercentile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.percentile(self.x,q,axis=axis,method=method)
 def xquantile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.quantile(self.x,q,axis=axis,method=method)
 # 外れ値
 def xoutlier(self):return moutlier(self.x)
 def xpopulation(self):return Population(self.x)
 ########
 #  y  #
 ########
 @property
 def yn(self):return self.y.size
 @property
 def ysum(self):return np.sum(self.y)
 @property
 def yave(self):return np.average(self.y)
 @property
 def ymin(self):return np.min(self.y)
 @property
 def ymax(self):return np.max(self.y)
 @property
 def ymean(self):return np.mean(self.y)
 @property
 def yvar(self):return np.var(self.y)
 @property
 def ystd(self):return np.std(self.y)
 @property
 def ypow2(self):return np.power(self.y,2)
 @property
 def ydeviation(self):return mdeviation(self.y)
 @property
 def ylog(self):return np.log(self.y)
 @property
 def ylog10(self):return np.log10(self.y)
 @property
 def ylog2(self):return np.log2(self.y)
 @property
 def ylog1p(self):return np.log1p(self.y)
 @property
 def ydevsq(self):return mdevsq(self.y)
 @property
 def yrange(self):return np.array([self.ymin,self.ymax])
 @property
 def yskew(self):return np.sum((self.y-self.yave)**3)/(self.yn*np.pow(self.ystd,3))
 @property
 def ykurtosis(self):return np.sum((self.y-self.yave)**4)/(self.yn*np.pow(self.yvar,2))
 def ypercentile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.percentile(self.y,q,axis=axis,method=method)
 def yquantile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.quantile(self.y,q,axis=axis,method=method)
 def youtlier(self):return moutlier(self.y)
 def ypopulation(self):return Population(self.y)
 ##########
 #  data  #
 ##########
 @property
 def sum(self):return np.sum(self.data)
 @property
 def ave(self):return np.average(self.data)
 @property
 def min(self):return np.min(self.data)
 @property
 def max(self):return np.max(self.data)
 @property
 def mean(self):return np.mean(self.data)
 @property
 def var(self):return np.var(self.data)
 @property
 def std(self):return np.std(self.data)
 @property
 def pow2(self):return np.power(self.data,2)
 @property
 def deviation(self):return mdeviation(self.data)
 @property
 def log(self):return np.log(self.data)
 @property
 def log10(self):return np.log10(self.data)
 @property
 def log2(self):return np.log2(self.data)
 @property
 def log1p(self):return np.log1p(self.data)
 @property
 def devsq(self):return mdevsq(self.data)
 @property
 def range(self):return np.array([[self.xmin,self.xmax],[self.ymin,self.ymax]])
 @property
 def skew(self):return np.sum((self.data-self.ave)**3)/(self.n*np.pow(self.std,3))
 @property
 def kurtosis(self):return np.sum((self.data-self.ave)**4)/(self.n*np.pow(self.var,2))
 def percentile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.percentile(self.data,q,axis=axis,method=method)
 def quantile(self,q,axis=None,method='linear'):
  if method not in method_list:method='linear'
  return np.quantile(self.data,q,axis=axis,method=method)
 def outlier(self):return moutlier(self.data)
 def population(self):return Population(self.data)
 @property
 def n(self):return self.data.shape[1]
 @property
 def n1(self):return self.n-1
 @property
 def CV(self):return self.std/self.ave
 def covariance(self):return np.cov(self.x,self.y)[0,1]
 def correlation(self):return np.corrcoef(self.x,self.y)[0,1]
 def correlation_coefficient(self):return self.Sxy/self.Sxxyyroot
 # x,y
 @property
 def Sxy(self):return np.cov(self.x,self.y)[0,1]
 @property
 def Sxxyy(self):return self.xdevsq*self.ydevsq
 @property
 def Sxxyyroot(self):return np.power(self.Sxxyy,0.5)
 # 回帰直線
 def regression(self,n=1):return mregression(self.x,self.y,n)