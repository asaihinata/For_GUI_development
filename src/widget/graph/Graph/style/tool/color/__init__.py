import numpy as np
from matplotlib.colors import cnames,to_hex,to_rgb,to_rgba
__all__=['Color']
class Color:
 def __init__(self,color,keep_alpha=False):
  if not isinstance(keep_alpha,bool):keep_alpha=False
  else:keep_alpha=keep_alpha
  if isinstance(color,list|tuple):colors=np.array(color)
  elif isinstance(color,str):colors=np.array([color.lower()])
  elif isinstance(color,np.ndarray):colors=color
  else:colors=None
  self.color=np.array(['#000000' if i is None else to_hex(i,keep_alpha) for i in colors],dtype=str)
 def tohex(self,keep_alpha=False):
  if not isinstance(keep_alpha,bool):keep_alpha=False
  else:keep_alpha=keep_alpha
  self.color=np.array(['#000000' if i is None else to_hex(i,keep_alpha) for i in self.color],dtype=str)
  return self
 def torgba(self,alpha=None):
  if alpha is not None:
   if not isinstance(alpha,int|float):
    raise TypeError('alphaは数値の型を指定してください')
   if not 0.0<=alpha<=1.0:
    raise ValueError('0.0<=alpha<=1.0の範囲で指定してください')
  self.color=np.array([to_rgba(i,alpha) for i in self.color],dtype=float)
  return self
 def torgb(self):
  self.color=np.array([to_rgb(i) for i in self.color],dtype=float)
  return self
 def __iter__(self):return iter(self.color)
 def __contains__(self,val):return val in self.color
 def __len__(self):return self.color.size
 def __getitem__(self,val):
  if isinstance(val,int):
   if 0<=val<len(self):return self.color[val]
   raise IndexError('配列の範囲外です')
  elif isinstance(val,slice):return self.color[val]
  raise TypeError('リストのインデックスはintまたはslicesである必要があります')
 @classmethod
 def colorname(cls):return list(cnames)
 @classmethod
 def colorhex(cls):return list(cnames.values())