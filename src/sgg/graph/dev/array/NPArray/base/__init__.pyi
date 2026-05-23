from collections.abc import Iterator
from typing import TypeAlias
from numpy import _ArrayT,_CopyMode,_ScalarT,dtype,ndarray
from numpy._typing import DTypeLike
from .....typing import Any,Type_Numberlike,Type_NumberlikeN,ndarray
_Array1D:TypeAlias=ndarray[tuple[int],dtype[_ScalarT]]
__all__=['NPArray']
class NPArray:
 dtype:DTypeLike
 data:ndarray
 def __init__(
self,
data:_ArrayT,
dtype:DTypeLike|None=None
)->None:...
 def __iter__(self)->Iterator[Any]:...
 def __array__(
self,
dtype:DTypeLike|None=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def tolist(self)->Any|list:'''list型に変換する。

 :return:
 :rtype: Any|list'''
 def sort(self)->NPArray:'''`data`にソートを実行する。

 :return:
 :rtype: NPArray'''
 def first_pop(self)->NPArray:'''配列の最初の要素のコピーをその配列の末尾に追加する。

 :return:
 :rtype: NPArray'''
 @property
 def T(self)->NPArray:...
 @property
 def ndim(self)->int:...
 @property
 def shape(self)->tuple[int,...]:...
 @property
 def size(self)->int:...
 def _flatten(self)->tuple[_Array1D,tuple[int,...]]:...
 def flatten(self)->NPArray:...
 def dimension(self)->bool:'''`data`の次元が1次元か判定する。'''
 def dimensions(self)->bool:'''`data`の次元が多次元か判定する。'''
 @classmethod
 def arange(
cls,
start:Type_Numberlike,
stop:Type_NumberlikeN=None,
step:Type_NumberlikeN=None,
dtype:DTypeLike|None=None
)->NPArray:...
 @classmethod
 def linspace(
cls,
start:Type_Numberlike,
stop:Type_Numberlike,
num:Type_Numberlike=50,
endpoint:bool=True,
dtype:DTypeLike|None=None
):...