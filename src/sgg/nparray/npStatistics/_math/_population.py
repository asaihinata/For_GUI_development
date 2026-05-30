'''母集団についての計算をする。'''
import numpy as np
from numpy import sqrt
from scipy.stats import norm
__all__=['cCoefficient','Population']
def cCoefficient(p=0.95):
 if not isinstance(p,float):
  raise TypeError('pにはfloat型で指定してください')
 elif not 0.0<=p<=1.0:
  raise ValueError('0.0<=p<=1.0で指定してください')
 return norm.ppf(p)
class Population:
 def __init__(self,data):
  self.data=data
 @property
 def n(self):return self.data.size
 @property
 def ave(self):
  return np.sum(self.data)/self.n
 @property
 def var(self):
  return np.sum((self.data-self.ave)**2)/self.n
 @property
 def SD(self):return sqrt(self.var)
 # 母比率の推定
 def ratio_E_samplingerror(self,p):
  if not isinstance(p,float):
   raise TypeError('pにはfloat型を指定してください')
  elif not 0.0<=p<=1.0:
   raise ValueError('pには0.0から1.0の範囲で指定してください')
  return 1.96*sqrt(p*(1-p)/self.n)
 def ratio_E(self,p):
  serror=self.ratio_E_samplingerror(p)
  return p+serror,p-serror
 def ratio_E_range(self,p):
  return self.ratio_E_samplingerror(p)*2
 def ratio_E_max(self,p):
  return p+self.ratio_E_samplingerror(p)
 def ratio_E_min(self,p):
  return p-self.ratio_E_samplingerror(p)
 # 母平均の推定
 def ave_E_samplingerror(self,p=0.95):
  return cCoefficient(p)*(self.SD/sqrt(self.n))
 def ave_E(self,p=0.95):
  ave=self.ave
  avs=self.ave_E_samplingerror(p)
  return ave+avs,ave-avs
 def ave_E_range(self,p=0.95):return self.ave_E_samplingerror(p)*2
 def ave_E_max(self,p=0.95):return self.ave+self.ave_E_samplingerror(p)
 def ave_E_min(self,p=0.95):return self.ave-self.ave_E_samplingerror(p)