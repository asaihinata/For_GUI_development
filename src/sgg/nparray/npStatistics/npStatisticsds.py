'''基本的な統計の計算をするモジュール'''
import numpy as np
from numpy.polynomial.chebyshev import chebfit,chebval
from ..dtype import numberDtype
from ..npNumber import NPNumber
from .npStatisticsd import NPStatisticsd
__all__=['NPStatisticsds']
method_list=[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen','weibull','linear',
'median_unbiased',
'normal_unbiased']
class NPStatisticsds:
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
 @property
 def x(self):return self.__x
 @property
 def y(self):return self.__y
 @property
 def data(self):return self.__data
 @property
 def xmath(self):return self.__xs
 @property
 def ymath(self):return self.__ys
 @property
 def mathes(self):return self.__datas
 def covariance(self):return np.cov(self.__x,self.__y)[0,1]
 def correlation(self):return np.corrcoef(self.__x,self.__y)[0,1]
 def correlation_coefficient(self):return self.Sxy/self.Sxxyyroot
 # x,y
 @property
 def Sxy(self):return np.cov(self.__x,self.__y)[0,1]
 @property
 def Sxxyy(self):return self.__xs.devsq*self.__ys.devsq
 @property
 def Sxxyyroot(self):return np.power(self.Sxxyy,0.5)
 # 回帰直線
 def regression(self,n=1):return chebfit(self.__x,self.__y,n)
 def oneregression(self):return chebfit(self.__x,self.__y,1)
 def chebysheveve(self,Fx,n=1):return chebval(Fx,chebfit(self.__x,self.__y,n))
 def __dataset(self,arr):
  classname=[i.__name__ for i in arr.__class__.__mro__]
  if 'NPArray' in classname:
   if 'NPNumber' in classname:return arr
   return arr.lengtharange()
  elif isinstance(arr,np.ndarray) and numberDtype(arr):return arr