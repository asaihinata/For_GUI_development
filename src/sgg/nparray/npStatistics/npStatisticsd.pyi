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
 def sum(self):'''`data`の合計を求める'''
 @property
 def mean(self):'''`data`の算術平均を求める'''
 @property
 def ave(self):'''`data`の加重平均を求める'''
 @property
 def min(self):'''`data`の最低値を求める'''
 @property
 def max(self):'''`data`の最大値を求める'''
 @property
 def var(self):'''`data`の分散を求める'''
 @property
 def std(self):'''`data`の標準偏差を求める'''
 @property
 def pow2(self):'''`data`を2乗した値を求める'''
 @property
 def deviation(self):'''偏差値を求める。'''
 @property
 def log(self):'''`data`の底が`e`の対数を求める'''
 @property
 def log10(self):'''`data`の底が`10`の対数を求める'''
 @property
 def log2(self):'''`data`の底が`2`の対数を求める'''
 @property
 def log1p(self):'''np.log1p(data)を返す'''
 @property
 def devsq(self):'''偏差平方和を求める。'''
 @property
 def range(self):'''`data`の範囲を求める'''
 @property
 def skew(self):'''歪度を求める。'''
 @property
 def kurtosis(self):'''尖度を求める。'''
 def percentile(
self,
q:tuple[int|float,...],
axis:int|None=None,
method:METHOD_LIST='linear'
):'''指定したパーセンタイルを計算する。

 :param q: 求めたいパーセンタイル値を指定する。
 :type q: tuple[int|float,...]
 :param axis: 計算する軸を指定する。
 :type axis: int|None
 :param method: パーセンタイルを推定するために使用する方法を指定する。
 :type method: METHOD_LIST'''
 def quantile(
self,
q:tuple[float,...],
axis:int|None=None,
method:METHOD_LIST='linear'
):'''指定した分位点を計算する。

 :param q: 求めたい分位点を指定する。
 :type q: tuple[float,...]
 :param axis: 計算する軸を指定する。
 :type axis: int|None
 :param method: 分位点を推定するために使用する方法を指定する。
 :type method: METHOD_LIST'''
 def IQR(
axis:int|None=None,
method:METHOD_LIST='linear'
):'''`data`の四分位範囲を求める。

 :param axis: 計算する軸を指定する。
 :type axis: int|None
 :param method: 分位点を推定するために使用する方法を指定する。
 :type method: METHOD_LIST'''
 def outlier(self):'''四分位範囲の外れ値を求める。'''
 def population(self)->Population:'''data`の母集団を求める。

 :return: `Population`を返す。
 :rtype: Population'''
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