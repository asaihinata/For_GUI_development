from collections.abc import Iterator
from typing import Any,overload
from ...developer import LIST
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