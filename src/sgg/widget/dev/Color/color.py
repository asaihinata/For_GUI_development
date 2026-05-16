from re import compile,findall
import numpy as np
from matplotlib.colors import to_hex,to_rgb,to_rgba
from .colorlist import ColorData
from ...typing import Type_Numberlike
__all__=['Colors']
HEX8_RE=compile(r'^#[0-9a-f]{8}$')
HEX6_RE=compile(r'^#[0-9a-f]{6}$')
HEX3_RE=compile(r'^#[0-9a-f]{3}$')
RGB_RE=compile(r'^rgb\((\d+),(\d+),(\d+)\)$')
RGBA_RE=compile(r'^rgba\((\d+),(\d+),(\d+),([0-9.]+)\)$')
HSV_RE=compile(r'^hsv\((\d+),(\d+),(\d+)\)$')
class Colors:
 def __init__(self,color,ranges=True,keep_alpha=True):
  if isinstance(color,Colors):color=color.color
  if isinstance(keep_alpha,bool):self.keep_alpha=keep_alpha
  else:self.keep_alpha=True
  if isinstance(ranges,bool):self.ranges=ranges
  else:self.ranges=True
  cons=self._res(color)
  if self.ranges:cons=cons/255
  self.color=to_hex(cons,self.keep_alpha)
 def tohex(self,keep_alpha=None):
  if not isinstance(keep_alpha,bool):keep_alpha=self.keep_alpha
  return to_hex(self.color,keep_alpha)
 def torgba(self,alpha=None):return to_rgba(self.color,alpha)
 def torgb(self):return to_rgb(self.color)
 def chagehex6(self,val):
  val=val[0][1:]
  return np.fromiter((int(val[i:i+2],16)for i in range(0,len(val),2)),dtype=np.int16)
 def chagehex3(self,val):
  def sets(t):return f'{t}{t}'
  val=val[0][1:]
  return np.fromiter((int(sets(val[i:i+1]),16)for i in range(0,len(val))),dtype=np.int16)
 def chage(self,val):return np.array(val[0],np.int8)
 def _res(self,color):
  if isinstance(color,str):
   if color[0]=='#':
    if HEX8_RE.match(color):return self.chagehex6(findall(HEX8_RE,color))
    elif HEX6_RE.match(color):return self.chagehex6(findall(HEX6_RE,color))
    elif HEX3_RE.match(color):return self.chagehex3(findall(HEX3_RE,color))
   elif RGB_RE.match(color):return self.chage(findall(RGB_RE,color))
   elif RGBA_RE.match(color):return self.chage(findall(RGBA_RE,color))
   elif HSV_RE.match(color):return self.chage(findall(HSV_RE,color))
   elif np.where(color in ColorData(),True,False):return self._res(ColorData()[int(np.where(color==ColorData())[0][0])][1])
  elif isinstance(color,(list,tuple)):
   if not all((isinstance(i,Type_Numberlike))for i in color):
    raise TypeError('配列内に数値の型ではない要素が含まれています')
   elif self.ranges and not all(0<=i<=255 for i in color):
    raise ValueError('配列内に数値には0から255の範囲で指定してください')
   elif not self.ranges and not all(0<=i<=1.0 for i in color):
    raise ValueError('配列内に数値には0から1の範囲で指定してください')
   return np.array(color)
  elif isinstance(color,np.ndarray):
   if not all((isinstance(i,Type_Numberlike))for i in color):
    raise TypeError('配列内に数値の型ではない要素が含まれています')
   elif self.ranges and not all(0<=i<=255 for i in color):
    raise ValueError('配列内に数値には0から255の範囲で指定してください')
   elif not self.ranges and not all(0<=i<=1.0 for i in color):
    raise ValueError('配列内に数値には0から1の範囲で指定してください')
   return color
 def _lists(self,arr):
  lens=len(arr)
  if all((isinstance(i,Type_Numberlike) and 0<=i<=255) for i in arr) and (lens==3 or lens==4):return True
  return False