'''基本的な統計の計算をするモジュール'''
import numpy as np
from ..dtype import numberDtype
from ..npNumber import NPNumber
from ._math import *
from .npStatisticsd import NPStatisticsd
__all__=['NPStatisticsds']
method_list=[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen','weibull','linear',
'median_unbiased',
'normal_unbiased'
]
class NPStatisticsds:
 def __dataset(self,arr):
  classname=[i.__name__ for i in arr.__class__.__mro__]
  if 'NPArray' in classname:
   if 'NPNumber' in classname:return arr
   return arr.lengtharange()
  elif isinstance(arr,np.ndarray) and numberDtype(arr):return arr
 def __init__(self,data=None,x=None,y=None):
  if data is None and x is None and y is None:
   raise TypeError('dataもしくはx,yにNPNumberもしくはnp.ndarrayを指定してください')
  elif x is None or y is None:
   data=self.__dataset(data)
   if isinstance(data,NPNumber|np.ndarray):
    if data.ndim!=2:
     raise ValueError('dataには2次元配列で指定してください')
    else:
     self.__data=data.data if isinstance(data,NPNumber) else data
     self.__x,self.__y=self.__data
   else:
    raise TypeError('dataにはNPNumberもしくはnp.ndarrayを指定してください')
  elif x is not None or y is not None:
   x=self.__dataset(x)
   y=self.__dataset(y)
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
   self.__x=x.data if isinstance(x,NPNumber) else x
   self.__y=y.data if isinstance(y,NPNumber) else y
   self.__data=np.vstack((self.__x,self.__y))
  self.__xs=NPStatisticsd(self.__x)
  self.__ys=NPStatisticsd(self.__y)
  self.__datas=NPStatisticsd(self.__data)
 def __repr__(self):return f'NPStatisticsds(\ndata={self.__data},\nx={self.__x},\ny={self.__y})'
 ########
 #  x  #
 ########
 @property
 def x(self):return self.__x
 @property
 def xn(self):return self.__x.size
 @property
 def xsum(self):return self.__xs.sum
 @property
 def xave(self):return self.__xs.ave
 @property
 def xmin(self):return self.__xs.min
 @property
 def xmax(self):return self.__xs.max
 @property
 def xmean(self):return self.__xs.mean
 @property
 def xvar(self):return self.__xs.var
 @property
 def xstd(self):return self.__xs.std
 @property
 def xpow2(self):return self.__xs.pow2
 @property
 def xdeviation(self):return self.__xs.deviation
 @property
 def xlog(self):return self.__xs.log
 @property
 def xlog10(self):return self.__xs.log10
 @property
 def xlog2(self):return self.__xs.log2
 @property
 def xlog1p(self):return self.__xs.log1p
 @property
 def xdevsq(self):return self.__xs.devsq
 @property
 def xrange(self):return self.__xs.range
 @property
 def xskew(self):return self.__xs.skew
 @property
 def xkurtosis(self):return self.__xs.kurtosis
 # 四分位範囲
 def xpercentile(self,q,axis=None,method='linear'):return self.__xs.percentile(q,axis=axis,method=method)
 def xquantile(self,q,axis=None,method='linear'):return self.__xs.quantile(q,axis=axis,method=method)
 # 外れ値
 def xoutlier(self):return self.__xs.outlier()
 def xpopulation(self):return self.__xs.population()
 def xhist_bin_edges(self,bins=10,range=None,weights=None):
  return self.__xs.hist_bin_edges(bins=bins,range=range,weights=weights)
 ########
 #  y  #
 ########
 @property
 def y(self):return self.__y
 @property
 def yn(self):return self.__y.size
 @property
 def ysum(self):return self.__ys.sum
 @property
 def yave(self):return self.__ys.ave
 @property
 def ymin(self):return self.__ys.min
 @property
 def ymax(self):return self.__ys.max
 @property
 def ymean(self):return self.__ys.mean
 @property
 def yvar(self):return self.__ys.var
 @property
 def ystd(self):return self.__ys.std
 @property
 def ypow2(self):return self.__ys.pow2
 @property
 def ydeviation(self):return self.__ys.deviation
 @property
 def ylog(self):return self.__ys.log
 @property
 def ylog10(self):return self.__ys.log10
 @property
 def ylog2(self):return self.__ys.log2
 @property
 def ylog1p(self):return self.__ys.log1p
 @property
 def ydevsq(self):return self.__ys.devsq
 @property
 def yrange(self):return self.__ys.range
 @property
 def yskew(self):return self.__ys.skew
 @property
 def ykurtosis(self):return self.__ys.kurtosis
 # 四分位範囲
 def ypercentile(self,q,axis=None,method='linear'):return self.__ys.percentile(q,axis=axis,method=method)
 def yquantile(self,q,axis=None,method='linear'):return self.__ys.quantile(q,axis=axis,method=method)
 # 外れ値
 def youtlier(self):return self.__ys.outlier()
 def ypopulation(self):return self.__ys.population()
 def yhist_bin_edges(self,bins=10,range=None,weights=None):
  return self.__ys.hist_bin_edges(bins=bins,range=range,weights=weights)
 ##########
 #  data  #
 ##########
 @property
 def data(self):return self.__data
 @property
 def n(self):return self.__data.size
 @property
 def sum(self):return self.__datas.sum
 @property
 def ave(self):return self.__datas.ave
 @property
 def min(self):return self.__datas.min
 @property
 def max(self):return self.__datas.max
 @property
 def mean(self):return self.__datas.mean
 @property
 def var(self):return self.__datas.var
 @property
 def std(self):return self.__datas.std
 @property
 def pow2(self):return self.__datas.pow2
 @property
 def deviation(self):return self.__datas.deviation
 @property
 def log(self):return self.__datas.log
 @property
 def log10(self):return self.__datas.log10
 @property
 def log2(self):return self.__datas.log2
 @property
 def log1p(self):return self.__datas.log1p
 @property
 def devsq(self):return self.__datas.devsq
 @property
 def range(self):return self.__datas.range
 @property
 def skew(self):return self.__datas.skew
 @property
 def kurtosis(self):return self.__datas.kurtosis
 # 四分位範囲
 def percentile(self,q,axis=None,method='linear'):return self.__datas.percentile(q,axis=axis,method=method)
 def quantile(self,q,axis=None,method='linear'):return self.__datas.quantile(q,axis=axis,method=method)
 # 外れ値
 def outlier(self):return self.__datas.outlier()
 def population(self):return self.__datas.population()
 def hist_bin_edges(self,bins=10,range=None,weights=None):
  return self.__datas.hist_bin_edges(bins=bins,range=range,weights=weights)
 @property
 def n(self):return self.__data.shape[1]
 @property
 def n1(self):return self.n-1
 @property
 def CV(self):return self.std/self.ave
 def covariance(self):return np.cov(self.__x,self.__y)[0,1]
 def correlation(self):return np.corrcoef(self.__x,self.__y)[0,1]
 def correlation_coefficient(self):return self.Sxy/self.Sxxyyroot
 # x,y
 @property
 def Sxy(self):return np.cov(self.__x,self.__y)[0,1]
 @property
 def Sxxyy(self):return self.xdevsq*self.ydevsq
 @property
 def Sxxyyroot(self):return np.power(self.Sxxyy,0.5)
 # 回帰直線
 def regression(self,n=1):return mregression(self.__x,self.__y,n)
 def oneregression(self):return mregression(self.__x,self.__y,1)
 def chebysheveve(self,Fx,n=1):return mFregression(self.__x,self.__y,Fx,n)