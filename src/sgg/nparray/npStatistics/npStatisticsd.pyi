'''基本的な統計の計算をするモジュール'''
from typing import Any,TypeAlias,Literal
from numpy import ndarray
from numpy.typing import ArrayLike,NDArray
from ..npNumber import NPNumber
from ._math import Population
__all__=['NPStatisticsd']
BINS_LIST:TypeAlias=Literal['stone','auto','scott','doane','fd','rice','sqrt','sturges']
METHOD_LIST:TypeAlias=Literal[
'inverted_cdf',
'averaged_inverted_cdf',
'closest_observation',
'interpolated_inverted_cdf',
'hazen','weibull','linear',
'median_unbiased',
'normal_unbiased'
]
class NPStatisticsd:
 def __init__(
self,
data:NPNumber|ndarray=...
):...
 def __repr__(self)->str:...
 @property
 def data(self)->ndarray:...
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
 def deviation(self):'''偏差値を求める。'''
 @property
 def log(self):...
 @property
 def log10(self):...
 @property
 def log2(self):...
 @property
 def log1p(self):...
 @property
 def devsq(self):'''偏差平方和を求める。'''
 @property
 def range(self):...
 @property
 def skew(self):'''歪度を求める。'''
 @property
 def kurtosis(self):'''尖度を求める。'''
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
 def n(self):'''長さの数値を返す。'''
 @property
 def n1(self):'''長さの数値-1の値を返す。'''
 def hist_bin_edges(
self,
bins:int|BINS_LIST|ArrayLike=10,
range:tuple[float,float]|None=None,
weights:ArrayLike|None=None
)->NDArray[Any]:'''`bins`で指定された計算方法で計算されたビンの境界を求める。

 :param bins: ビンの数や計算方法を指定する。
 :type bins: int|BINS_LIST|ArrayLike
 :param range: ビンの下限と上限を指定する。
 :type range: tuple[float,float]|None
 :param weights: 重みを指定する。
 :type weights: ArrayLike|None
 :return: `bins`で指定された計算方法で計算した結果を返す。
 :rtype: NDArray[Any]'''