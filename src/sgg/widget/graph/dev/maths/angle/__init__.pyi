from ....typing import Type_Numberlike,overload
__all__=['Angle','Deg','Rad']
class Angle:
 angle:float
 @overload
 def __init__(
self,
angle:Type_Numberlike,
dtype:bool=...
)->None:'''度数法と弧度法の変換するクラス。

 :param angle: 変換したい角度を指定する。
 :type angle: Type_Numberlike
 :param dtype: 弧度法から度数法に変換するか,度数法から弧度法に変換するか指定する。
 :type dtype: bool
 :raises TypeError: `angle`に数値の型を指定しなかった場合に発生させる'''
 @overload
 def __init__(
self,
angle:Type_Numberlike,
dtype:bool=True
)->None:'''弧度法から度数法に変換する。

 :param angle: 変換したい角度を指定する。
 :type angle: Type_Numberlike
 :param dtype: 弧度法から度数法に変換するか,度数法から弧度法に変換するか指定する。
 :type dtype: bool
 :raises TypeError: `angle`に数値の型を指定しなかった場合に発生させる'''
 @overload
 def __init__(
self,
angle:Type_Numberlike,
dtype:bool=False
)->None:'''度数法から弧度法に変換する。

 :param angle: 変換したい角度を指定する。
 :type angle: Type_Numberlike
 :param dtype: 弧度法から度数法に変換するか,度数法から弧度法に変換するか指定する。
 :type dtype: bool
 :raises TypeError: `angle`に数値の型を指定しなかった場合に発生させる'''
 @classmethod
 def __instancecheck__(cls,ins)->bool:...
 def __str__(self)->str:...
 def __int__(self)->int:...
 def __float__(self)->float:...
 def __eq__(self,val:Type_Numberlike)->bool:...
 def __ne__(self,val:Type_Numberlike)->bool:...
 def __lt__(self,val:Type_Numberlike)->bool:...
 def __le__(self,val:Type_Numberlike)->bool:...
 def __gt__(self,val:Type_Numberlike)->bool:...
 def __ge__(self,val:Type_Numberlike)->bool:...
class Rad(Angle):
 '''弧度法から度数法に変換する。'''
 angle:float
 def __init__(
self,
angle:Type_Numberlike|Deg|Rad
)->None:...
class Deg(Angle):
 angle:float
 '''度数法から弧度法に変換する。'''
 def __init__(
self,
angle:Type_Numberlike|Deg|Rad
)->None:...