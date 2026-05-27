'''基本的な計算をするモジュール'''
import numpy as np
from numpy.polynomial import Polynomial
from ..npNumber import NPNumber
__all__=['NPStatistics']
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
 def __repr__(self):return f'{self.data}'
 # x property
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
 def xdeviation(self):return ((10/self.xstd)*(self.x-self.xmean))+50
 @property
 def xlog(self):return np.log(self.x)
 @property
 def xlog10(self):return np.log10(self.x)
 @property
 def xlog2(self):return np.log2(self.x)
 @property
 def xlog1p(self):return np.log1p(self.x)
 @property
 def xdevsq(self):
  xmean=self.xmean
  return np.sum((self.x-xmean)**2)/self.n1
 # y property
 @property
 def ysum(self):return np.sum(self.y)
 @property
 def yave(self):return np.average(self.y)
 @property
 def ymin(self):return np.min(self.y)
 @property
 def ymay(self):return np.max(self.y)
 @property
 def ymean(self):return np.mean(self.y)
 @property
 def yvar(self):return np.var(self.y)
 @property
 def ystd(self):return np.std(self.y)
 @property
 def ypow2(self):return np.power(self.y,2)
 @property
 def ydeviation(self):return ((10/self.ystd)*(self.y-self.ymean))+50
 @property
 def ylog(self):return np.log(self.y)
 @property
 def ylog10(self):return np.log10(self.y)
 @property
 def ylog2(self):return np.log2(self.y)
 @property
 def ylog1p(self):return np.log1p(self.y)
 @property
 def ydevsq(self):
  ymean=self.ymean
  return np.sum((self.y-ymean)**2)/self.n1
 # data
 @property
 def sum(self):return np.sum(self.data)
 @property
 def ave(self):return np.average(self.data)
 @property
 def min(self):return np.min(self.data)
 @property
 def may(self):return np.max(self.data)
 @property
 def mean(self):return np.mean(self.data)
 @property
 def var(self):return np.var(self.data)
 @property
 def std(self):return np.std(self.data)
 @property
 def pow2(self):return np.power(self.data,2)
 @property
 def deviation(self):return ((10/self.std)*(self.data-self.mean))+50
 @property
 def log(self):return np.log(self.data)
 @property
 def log10(self):return np.log10(self.data)
 @property
 def log2(self):return np.log2(self.data)
 @property
 def log1p(self):return np.log1p(self.data)
 @property
 def devsq(self):
  mean=self.mean
  return np.sum((self.data-mean)**2)
 @property
 def n(self):return self.data.shape[1]
 @property
 def n1(self):return self.n-1
 @property
 def CV(self):return self.std/self.ave
 def covariance(self):return np.cov(self.x,self.y)[0,1]
 def correlation(self):return np.corrcoef(self.x,self.y)[0,1]
 def correlation_coefficient(self):return self.Sxy/self.Sxxyyroot
 #x,y
 @property
 def Sxy(self):return np.cov(self.x,self.y)[0,1]
 @property
 def Sxxyy(self):return self.xdevsq*self.ydevsq
 @property
 def Sxxyyroot(self):return np.power(self.Sxxyy,0.5)
 def regression(self,n=1,x=None):
  S=np.polyfit(self.x,self.y,n)
  if isinstance(x,int|float):return np.polyval(S,x)
  return S