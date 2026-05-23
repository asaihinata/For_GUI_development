from typing import Literal
from numpy import _ArrayT,ndarray
from numpy._typing import DTypeLike
from ..base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 data:ndarray
 def __init__(
self,
data:_ArrayT,
dtype:DTypeLike|None=None
)->None:...
 def cussum(self)->NPNumber:'''一つ前の元の値との和を求める。'''
 def cumprod(self)->NPNumber:'''一つ前の元の値との積を求める。'''
 @property
 def sum(self):...
 def asum(self,axis:int|None=None,dtype:DTypeLike|None=None):...
 @property
 def median(self):...
 def amedian(self,axis:int|None=None):...
 @property
 def var(self):...
 def avar(self,axis:int|None=None,dtype:DTypeLike|None=None):...
 @property
 def max(self):...
 def amax(self,axis:int|None=None):...
 @property
 def min(self):...
 def amin(self,axis:int|None=None):...
 @property
 def mean(self):...
 def amean(self,axis:int|None=None,dtype:DTypeLike|None=None):...
 @property
 def std(self):...
 def astd(self,axis:int|None=None,dtype:DTypeLike|None=None):...
 def percentile(
self,
q:tuple[int,...],
axis:int|None=None,
method:Literal[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen',
'weibull',
'linear',
'median_unbiased',
'normal_unbiased'
]='linear'
):...
 def quantile(
self,
q:tuple[int,...],
axis:int|None=None,
method:Literal[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen',
'weibull',
'linear',
'median_unbiased',
'normal_unbiased'
]='linear'
):...