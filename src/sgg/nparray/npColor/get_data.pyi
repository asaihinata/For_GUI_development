'''
色データを保管,色データを取得するモジュール


css_color.csv

https://drafts.csswg.org/css-color-4/#named-colors

xkcd_color.csv

https://xkcd.com/color/rgb.txt
'''
from types import NotImplementedType
from typing import Any,Literal,overload
from numpy import dtype,ndarray,str_,ufunc
from ..base import NPArray
__all__=['Get_color']
class Get_color(NPArray):
 '''色データのcsvファイルのデータを取得する。'''
 data:ndarray[Any,dtype[str_]]
 @overload
 def __init__(
self,
target:Literal[
'color.csv',
'css_color.csv',
'xkcd_color.csv'
]|None=None
)->None:'''色データのcsvファイルのデータを取得する。

 :param target: 取得するファイルを指定する。
 :type target: Literal['color.csv','css_color.csv','xkcd_color.csv']|None'''
 @overload
 def __init__(
self,
target:Literal[
'color.csv',
'css_color.csv',
'xkcd_color.csv'
]|None='color.csv'
)->None:'''color.csvファイルのデータを取得する。

 :param target: 取得するファイルを指定する。
 :type target: Literal['color.csv','css_color.csv','xkcd_color.csv']|None'''
 @overload
 def __init__(
self,
target:Literal[
'color.csv',
'css_color.csv',
'xkcd_color.csv'
]|None='css_color.csv'
)->None:'''css_color.csvファイルのデータを取得する。

 :param target: 取得するファイルを指定する。
 :type target: Literal['color.csv','css_color.csv','xkcd_color.csv']|None'''
 @overload
 def __init__(
self,
target:Literal[
'color.csv',
'css_color.csv',
'xkcd_color.csv'
]|None='xkcd_color.csv'
)->None:'''xkcd_color.csvファイルのデータを取得する。

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
 def gets(self,colorname:str)->Any|None:...