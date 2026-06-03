from typing import overload,Literal
from numpy import dtype,float64,ndarray
from ..npNumber import NPNumber
from ._math import Population
__all__=['NPStatistics']
METHOD_LIST=Literal[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen','weibull','linear',
'median_unbiased',
'normal_unbiased'
]
class NPStatistics:
 x:ndarray
 y:ndarray
 data:ndarray
 @overload
 def __init__(
self,
data:NPNumber|ndarray=...
):...
 @overload
 def __init__(
self,
x:NPNumber|ndarray=...,
y:NPNumber|ndarray=...
):...
 def __repr__(self)->str:...
 ########
 #  x  #
 ########
 @property
 def xsum(self):...
 @property
 def xave(self):...
 @property
 def xmin(self):...
 @property
 def xmax(self):...
 @property
 def xmean(self):...
 @property
 def xvar(self):...
 @property
 def xstd(self):...
 @property
 def xpow2(self):...
 @property
 def xdeviation(self):'''`x`の偏差値を求める。'''
 @property
 def xlog(self):...
 @property
 def xlog10(self):...
 @property
 def xlog2(self):...
 @property
 def xlog1p(self):...
 @property
 def xdevsq(self):'''`x`の偏差平方和を求める。'''
 @property
 def xrange(self):...
 @property
 def xskew(self):'''`x`の歪度を求める。'''
 @property
 def xkurtosis(self):'''`x`の尖度を求める。'''
 def xpercentile(
self,
q:tuple[float,...],
axis=None,
method:METHOD_LIST='linear'
):...
 def xquantile(
self,
q:tuple[int|float,...],
axis=None,
method:METHOD_LIST='linear'
):...
 def xoutlier(self):...
 def xpopulation(self)->Population:...
 ########
 #  y  #
 ########
 @property
 def ysum(self):...
 @property
 def yave(self):...
 @property
 def ymin(self):...
 @property
 def ymax(self):...
 @property
 def ymean(self):...
 @property
 def yvar(self):...
 @property
 def ystd(self):...
 @property
 def ypow2(self):...
 @property
 def ydeviation(self):'''`y`の偏差値を求める。'''
 @property
 def ylog(self):...
 @property
 def ylog10(self):...
 @property
 def ylog2(self):...
 @property
 def ylog1p(self):...
 @property
 def ydevsq(self):'''`y`の偏差平方和を求める。'''
 @property
 def yrange(self):...
 @property
 def yskew(self):'''`y`の歪度を求める。'''
 @property
 def ykurtosis(self):'''`y`の尖度を求める。'''
 def ypercentile(
self,
q:tuple[float,...],
axis=None,
method:METHOD_LIST='linear'
):...
 def yquantile(
self,
q:tuple[int|float,...],
axis=None,
method:METHOD_LIST='linear'
):...
 def youtlier(self):...
 def ypopulation(self)->Population:...
 ##########
 #  data  #
 ##########
 @property
 def sum(self):...
 @property
 def ave(self):...
 @property
 def min(self):...
 @property
 def max(self):...
 @property
 def mean(self):...
 @property
 def var(self):...
 @property
 def std(self):...
 @property
 def pow2(self):...
 @property
 def deviation(self):'''`data`の偏差値を求める。'''
 @property
 def log(self):...
 @property
 def log10(self):...
 @property
 def log2(self):...
 @property
 def log1p(self):...
 @property
 def devsq(self):'''`data`の偏差平方和を求める。'''
 @property
 def range(self):...
 @property
 def skew(self):'''`data`の歪度を求める。'''
 @property
 def kurtosis(self):'''`data`の尖度を求める。'''
 def percentile(
self,
q:tuple[int|float,...],
axis=None,
method:METHOD_LIST='linear'
):...
 def quantile(
self,
q:tuple[int|float,...],
axis=None,
method:METHOD_LIST='linear'
):...
 def outlier(self):...
 def population(self)->Population:...
 @property
 def CV(self):'''変動係数を求める。'''
 @property
 def n(self):'''`data`の長さの数値を返す。'''
 @property
 def n1(self):'''`data`の長さの数値-1の値を返す。'''
 def covariance(self):'''共分散を求める。'''
 def correlation(self):'''相関係数を求める。'''
 def correlation_coefficient(self):'''単相関係数を求める。'''
 # x,y
 @property
 def Sxxyy(self):'''`x`の偏差平方和と`y`の偏差平方和の積を求める。'''
 @property
 def Sxxyyroot(self):'''`x`の偏差平方和と`y`の偏差平方和の積の平方和を求める。'''
 # 回帰直線
 def regression(
self,
n:int=1
)->ndarray[float64,dtype[float64]]:'''点(x,y)に次数`n`の多項式を当てはめる。'''