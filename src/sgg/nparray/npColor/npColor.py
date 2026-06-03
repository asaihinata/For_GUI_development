import numpy as np
from matplotlib.colors import to_hex
from ..npStr import NPString
from ._color_check import check
from .data import Get_color
__all__=['NPColor']
class NPColor:
 def __init__(self,color):
  if isinstance(color,str):data=self._colormake(color)
  self.data=NPString(data).data
 def __repr__(self):return f'NPColor({self.data})'
 def _colormake(self,color):
  colorname=Get_color.gets(color)
  if colorname is None:
   check_Color=check(color)
   if check_Color is None:
    raise ValueError('指定された色が不正確です')
   return np.concatenate((np.array(['-',to_hex(check_Color/255)],dtype=np.str_),check_Color.astype(np.str_)))
  else:
   return colorname