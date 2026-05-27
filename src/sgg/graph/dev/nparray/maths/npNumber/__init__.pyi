'''基本的な計算をするモジュール'''
from types import NotImplementedType
from typing import Any,Literal,overload
import numpy as np
from numpy._typing import DTypeLike
from ...base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 data:np.ndarray
 def __init__(
self,
data:np._ArrayT,
dtype:DTypeLike=np.float32,
axis:int|None=None
)->None:...
 def __abs__(self)->NPNumber:...
 def __repr__(self)->str:...
 def __add__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 def __sub__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 def __mul__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 def __truediv__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 __radd__=__add__
 __rsub__=__sub__
 __rmul__=__mul__
 __rtruediv__=__truediv__
 def __mod__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 def __floordiv__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 def __pow__(self,other:int|float|np.ndarray|NPNumber)->NPNumber:...
 def __array_ufunc__(self,ufunc,method,*args,**kwargs)->NPNumber|Any|NotImplementedType:...
 def __digits(self,digit:int)->np.int64:...
 @property
 def sum(self):...
 @property
 def median(self):...
 @property
 def var(self):...
 @property
 def max(self):...
 @property
 def min(self):...
 @property
 def mean(self):...
 @property
 def std(self):...
 @property
 def pow2(self):...
 @property
 def deviation(self):'''標準偏差を求める。'''
 @property
 def log(self):...
 @property
 def log10(self):...
 @property
 def log2(self):...
 @property
 def log1p(self):...
 @property
 def degree(self):...
 @property
 def radian(self):...
 def logx(self,x:int|float):...
 def mod(self,x):...
 def divmod(self,x):...
 def pow(self,x)->NPNumber:...
 def sqrt(self,root:int|float=2)->NPNumber:...
 def floor(self,digit:int|None=...)->NPNumber:...
 def trunc(self,digit:int|None=...)->NPNumber:...
 def ceil(self,digit:int|None=...)->NPNumber:...
 def round(self,digit:int|None=...)->NPNumber:...
 def cussum(self)->NPNumber:'''一つ前の元の値との和を求める。'''
 def cumprod(self)->NPNumber:'''一つ前の元の値との積を求める。'''
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
)->np.ndarray:...
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
)->np.ndarray:...
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']|None=...,
digit:int|None=...
)->np.float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']|None
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を返す。
 :rtype: np.float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['none']|None=None
)->np.float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :return: スタージェスの公式で求めた値を返す。
 :rtype: np.float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='floor',
digit:int|None=...
)->np.float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.floor()`で返す。
 :rtype: np.float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='trunc',
digit:int|None=...
)->np.float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.trunc()`で返す。
 :rtype: np.float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='ceil',
digit:int|None=...
)->np.float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.ceil()`で返す。
 :rtype: np.float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='round',
digit:int|None=...
)->np.float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.round()`で返す。
 :rtype: np.float64'''
 def ratio(
self,
axis:int|None=None
)->np.ndarray:'''行や列ごとの合計に対する比率を求める。'''