'''
色データを保管,色データを取得するモジュール

color.csvはhttps://drafts.csswg.org/css-color-4/#named-colorsを元に作成
'''
from pathlib import Path
from types import NotImplementedType
from typing import Any,Literal
from numpy import ndarray,str_,ufunc,where
from ...readfile import Getcsv
from ..npArray import NPArray
__all__=['Get_color']
class Get_color(NPArray):
 '''色データを取得する。'''
 def __init__(self)->None:
  '''色データを取得する。'''
  colordata=Getcsv(Path(__file__).parent/'data/color.csv').get_numpy()
  super().__init__(colordata,dtype=str_)
 def __repr__(self)->str:return f'Get_color({self.data})'
 def __array_ufunc__(
self,
ufunc:ufunc,
method:Literal['__call__','reduce','reduceat','accumulate','outer','at'],
*args,
**kwargs
)->Any|NotImplementedType|Get_color:
  if method=='__call__':
   args=[x.data if isinstance(x,Get_color) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,ndarray):return Get_color(result)
   return result
  return NotImplemented
 def gets(self,colorname:str)->Any|None:
  c,_=where(colorname==self.data)
  if c.size==0:return None
  return self.data[c][0]