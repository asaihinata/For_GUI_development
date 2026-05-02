from matplotlib.colors import cnames,to_hex,to_rgb,to_rgba
import numpy as np
__all__=['Color']
class Color:
 def __init__(self,color):
  if isinstance(color,(list,tuple)):colors=np.array(color)
  elif isinstance(color,np.ndarray):colors=color
  elif isinstance(color,str):colors=np.array([color])
  self.color=np.array([np.frompyfunc(to_rgba,1,1)(i) for i in colors])
 def tohex(self,keep_alpha=False):
  if not isinstance(keep_alpha,bool):keep_alpha=False
  else:keep_alpha=keep_alpha
  self.color=np.array([np.frompyfunc(to_hex,2,1)(i,keep_alpha) for i in self.color])
  return self
 def torgba(self,alpha=None):
  if alpha is not None:
   if not isinstance(alpha,(int,float)):
    raise TypeError('alphaは数値の型を指定してください')
   if not 0<=alpha<=1:
    raise ValueError('0.0<=alpha<=1.0の範囲で指定してください')
  self.color=np.array([np.frompyfunc(to_rgba,2,1)(i,alpha) for i in self.color])
  return self
 def torgb(self):
  self.color=np.array([np.frompyfunc(to_rgb,1,1)(i) for i in self.color])
  return self
 def __iter__(self):return iter(self.color)
 def __contains__(self,val):return val in self.color
 def __len__(self):return self.color.size
 @classmethod
 def colorname(cls):return list(cnames)
 @classmethod
 def colorhex(cls):return list(cnames.values())