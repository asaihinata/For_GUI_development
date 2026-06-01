from collections.abc import Iterator
from types import NotImplementedType
from typing import Any,Literal
from numpy import _CopyMode,_ScalarT,dtype,ndarray,ufunc
from numpy._typing import DTypeLike
__all__=['NPArray']
class NPArray:
 dtype:DTypeLike
 data:ndarray
 name:str
 def __init__(
self,
data:list|tuple|ndarray,
dtype:DTypeLike|None=None,
depth_limit:int|None=None
)->None:'''
 :param data: データの配列を指定する。
 :type data: list|tuple|ndarray
 :param dtype: numpyの配列で指定する型を指定する。
 :type dtype: DTypeLike|None
 :param depth_limit: 配列の最大の深さを指定する。
 :type depth_limit: int|None'''
 def __getitem__(self,key:Any)->Any:...
 def __contains__(self,item:Any)->bool:...
 def __repr__(self)->str:...
 def __iter__(self)->Iterator[Any]:...
 def __len__(self)->int:...
 def __array__(
self,
dtype:DTypeLike|None=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def __array_ufunc__(
self,
ufunc:ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args:Any,
**kwargs:Any
)->Any|NotImplementedType|NPArray:...
 def tolist(self)->list:'''list型にして返す。'''
 def sort(self)->NPArray:'''`data`にソートを実行する。'''
 def first_pop(self)->NPArray:'''配列の最初の要素のコピーをその配列の末尾に追加する。'''
 def first_element(self):'''`data`の最初の要素を取得する。'''
 @property
 def nbytes(self)->int:...
 @property
 def T(self)->NPArray:...
 @property
 def ndim(self)->int:...
 @property
 def shape(self)->tuple[int,...]:...
 @property
 def size(self)->int:...
 def astype(
self,
dtype:DTypeLike|None
)->NPArray:'''`dtype`で指定された型に変更します。'''
 def lengtharange(
self,
start:int=0,
dtype:DTypeLike|None=None
)->ndarray:...
 def _flatten(self)->tuple[ndarray[tuple[int],dtype[_ScalarT]],tuple[int,...]]:...
 def flatten(self)->NPArray:...
 def dimension(self)->bool:'''`data`の次元が1次元か判定する。'''
 def dimensions(self)->bool:'''`data`の次元が多次元か判定する。'''
 def get(self,val:int)->Any:'''配列の`val`番目の要素を取得する。'''
 def reshape(self,size:tuple[int,...])->NPArray:...