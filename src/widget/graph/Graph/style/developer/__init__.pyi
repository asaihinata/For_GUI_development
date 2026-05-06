from typing import Any,overload
import numpy as np
from .....developer import Number
Typenumberlike=bool|float|int|Number|np.float16|np.float32|np.float64|np.int16|np.int32|np.int64|np.int8|np.uint16|np.uint32|np.uint64|np.uint8
def range_zero_one(val:float,out:float=1.0,endpoint:bool=True)->float:...
def num1s(val:int|float|Number=0,mins:int|float|Number=1)->int|float|Number:...
def num0s(val:int|float|Number=0,mins:int|float|Number=0)->int|float|Number:...
def num0(val:int|float|Number=0,mins:int|float|Number=0)->int|float|Number:...
def list2float(lin:list[Any]|tuple[Any]=None)->bool:...
def listchose(val:str,arr:list,other:str|None=None)->str:...
class Angle:
 @overload
 def __init__(
self,
angle:Typenumberlike,
dtype:bool=...
)->None:'''度数法と弧度法の変換するクラス。
 :param angle: 変換したい角度を指定する。
 :type angle: Typenumberlike
 :param dtype: 弧度法から度数法に変換するか,度数法から弧度法に変換するか指定する。
 :type dtype: bool
 :raises TypeError: `angle`に数値の型を指定しなかった場合に発生させる'''
 @overload
 def __init__(
self,
angle:Typenumberlike,
dtype:bool=True
)->None:'''弧度法から度数法に変換する。
 :param angle: 変換したい角度を指定する。
 :type angle: Typenumberlike
 :param dtype: 弧度法から度数法に変換するか,度数法から弧度法に変換するか指定する。
 :type dtype: bool
 :raises TypeError: `angle`に数値の型を指定しなかった場合に発生させる'''
 @overload
 def __init__(
self,
angle:Typenumberlike,
dtype:bool=False
)->None:'''度数法から弧度法に変換する。
 :param angle: 変換したい角度を指定する。
 :type angle: Typenumberlike
 :param dtype: 弧度法から度数法に変換するか,度数法から弧度法に変換するか指定する。
 :type dtype: bool
 :raises TypeError: `angle`に数値の型を指定しなかった場合に発生させる'''
 @classmethod
 def __instancecheck__(cls,ins)->bool:...
 def __str__(self)->str:...
 def __int__(self)->int:...
 def __float__(self)->float:...
 def __eq__(self,val:int|float)->bool:...
 def __ne__(self,val:int|float)->bool:...
 def __lt__(self,val:int|float)->bool:...
 def __le__(self,val:int|float)->bool:...
 def __gt__(self,val:int|float)->bool:...
 def __ge__(self,val:int|float)->bool:...
class Rad:
 '''弧度法から度数法に変換する。'''
 def __init__(
self,
angle:Typenumberlike|Deg|Rad
)->None:...
class Deg:
 '''度数法から弧度法に変換する。'''
 def __init__(
self,
angle:Typenumberlike|Deg|Rad
)->None:...