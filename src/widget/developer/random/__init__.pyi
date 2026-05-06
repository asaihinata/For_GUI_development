from collections.abc import Iterable
from typing import Any,NoReturn,overload
import numpy as np
from numpy._typing import (NDArray,_ArrayLikeFloat_co,_FloatLike_co,
                           _ShapeLike)
from numpy.random import Generator
from ...developer import LIST
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
 def rand(cls,size:_ShapeLike=None)->np.ndarray:'''0から1の間の値をランダムに生成した`numpy`の配列を作る。
 :param size: 配列のサイズを指定する。
 :type size: _ShapeLike
 :return: `numpy`の配列を返す。
 :rtype: np.ndarray'''
 @overload
 @classmethod
 def randn(cls,size:None|_ShapeLike=None)->float|NDArray[np.float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。
 :param size: サイズを指定する。
 :type size: None|_ShapeLike
 :return: 乱数の値を返す
 :rtype: float|NDArray[np.float64]'''
 @overload
 @classmethod
 def randn(cls,size:None=None)->float:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。
 :param size: サイズを指定する。
 :type size: None
 :return: 乱数の値を返す
 :rtype: float'''
 @overload
 @classmethod
 def randn(cls,size:_ShapeLike=None)->NDArray[np.float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。
 :param size: サイズを指定する。
 :type size: _ShapeLike
 :return: 乱数の値を返す
 :rtype: NDArray[np.float64]'''
 @overload
 @overload
 @classmethod
 def gamma(cls,shape:_FloatLike_co,scale:_FloatLike_co=1,size:None=None)->float:...
 @overload
 @classmethod
 def gamma(cls,shape:_ArrayLikeFloat_co,scale:_ArrayLikeFloat_co=1,size:_ShapeLike|None=None)->NDArray[np.float64]:...
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=...
)->np.int64|np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
endpoint:bool=...
)->np.int64:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=None,
endpoint:bool=...
)->np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=True
)->np.int64|np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`]に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
 @overload
 @classmethod
 def randint(
cls,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=False
)->np.int64|np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`)に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
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
 def randrange(cls,min=0,max=1,size:_ShapeLike=None)->np.ndarray:
  '''`min`から`max`の範囲の値をランダムに生成された値の配列を作成する。
 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :param size: 配列の大きさを指定する。
 :type size: _ShapeLike
 :return: `min`から`max`の範囲の値をランダムに生成された値の配列を返す。
 :rtype: np.ndarray'''
 @classmethod
 def seed(cls,seeds:int)->NoReturn:'''seed値を変更する。
 :param seeds: seed値を指定する。
 :type seeds: int'''
 @classmethod
 def normal(
self,
low:int|float=0,
high:int|float=1,
lenght:int=1,
hierarchy:int=1
)->np.ndarray:'''指定された行数と列数分のランダムに生成された正規分布のnumpyの配列を返す。
 :param low: 分布の平均値を指定する。
 :type low: int
 :param high: 分布の標準偏差を指定する。
 :type high: int
 :param lenght: 生成される配列の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の行数を指定する。
 :type hierarchy: int
 :return: 指定された行数と列数分の正規分布のnumpyの配列を返す。
 :rtype: np.ndarray'''
 @overload
 @classmethod
 def rands(
cls,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
)->NDArray[np.float64]:'''指定されたの個数のランダムに生成された値の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された値の配列を返す。
 :rtype: NDArray[np.float64]'''
 @overload
 @classmethod
 def rands(
cls,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[np.float64]:'''指定されたのサイズのランダムに生成された値の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された値の配列を返す。
 :rtype: NDArray[np.float64]'''
 @overload
 @classmethod
 def randsint(
cls,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
)->NDArray[np.int64]:'''指定されたの個数のランダムに生成された整数の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された整数の配列を返す。
 :rtype: NDArray[np.int64]'''
 @overload
 @classmethod
 def randsint(
cls,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[np.int64]:'''指定されたのサイズのランダムに生成された整数の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された整数の配列を返す。
 :rtype: NDArray[np.int64]'''
 @classmethod
 def listrand(
cls,
arr:LIST|list|tuple|np.ndarray,
size:int|tuple[int,int]|None=None
)->np.ndarray:'''配列から重複ありのランダムに選択された要素の配列を作成する。
 :param arr: 配列を指定する。
 :type arr: LIST|list|tuple|np.ndarray
 :param size: 作成する配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :return: 配列から重複ありのランダムに選択された要素の配列を返す。
 :rtype: np.ndarray'''
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
 def rand(self,size:_ShapeLike=None)->np.ndarray:'''0から1の間の値をランダムに生成した`numpy`の配列を作る。
 :param size: 配列のサイズを指定する。
 :type size: _ShapeLike
 :return: `numpy`の配列を返す。
 :rtype: np.ndarray'''
 @overload
 def randn(self,size:None|_ShapeLike=None)->float|NDArray[np.float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。
 :param size: サイズを指定する。
 :type size: None|_ShapeLike
 :return: 乱数の値を返す
 :rtype: float|NDArray[np.float64]'''
 @overload
 def randn(self,size:None=None)->float:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。
 :param size: サイズを指定する。
 :type size: None
 :return: 乱数の値を返す
 :rtype: float'''
 @overload
 def randn(self,size:_ShapeLike=None)->NDArray[np.float64]:'''標準正規分布(平均0,標準偏差1)に従う乱数を生成する。
 :param size: サイズを指定する。
 :type size: _ShapeLike
 :return: 乱数の値を返す
 :rtype: NDArray[np.float64]'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=...
)->np.int64|np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
endpoint:bool=...
)->np.int64:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param endpoint: 生成される値の区間を指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=None,
endpoint:bool=...
)->np.ndarray:'''ランダムに生成された整数を作成する。
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
 :rtype: np.int64|np.ndarray'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=True
)->np.int64|np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`]に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
 @overload
 def randint(
self,
low:int,
high:int|None=None,
size:int|tuple[int,int]|None=...,
endpoint:bool=False
)->np.int64|np.ndarray:'''ランダムに生成された整数を作成する。
 :param low: ランダムに生成される整数の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される整数の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param size: 生成される配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :param endpoint: 生成される値の区間を[`low`,`high`)に指定する。
 :type endpoint: bool
 :return: ランダムに生成された整数を返す。
 :rtype: np.int64|np.ndarray'''
 @overload
 def gamma(self,shape:_FloatLike_co,scale:_FloatLike_co=1,size:None=None)->float:...
 @overload
 def gamma(self,shape:_ArrayLikeFloat_co,scale:_ArrayLikeFloat_co=1,size:_ShapeLike|None=None)->NDArray[np.float64]:...
 @overload
 def randrange(self,min=0,max=1)->float:'''`min`から`max`の範囲の値をランダムに生成する。
 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :return: 範囲内のランダムに生成された値を返す。
 :rtype: float'''
 @overload
 def randrange(self,min=0,max=1,size:_ShapeLike=None)->np.ndarray:
  '''`min`から`max`の範囲の値をランダムに生成された値の配列を作成する。
 :param min: ランダムに生成する値の最小値を指定する。
 :type min: int
 :param max: ランダムに生成する値の最大値を指定する。
 :type max: int
 :param size: 配列の大きさを指定する。
 :type size: _ShapeLike
 :return: `min`から`max`の範囲の値をランダムに生成された値の配列を返す。
 :rtype: np.ndarray'''
 def seed(self,seeds:int)->NoReturn:'''seed値を変更する。
 :param seeds: seed値を指定する。
 :type seeds: int'''
 def normal(
self,
low:int|float=0,
high:int|float=1,
lenght:int=1,
hierarchy:int=1
)->np.ndarray:'''指定された行数と列数分のランダムに生成された正規分布のnumpyの配列を返す。
 :param low: 分布の平均値を指定する。
 :type low: int
 :param high: 分布の標準偏差を指定する。
 :type high: int
 :param lenght: 生成される配列の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の行数を指定する。
 :type hierarchy: int
 :return: 指定された行数と列数分の正規分布のnumpyの配列を返す。
 :rtype: np.ndarray'''
 @overload
 def rands(
self,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
)->NDArray[np.float64]:'''指定されたの個数のランダムに生成された値の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された値の配列を返す。
 :rtype: NDArray[np.float64]'''
 @overload
 def rands(
self,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[np.float64]:'''指定されたのサイズのランダムに生成された値の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された値の配列を返す。
 :rtype: NDArray[np.float64]'''
 @overload
 def randsint(
self,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
)->NDArray[np.int64]:'''指定されたの個数のランダムに生成された整数の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :return: 指定されたの個数のランダムに生成された整数の配列を返す。
 :rtype: NDArray[np.int64]'''
 @overload
 def randsint(
self,
low:int|float=...,
high:int|float|None=...,
lenght:int=...,
hierarchy:int|None=None,
)->NDArray[np.int64]:'''指定されたのサイズのランダムに生成された整数の配列を返す。
 :param low: ランダムに生成される値の最小値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type low: int
 :param high: ランダムに生成される値の最大値を指定する。ただし`high`がNoneの場合,`low`が0に,`high`が`low`になる。
 :type high: int|None
 :param lenght: 生成される配列の要素の列数を指定する。
 :type lenght: int
 :param hierarchy: 生成される配列の要素の行数を指定する。
 :type hierarchy: int
 :return: 指定されたのサイズのランダムに生成された整数の配列を返す。
 :rtype: NDArray[np.int64]'''
 def listrand(
self,
arr:LIST|list|tuple|np.ndarray,
size:int|tuple[int,int]|None=None
)->np.ndarray:'''配列から重複ありのランダムに選択された要素の配列を作成する。
 :param arr: 配列を指定する。
 :type arr: LIST|list|tuple|np.ndarray
 :param size: 作成する配列の大きさを指定する。
 :type size: int|tuple[int,int]|None
 :return: 配列から重複ありのランダムに選択された要素の配列を返す。
 :rtype: np.ndarray'''