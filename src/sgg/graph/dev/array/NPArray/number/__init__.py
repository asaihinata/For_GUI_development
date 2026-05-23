import numpy as np
from ..base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 def __init__(self,data,dtype=None):
  super().__init__(data,dtype)
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
 @property
 def sum(self):return np.sum(self.data)
 def asum(self,axis=None,dtype=None):return np.sum(self.data,axis=axis,dtype=dtype)
 @property
 def median(self):return np.median(self.data)
 def amedian(self,axis=None):return np.median(self.data,axis=axis)
 @property
 def var(self):return np.var(self.data)
 def avar(self,axis=None,dtype=None):return np.var(self.data,axis=axis,dtype=dtype)
 @property
 def max(self):return np.max(self.data)
 def amax(self,axis=None):return np.amax(self.data,axis=axis)
 @property
 def min(self):return np.min(self.data)
 def amin(self,axis=None):return np.amin(self.data,axis=axis)
 @property
 def mean(self):return np.mean(self.data)
 def amean(self,axis=None,dtype=None):return np.mean(self.data,axis=axis,dtype=dtype)
 @property
 def std(self):return np.std(self.data)
 def astd(self,axis=None,dtype=None):return np.std(self.data,axis=axis,dtype=dtype)
 def percentile(self,q,axis=None,method='linear'):
  if method not in [
   'inverted_cdf',
   'averaged_inverted_cdf',
   'closest_observation',
   'interpolated_inverted_cdf',
   'hazen',
   'weibull',
   'linear',
   'median_unbiased',
   'normal_unbiased'
  ]:
   method='linear'
  return np.percentile(self.data,q,axis=axis,method=method)
 def quantile(self,q,axis=None,method='linear'):
  if method not in [
   'inverted_cdf',
   'averaged_inverted_cdf',
   'closest_observation',
   'interpolated_inverted_cdf',
   'hazen',
   'weibull',
   'linear',
   'median_unbiased',
   'normal_unbiased'
  ]:
   method='linear'
  return np.quantile(self.data,q,axis=axis,method=method)