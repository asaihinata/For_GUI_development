from collections.abc import Iterator
from typing import Any,TypeAlias
from numpy import _ArrayT,_CopyMode,_DTypeT_co,ndarray
from ....typing import _T,Type_all,Type_NumberandNone,Type_Numberlike
__all__:Type_all=['NPArray']
DType:TypeAlias=_DTypeT_co|None
class NPArray:
 dtype:DType
 data:ndarray
 def __init__(
self,
data:_ArrayT,
*,
dtype:DType=None
)->None:...
 def __iter__(self)->Iterator[Any]:...
 def __array__(
self,
dtype:DType=None,
copy:bool|_CopyMode|None=None
)->ndarray:...
 def tolist(self)->_T:'''list型に変換する。

 :return:
 :rtype: _T'''
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
 def dimension(self)->bool:'''`data`の次元が1次元か判定する。'''
 def dimensions(self)->bool:'''`data`の次元が多次元か判定する。'''
 def cussum(self)->NPArray:...
 @classmethod
 def arange(
cls,
start:Type_Numberlike,
stop:Type_NumberandNone=None,
step:Type_NumberandNone=None,
dtype:DType=None
)->NPArray:...
 @classmethod
 def linspace(
cls,
start:Type_Numberlike,
stop:Type_Numberlike,
num:Type_Numberlike=50,
endpoint:bool=True,
dtype:DType=None
):...