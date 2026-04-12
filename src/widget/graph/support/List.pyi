'''グラフのx,y,z,dataの配列の変換を手助ける。'''
from collections.abc import Iterator
from typing import Any
from numpy import ndarray
from ...developer import LIST
class Datalist:
 def __init__(self,data:ndarray)->None:...
 def T(self)->ndarray:...
 def sort(self,axis:int=1)->ndarray:...
 def inversion(self)->ndarray:...
class Manylist(Datalist):
 def __init__(self,data:tuple|list|ndarray|LIST=None)->None: '''一次元配列を含む多次元配列を許す配列を作成する。

 :param data: 配列を指定する。
 :type data: tuple|list|ndarray|LIST
 :raises TypeError: `data`に配列以外の型を指定した場合に発生させる。'''
 def __iter__(self)->Iterator[list[Any]]:...
 def __len__(self)->int:...
class Onelist(Datalist):
 def __init__(self,data:tuple|list|ndarray|LIST=None)->None:'''一次元配列のみを許す配列を作成する。

 :param data: 一次元配列を指定する。
 :type data: tuple|list|ndarray|LIST
 :raises TypeError: `data`に配列の型以外で指定した場合に発生させる。
 :raises ValueError: `data`を多次元配列で指定した場合に発生させる。'''
 def __iter__(self)->Iterator[Any]:...
 def __len__(self)->int:...
class Conectlist(Datalist):
 def __init__(self,data:tuple|list|ndarray|LIST=None)->None:'''配列から一次元配列を作成する。

 :param data: 配列を指定する。
 :type data: tuple|list|ndarray|LIST
 :raises TypeError: `data`に配列以外の型を指定した場合に発生させる。'''
 def __iter__(self)->Iterator[Any]:...
 def __len__(self)->int:...