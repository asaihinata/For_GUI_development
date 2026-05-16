from sys import getsizeof
from numpy import asarray
from numpy.random import choice,default_rng
__all__=['rands']
class rands:
 '''ランダムな値を生成する。'''
 def __init__(self,seed=42):
  if not isinstance(seed,int):seed=42
  self.seeds=seed
  self.rng=default_rng(seed=seed)
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.rng)+getsizeof(self.seeds)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,rands)
 def seed(self,seed):
  if isinstance(seed,int):
   self.seeds=seed
   self.rng=default_rng(seed=seed)
 def gamma(self,shape,scale=1,size=None):return self.rng.gamma(shape,scale,size)
 def rand(self,size=None):return self.rng.random(size)
 def randn(self,size=None):return self.rng.standard_normal(size)
 def randint(self,low=1,high=None,size=None,endpoint=False):
  return self.rng.integers(low,high=high,size=size,endpoint=endpoint)
 def randrange(self,min=0,max=1,size=None):
  if max<min:min,max=max,min
  return self.rng.random(size)*(max-min)+max
 def normal(self,low=0,high=1,lenght=None,hierarchy=None):
  if isinstance(hierarchy,int) and 2<=hierarchy:
   return self.rng.normal(low,high,(hierarchy,lenght))
  else:
   return self.rng.normal(low,high,lenght)
 def rands(self,low=1,high=None,lenght=1,hierarchy=None):
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return self.rng.uniform(low=low,high=high,size=(hierarchy,lenght))
  else:return self.rng.uniform(low=low,high=high,size=lenght)
 def randsint(self,low=1,high=None,lenght=1,hierarchy=None):
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return self.rng.integers(low=low,high=high,size=(hierarchy,lenght))
  else:return self.rng.integers(low=low,high=high,size=lenght)
 def listrand(self,arr,size=None):return choice(asarray(arr),size=size)