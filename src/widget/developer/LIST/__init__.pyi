from collections.abc import Iterator
from typing import Any,NoReturn,overload
from numpy._core.numeric import _AnyShapeT
class LIST:
 __static_attributes__:tuple[str]
 __class__:type
 __firstlineno__:int
 lists:list
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
 def __getitem__(self,val:int|slice)->Any|list:...
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
 def count(self,val:Any)->int:'''指定した`val`が配列内にいくつ出現するか調べる。

 :param val: _description_
 :type val: Any
 :return: 配列内の出現数を返す。
 :rtype: int'''
 def empty(self)->bool:'''`LIST`が空かを調べる。

 :return: `LIST`が空かを調べる。
 :rtype: bool'''
 @overload
 @classmethod
 def range(
cls,
start:int=...,
end:int=...,
step:int=...,
endpoint:bool=False
)->LIST:'''stepの間隔でstartからendまでの範囲を生成する。

 :param start: 開始の値を指定する。
 :type start: int
 :param end: 終了の値を指定する。
 :type end: int
 :param step: 間隔を指定する。
 :type step: int
 :param endpoint: 範囲にendを含むか指定する。
 :type endpoint: bool
 :return:
 :rtype: LIST'''
 @overload
 @classmethod
 def range(
cls,
end:int=...
)->LIST:'''1の間隔で0からendまでの範囲を生成する。

 :param end: 終了の値を指定する。
 :type end: int
 :return:
 :rtype: LIST'''
 @overload
 @classmethod
 def range(
cls,
start:int=...,
end:int=...
)->LIST:'''1の間隔でstartからendまでの範囲を生成する。

 :param start: 開始の値を指定する。
 :type start: int
 :param end: 終了の値を指定する。
 :type end: int
 :return:
 :rtype: LIST'''
 @classmethod
 def full(
cls,
val:Any,
size:int|_AnyShapeT=...
)->LIST:'''`val`を`size`の大きさの配列を作成する。

 :param val: 埋めたい値を指定する。
 :type val: Any
 :param size: サイズを指定する。
 :type size: int|_AnyShapeT
 :return: `val`を`size`の大きさで埋めた配列を返す。
 :rtype: LIST'''