'''
色データを保管,色データを取得するモジュール

color.csvはhttps://drafts.csswg.org/css-color-4/#named-colorsを元に作成
'''
from types import NotImplementedType
from typing import Any,Literal
from numpy import dtype,ndarray,str_,ufunc
from ...base import NPArray
__all__=['Get_color']
class Get_color(NPArray):
 '''色データのcsvファイルのデータを取得する。'''
 data:ndarray[Any,dtype[str_]]
 def __init__(self)->None:'''色データのcsvファイルのデータを取得する。

 :param target: 取得するファイルを指定する。
 :type target: Literal['color.csv','css_color.csv','xkcd_color.csv']|None'''
 def __repr__(self)->str:...
 def __array_ufunc__(
self,
ufunc:ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args:Any,
**kwargs:Any
)->Any|NotImplementedType|Get_color:...
 @staticmethod
 def gets(colorname:str)->Any|None:...