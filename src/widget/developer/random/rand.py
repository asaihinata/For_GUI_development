from sys import getsizeof
import numpy as np
from numpy.random import choice,default_rng
from ..LIST import LIST
from ..Number import Number
class rand:
 '''ランダムな値を生成する。'''
 seeds=42
 rng=default_rng(seed=42)
 def __init__(self):
  self.seeds=rand.seeds
  self.rng=rand.rng
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.rng)+getsizeof(self.seeds)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,rand)
 @classmethod
 def seed(cls,seeds):
  if isinstance(seeds,int):cls.seeds,cls.rng=seeds,default_rng(seed=seeds)
 @classmethod
 def rand(cls,size=None):return cls._rand(size)
 @staticmethod
 def _rand(size):return rand.rng.random(size)
 @classmethod
 def randn(cls,size=None):return cls._randn(size)
 @staticmethod
 def _randn(size):return rand.rng.standard_normal(size)
 @classmethod
 def randint(cls,low=1,high=None,size=None,endpoint=False):return cls._randint(low,high=high,size=size,endpoint=endpoint)
 @staticmethod
 def _randint(low,high=None,size=None,endpoint=False):return rand.rng.integers(low,high=high,size=size,endpoint=endpoint)
 @classmethod
 def gamma(cls,shape,scale=1,size=None):return rand.rng.gamma(shape,scale,size)
 @classmethod
 def randrange(cls,min=0,max=1,size=None):
  if max<min:min,max=max,min
  return cls._randrange(min,max,size)
 @staticmethod
 def _randrange(low,high,size):return rand.rng.random(size)*(high-low)+low
 @classmethod
 def normal(cls,low=0,high=1,lenght=None,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  return cls.rng.normal(low,high,(hierarchy,lenght)) if isinstance(hierarchy,int) and 2<=hierarchy else cls.rng.normal(low,high,lenght)
 @classmethod
 def rands(cls,low=1,high=None,lenght=1,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return cls.rng.uniform(low=low,high=high,size=(hierarchy,lenght))
  else:return cls.rng.uniform(low=low,high=high,size=lenght)
 @classmethod
 def randsint(cls,low=1,high=None,lenght=1,hierarchy=None):
  if isinstance(low,Number):low=low.val
  if isinstance(high,Number):high=high.val
  if high<low:high,high=high,low
  if isinstance(hierarchy,int) and 2<=hierarchy:return cls.rng.integers(low=low,high=high,size=(hierarchy,lenght))
  else:return cls.rng.integers(low=low,high=high,size=lenght)
 @classmethod
 def listrand(cls,arr,size=None):
  return choice(np.array(list(arr)if isinstance(arr,LIST) else arr),size=size)