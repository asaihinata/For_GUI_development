'''基本的な計算をするモジュール'''
from collections.abc import Iterator
from types import NotImplementedType
from typing import Any,Literal,overload
from _typeshed import Incomplete
from numpy import float64,int64,ndarray,ufunc
from numpy._typing import DTypeLike
from ..base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 data:ndarray
 def __init__(
self,
data:list|tuple|ndarray,
dtype:DTypeLike=float64,
depth_limit:int|None=None,
axis:int|None=None
)->None:'''
 :param data: データの配列を指定する。
 :type data: list|tuple|ndarray
 :param dtype: numpyの配列で指定する型を指定する。
 :type dtype: DTypeLike|None
 :param depth_limit: 配列の最大の深さを指定する。
 :type depth_limit: int|None
 :param axis: 計算処理を行う方向を指定する。
 :type axis: int|None'''
 def __repr__(self)->str:...
 def __iter__(self)->Iterator[Any]:...
 def __abs__(self)->NPNumber:...
 def __add__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 def __sub__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 def __mul__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 def __truediv__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 __radd__=__add__
 __rsub__=__sub__
 __rmul__=__mul__
 __rtruediv__=__truediv__
 __iadd__=__add__
 __isub__=__sub__
 __imul__=__mul__
 __itruediv__=__truediv__
 def __eq__(self,value:ndarray|NPNumber)->ndarray[Incomplete]:...
 def __ne__(self,value:ndarray|NPNumber)->ndarray[Incomplete]:...
 def __lt__(self,other:ndarray|NPNumber)->ndarray[Incomplete]:...
 def __le__(self,other:ndarray|NPNumber)->ndarray[Incomplete]:...
 def __gt__(self,other:ndarray|NPNumber)->ndarray[Incomplete]:...
 def __ge__(self,other:ndarray|NPNumber)->ndarray[Incomplete]:...
 def __mod__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 def __floordiv__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 def __pow__(self,other:int|float|ndarray|NPNumber)->NPNumber:...
 def __array_ufunc__(
self,
ufunc:ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args:Any,
**kwargs:Any
)->Any|NotImplementedType|NPNumber:...
 def __digits(self,digit:int)->int64:...
 @property
 def T(self)->NPNumber:...
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
)->ndarray:...
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
)->ndarray:...
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']|None=...,
digit:int|None=...
)->float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']|None
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を返す。
 :rtype: float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['none']|None=None
)->float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :return: スタージェスの公式で求めた値を返す。
 :rtype: float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='floor',
digit:int|None=...
)->float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.floor()`で返す。
 :rtype: float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='trunc',
digit:int|None=...
)->float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.trunc()`で返す。
 :rtype: float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='ceil',
digit:int|None=...
)->float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.ceil()`で返す。
 :rtype: float64'''
 @overload
 def sturgesval(
self,
decimal:Literal['floor','trunc','ceil','round','none']='round',
digit:int|None=...
)->float64:'''データ数からヒストグラムの階級数を求める。(スタージェスの公式を使用)

 :param decimal: 小数点以下の処理について指定する。
 :type decimal: Literal['floor','trunc','ceil','round','none']
 :param digit: 返す小数点の桁数を指定する。
 :type digit: int|None
 :return: スタージェスの公式で求めた値を`numpy.round()`で返す。
 :rtype: float64'''
 def ratio(
self,
axis:int|None=None
)->ndarray:'''行や列ごとの合計に対する比率を求める。'''
 def zero_check(self)->ndarray:'''要素の数値が0の位置を探す'''