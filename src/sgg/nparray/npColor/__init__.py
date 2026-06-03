'''
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,カラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
'''
from matplotlib.colors import to_hex
from numpy import array,concatenate,issubdtype,ndarray,nditer,str_
from ..npStr import NPString
from ._color_check import check
from .data import Get_color
__all__=['NPColor']
class NPColor:
 def __init__(self,color):
  if isinstance(color,str):data=self._colormake(color)
  elif isinstance(color,list|tuple):data=[self._colormake(i)for i in color]
  elif isinstance(color,ndarray):
   if not issubdtype(color.dtype,str_|str):
    raise TypeError('ndarrayのdtypeにはstr_型もしくはstr型を指定してください')
   data=[self._colormake(i)for i in nditer(color)]
  else:
   raise TypeError('指定された型が正しくありせん')
  self.data=NPString(data).data
 def __repr__(self):return f'NPColor({self.data})'
 def _colormake(self,color):
  if not isinstance(color,str):
   raise TypeError('colorにはstr型で指定してください')
  colorname=Get_color.gets(color)
  if colorname is None:
   check_Color=check(color)
   if check_Color is None:
    raise ValueError('指定された色が不正確です')
   return concatenate((array(['-',to_hex(check_Color/255)],dtype=str_),check_Color.astype(str_)))
  else:
   return colorname