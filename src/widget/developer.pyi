from collections.abc import Iterator
from typing import Any,Iterable,NoReturn,overload
from numpy import float64,int64,ndarray
from numpy._typing import NDArray,_ShapeLike
from numpy.random import Generator
from ..types import Numbertype
class clear:
 def __init__(self)->None:...
 def __dir__(self)->list[str]:...
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:...
class rand:
 seeds:int
 rng:Generator
 __firstlineno__:int
 __module__:str
 __dict__:dict[str,Any]
 __doc__:str
 __sizeof__:int
 def __dir__(self)->Iterable[str]:...
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:...
 def __init__(self)->None:
  self.seeds:int
  self.rng:Generator
 @overload
 @classmethod
 def rand(cls)->float:'''0から1の間の値をランダムに生成する。

 :return: 0から1の間の値をランダムに生成された値を返す。
 :rtype: float'''
 @overload
 @classmethod
 def rand(cls,size:_ShapeLike=None)->ndarray:'''0から1の間の値をランダムに生成した`numpy`の配列を作る。

 :param size: 配列のサイズを指定する。
 :type size: _ShapeLike
 :return: `numpy`の配列を返す。
 :rtype: ndarray'''
 @overload
 @classmethod
 def randn(cls,size:None|_ShapeLike=None)->float|NDArray[float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。

 :param size: サイズを指定する。
 :type size: None|_ShapeLike
 :return: 乱数の値を返す
 :rtype: float|NDArray[float64]'''
 @overload
 @classmethod
 def randn(cls,size:None=None)->float:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。

 :param size: サイズを指定する。
 :type size: None
 :return: 乱数の値を返す
 :rtype: float'''
 @overload
 @classmethod
 def randn(cls,size:_ShapeLike=None)->NDArray[float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。

 :param size: サイズを指定する。
 :type size: _ShapeLike
 :return: 乱数の値を返す
 :rtype: NDArray[float64]'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=...
)->int64|ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
endpoint:bool=...
)->int64:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=None,
endpoint:bool=...
)->ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=True
)->int64|ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`]に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=False
)->int64|ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`)に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 @classmethod
 def randrange(cls,min=0,max=1)->float:'''`min`から`max`の範囲の値をランダムに生成する。

 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :return: 範囲内のランダムに生成された値を返す。
 :rtype: float'''
 @overload
 @classmethod
 def randrange(cls,min=0,max=1,size:_ShapeLike=None)->ndarray:
  '''`min`から`max`の範囲の値をランダムに生成された値の配列を作成する。

 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :param size: 配列の大きさを指定する。
 :type size: _ShapeLike
 :return: `min`から`max`の範囲の値をランダムに生成された値の配列を返す。
 :rtype: ndarray'''
 @classmethod
 def seed(cls,seeds:int)->NoReturn:'''seed値を変更する。

 :param seeds: seed値を指定する。
 :type seeds: int'''
 @classmethod
 def normal(
self,
low:Numbertype=0,
high:Numbertype=1,
lenght:int=1,
hierarchy:int=1
)->ndarray:'''指定された行数と列数分のランダムに生成された正規分布のnumpyの配列を返す。

 :param low: 分布の平均値を指定する。
 :type low: int
 :param high: 分布の標準偏差を指定する。
 :type high: int
 :param lenght: 生成される配列の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の行数を指定する。
 :type hierarchy: int
 :return: 指定された行数と列数分の正規分布のnumpyの配列を返す。
 :rtype: ndarray'''
 @overload
 @classmethod
 def rands(
cls,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
)->NDArray[float64]:'''指定されたの個数のランダムに生成された値の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された値の配列を返す。
 :rtype: NDArray[float64]'''
 @overload
 @classmethod
 def rands(
cls,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[float64]:'''指定されたのサイズのランダムに生成された値の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された値の配列を返す。
 :rtype: NDArray[float64]'''
 @overload
 @classmethod
 def randsint(
cls,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
)->NDArray[int64]:'''指定されたの個数のランダムに生成された整数の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された整数の配列を返す。
 :rtype: NDArray[int64]'''
 @overload
 @classmethod
 def randsint(
cls,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[int64]:'''指定されたのサイズのランダムに生成された整数の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された整数の配列を返す。
 :rtype: NDArray[int64]'''
 @classmethod
 def listrand(
cls,
arr:LIST|list|tuple|ndarray,
size:int|tuple[int,int]|None=None
)->ndarray:'''配列から重複ありのランダムに選択された要素の配列を作成する。

 :param arr: 配列を指定する。
 :type arr: LIST|list|tuple|ndarray
 :param size: 作成する配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :return: 配列から重複ありのランダムに選択された要素の配列を返す。
 :rtype: ndarray'''
class rands:
 seeds:int
 rng:Generator
 __firstlineno__:int
 __module__:str
 __dict__:dict[str,Any]
 __doc__:str
 __sizeof__:int
 def __dir__(self)->Iterable[str]:...
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:...
 def __init__(self)->None:
  self.seeds:int
  self.rng:Generator
 @overload
 def rand(self)->float:'''0から1の間の値をランダムに生成する。

 :return: 0から1の間の値をランダムに生成された値を返す。
 :rtype: float'''
 @overload
 def rand(self,size:_ShapeLike=None)->ndarray:'''0から1の間の値をランダムに生成した`numpy`の配列を作る。

 :param size: 配列のサイズを指定する。
 :type size: _ShapeLike
 :return: `numpy`の配列を返す。
 :rtype: ndarray'''
 @overload
 def randn(self,size:None|_ShapeLike=None)->float|NDArray[float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。

 :param size: サイズを指定する。
 :type size: None|_ShapeLike
 :return: 乱数の値を返す
 :rtype: float|NDArray[float64]'''
 @overload
 def randn(self,size:None=None)->float:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。

 :param size: サイズを指定する。
 :type size: None
 :return: 乱数の値を返す
 :rtype: float'''
 @overload
 def randn(self,size:_ShapeLike=None)->NDArray[float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。

 :param size: サイズを指定する。
 :type size: _ShapeLike
 :return: 乱数の値を返す
 :rtype: NDArray[float64]'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=...
)->int64|ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
endpoint:bool=...
)->int64:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=None,
endpoint:bool=...
)->ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :raises TypeError: `low`にint型を指定しなかった場合に発生させる。
 :raises TypeError: `high`にNoneを除くint型を指定しなかった場合に発生させる。
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=True
)->int64|ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`]に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=False
)->int64|ndarray:'''ランダムに生成された整数を作成する。

 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`)に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: int64|ndarray'''
 @overload
 def randrange(self,min=0,max=1)->float:'''`min`から`max`の範囲の値をランダムに生成する。

 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :return: 範囲内のランダムに生成された値を返す。
 :rtype: float'''
 @overload
 def randrange(self,min=0,max=1,size:_ShapeLike=None)->ndarray:
  '''`min`から`max`の範囲の値をランダムに生成された値の配列を作成する。

 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :param size: 配列の大きさを指定する。
 :type size: _ShapeLike
 :return: `min`から`max`の範囲の値をランダムに生成された値の配列を返す。
 :rtype: ndarray'''
 def seed(self,seeds:int)->NoReturn:'''seed値を変更する。

 :param seeds: seed値を指定する。
 :type seeds: int'''
 def normal(
self,
low:Numbertype=0,
high:Numbertype=1,
lenght:int=1,
hierarchy:int=1
)->ndarray:'''指定された行数と列数分のランダムに生成された正規分布のnumpyの配列を返す。

 :param low: 分布の平均値を指定する。
 :type low: int
 :param high: 分布の標準偏差を指定する。
 :type high: int
 :param lenght: 生成される配列の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の行数を指定する。
 :type hierarchy: int
 :return: 指定された行数と列数分の正規分布のnumpyの配列を返す。
 :rtype: ndarray'''
 @overload
 def rands(
self,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
)->NDArray[float64]:'''指定されたの個数のランダムに生成された値の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された値の配列を返す。
 :rtype: NDArray[float64]'''
 @overload
 def rands(
self,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[float64]:'''指定されたのサイズのランダムに生成された値の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された値の配列を返す。
 :rtype: NDArray[float64]'''
 @overload
 def randsint(
self,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
)->NDArray[int64]:'''指定されたの個数のランダムに生成された整数の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された整数の配列を返す。
 :rtype: NDArray[int64]'''
 @overload
 def randsint(
self,
low:Numbertype=...,
high:Numbertype|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[int64]:'''指定されたのサイズのランダムに生成された整数の配列を返す。

 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された整数の配列を返す。
 :rtype: NDArray[int64]'''
 def listrand(
self,
arr:LIST|list|tuple|ndarray,
size:int|tuple[int,int]|None=None
)->ndarray:'''配列から重複ありのランダムに選択された要素の配列を作成する。

 :param arr: 配列を指定する。
 :type arr: LIST|list|tuple|ndarray
 :param size: 作成する配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :return: 配列から重複ありのランダムに選択された要素の配列を返す。
 :rtype: ndarray'''
class sort:
 __static_attributes__:tuple[str]
 __class__:type
 __firstlineno__:int
 @overload
 def __init__(self,data:list|tuple|LIST,type:bool)->None:'''配列内の要素を昇順で並べ変える。

 :param data: 並べ替えたい配列を指定する。
 :type data: list|tuple|LIST
 :param type: 昇順か降順かを指定する。
 :type type: bool
 :raises TypeError: dataに配列の型を指定しなかった場合に発生させる'''
 @overload
 def __init__(self,data:list|tuple|LIST,type:bool=True)->None:'''配列内の要素を昇順で並べ変える。

 :param data: 並べ替えたい配列を指定する。
 :type data: list|tuple|LIST
 :param type: 昇順か降順かを指定する。
 :type type: bool
 :raises TypeError: dataに配列の型を指定しなかった場合に発生させる'''
 @overload
 def __init__(self,data:list|tuple|LIST,type:bool=False)->None:'''配列内の要素を降順で並べ変える。

 :param data: 並べ替えたい配列を指定する。
 :type data: list|tuple|LIST
 :param type: 昇順か降順かを指定する。
 :type type: bool
 :raises TypeError: dataに配列の型を指定しなかった場合に発生させる'''
 def __dir__(self)->list[str]:...
 @classmethod
 def __instancecheck__(cls,ins)->bool:...
 def __contains__(self,val:Any)->bool:...
 def __iter__(self)->Iterator[Any]:...
 def __bool__(self)->bool:...
 def __len__(self)->int:...
 def __reversed__(self)->sort:...
class LIST:
 __static_attributes__:tuple[str]
 __class__:type
 __firstlineno__:int
 def __init__(self,lists:Any,*arg:tuple)->None:'''配列を作成する。'''
 def __add__(self,val:list|tuple|LIST)->LIST:...
 def __radd__(self,val:list|tuple|LIST)->LIST:...
 def __iadd__(self,val:Any)->LIST:...
 def __mul__(self,val:int)->LIST:...
 def __contains__(self,val)->bool:...
 def __len__(self)->int:...
 def __iter__(self)->Iterator[Any]:...
 def __reversed__(self)->LIST:...
 def __eq__(self,lists:LIST)->bool:...
 def __ne__(self,lists:LIST)->bool:...
 @classmethod
 def __instancecheck__(cls,ins)->bool:...
 @overload
 def __getitem__(self,val:int)->Any:...
 @overload
 def __getitem__(self,val:slice)->list:...
 def __dir__(self)->list:...
 def __getattribute__(self,name:Any)->Any:...
 def flatten(self)->list:'''多次元配列を一次元配列に変換する。'''
 def get(self,val:int)->list:...
 def append(self,*arg:tuple)->None:...
 def clear(self)->NoReturn:'''LISTの要素を削除する。'''
 @overload
 def sort(self,type:bool=True)->LIST:'''LISTの要素を昇順で並べ替える。'''
 @overload
 def sort(self,type:bool=False)->LIST:'''LISTの要素を降順で並べ替える。'''
class Number:
 __static_attributes__:tuple[str]
 __class__:type
 __firstlineno__:int
 val:Numbertype
 def __init__(self,val:int|float|bool|Number)->None:'''数値に関するクラス

 :param val: 数値を指定する。
 :type val: int|float|bool|Number
 :raises TypeError: `val`に数値以外を指定した場合に発生させる。'''
 def __dir__(self)->list[str]:...
 def __getattribute__(self,name:Any)->Any:...
 @classmethod
 def __instancecheck__(cls,ins)->bool:...
 def __int__(self)->int:...
 def __float__(self)->float:...
 def __str__(self)->str:...
 def __bool__(self)->bool:'''値が0以上ならTrueを,0未満ならFalseを返す。'''
 def __format__(self,format_spec:str)->str:...
 def format(self,format_spec:str)->str:...
 def __len__(self)->int:...
 def len(self)->int:...
 def types(self)->Numbertype:...
 def __add__(self,val:int|float|Number)->Number:...
 def __sub__(self,val:int|float|Number)->Number:...
 def __mul__(self,val:int|float|Number)->Number:...
 def __pow__(self,val:int|float|Number)->Number:...
 def __floordiv__(self,val:int|float|Number)->Number:...
 def __ipow__(self,val:int|float|Number)->Number:...
 def __truediv__(self,val:int|float|Number)->Number:...
 def __pow__(self,val:int|float|Number)->Number:...
 def __ipow__(self,val:int|float|Number)->Number:...
 def __radd__(self,val:int|float|Number)->Number:...
 def __rsub__(self,val:int|float|Number)->Number:...
 def __rmul__(self,val:int|float|Number)->Number:...
 def __rtruediv__(self,val:int|float|Number)->Number:...
 def __rmod__(self,val:int|float|Number)->Number:...
 def __rpow__(self,val:int|float|Number)->Number:...
 def __rfloordiv__(self,val:int|float|Number)->Number:...
 def __iadd__(self,val:int|float|Number)->Number:...
 def __isub__(self,val:int|float|Number)->Number:...
 def __imul__(self,val:int|float|Number)->Number:...
 def __itruediv__(self,val:int|float|Number)->Number:...
 def __eq__(self,val:Any)->bool:...
 def __ne__(self,val:Any)->bool:...
 def __lt__(self,val:int|float|Number)->bool:...
 def __le__(self,val:int|float|Number)->bool:...
 def __gt__(self,val:int|float|Number)->bool:...
 def __ge__(self,val:int|float|Number)->bool:...
 def __abs__(self)->Number:...
 def __round__(self,n:int=0)->Number:...
 def __ceil__(self)->Number:...
 def __floor__(self)->Number:...
 def __neg__(self)->Number:...
 def __pos__(self)->Number:...
 def value(self)->Numbertype:...