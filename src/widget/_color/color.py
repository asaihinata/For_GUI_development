import re
import numpy as np
from matplotlib.colors import to_hex
from ._color_data import COLOR_DATA,ColorData
__all__=['Color','COLOR_DATA','ColorData']
HEX8_RE=re.compile(r'^#[0-9a-f]{8}$')
HEX6_RE=re.compile(r'^#[0-9a-f]{6}$')
HEX3_RE=re.compile(r'^#[0-9a-f]{3}$')
RGB_RE=re.compile(r'^rgb\((\d+),(\d+),(\d+)\)$')
RGBA_RE=re.compile(r'^rgba\((\d+),(\d+),(\d+),([0-9.]+)\)$')
HSV_RE=re.compile(r'^hsv\((\d+),(\d+),(\d+)\)$')
class Color:
 '''16進数カラーコード,カラー名,rgb,rgba,hsvを16進数カラーコードに変換する。'''
 def __init__(self,color,keep_alpha=True)->None:
  if not isinstance(keep_alpha,bool):self.keep_alpha=True
  else:self.keep_alpha=keep_alpha
  self.color=to_hex(self._res(color)/255,self.keep_alpha)
 def _res(self,color):
  def chagehex6(val):
   val=val[0][1:]
   return np.fromiter((int(val[i:i+2],16)for i in range(0,len(val),2)),dtype=np.int16)
  def chagehex3(val):
   def sets(t):return f'{t}{t}'
   val=val[0][1:]
   return np.fromiter((int(sets(val[i:i+1]),16)for i in range(0,len(val))),dtype=np.int16)
  def chage(val):return np.array(val[0],np.int8)
  if isinstance(color,str):
   if color[0]=='#':
    if HEX8_RE.match(color):color=chagehex6(re.findall(HEX8_RE,color))
    elif HEX6_RE.match(color):color=chagehex6(re.findall(HEX6_RE,color))
    elif HEX3_RE.match(color):color=chagehex3(re.findall(HEX3_RE,color))
    return color
   elif RGB_RE.match(color):color=chage(re.findall(RGB_RE,color))
   elif RGBA_RE.match(color):color=chage(re.findall(RGBA_RE,color))
   elif HSV_RE.match(color):color=chage(re.findall(HSV_RE,color))
   else:return self._res(ColorData.get(color)[1])
  return color