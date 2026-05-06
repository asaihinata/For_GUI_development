from os.path import join
from pathlib import Path
from re import compile, findall

from numpy import ndarray, where
from polars import read_csv

__all__=['Color','COLOR_DATA']
COLOR_DATA:ndarray=read_csv(join(Path(__file__).parent,'color.csv'),encoding='utf-8-sig',has_header=False).to_numpy()
HEX6_RE=compile(r'^#[0-9a-f]{6}$')
HEX3_RE=compile(r'^#[0-9a-f]{3}$')
RGB_RE=compile(r'^rgb\((\d+),(\d+),(\d+)\)$')
RGBA_RE=compile(r'^rgba\((\d+),(\d+),(\d+),([0-9.]+)\)$')
HSV_RE=compile(r'^hsv\((\d+),(\d+),(\d+)\)$')
class Color:
 '''16進数カラーコード,カラー名,rgb,rgba,hsvを16進数カラーコードに変換する。'''
 def __init__(self,color:str,other:str|None=None)->None:
  '''colorで指定した16進数カラーコード,カラー名,rgb,rgba,hsvを16進数カラーコードに変換する。

 :param color: 16進数カラーコード,カラー名,rgb,rgba,hsvを16進数カラーコードを指定する。
 :type color: str
 :param other: colorを16進数カラーコードに変換する際,何らかの例外が発生した際に返す値を指定する。
 :type other: str|None'''
  self.txt=self._color(color,other)
 def _color(self,color,other):
  if isinstance(color,str):
   c=color.strip().lower()
   if where(c in COLOR_DATA,True,False):return COLOR_DATA[where(c==COLOR_DATA)[0]][0][1]
   elif c[0]=='#' and HEX6_RE.match(c):return c
   elif c[0]=='#' and HEX3_RE.match(c):return f'#{''.join([i*2 for i in findall(r'[0-9a-fA-F]',c)])}'
   rgb_match=RGB_RE.match(c)
   if rgb_match:
    r,g,b=int(rgb_match.group(1)),int(rgb_match.group(2)),int(rgb_match.group(3))
    if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:return '#{:02x}{:02x}{:02x}'.format(r,g,b)
   rgba_match=RGBA_RE.match(c)
   if rgba_match:
    r,g,b=int(rgba_match.group(1)),int(rgba_match.group(2)),int(rgba_match.group(3))
    if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:return '#{:02x}{:02x}{:02x}'.format(r,g,b)
   hsv_match=HSV_RE.match(c)
   if hsv_match:
    h,s,v=int(hsv_match.group(1)),int(hsv_match.group(2)),int(hsv_match.group(3))
    if 0<=h<=360 and 0<=s<=100 and 0<=v<=100:
     r,g,b=self._hr(h/360,s/100,v/100)
     return '#{:02x}{:02x}{:02x}'.format(int(r*255),int(g*255),int(b*255))
   return other
  else:return other
 def _hr(self,h,s,v):
  if s==0:return v,v,v
  i=int(h*6)
  f=h*6-i
  p,q,t=v*(1-s),v*(1-s*f),v*(1-s*(1-f))
  i=i%6
  if i==0:return v,t,p
  elif i==1:return q,v,p
  elif i==2:return p,v,t
  elif i==3:return p,q,v
  elif i==4:return t,p,v
  else:return v,p,q
 def __str__(self):return str(self.txt)