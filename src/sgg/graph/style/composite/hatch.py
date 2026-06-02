'''塗りつぶし領域の領域内のマーカーを設定するモジュール'''
from re import compile
import numpy as np
from ..dev import NPString
__all__=['Hatch']
HATCH_LIST=['/','\\','|','-','+','x','o','O','.','*']
class Hatch:
 def __init__(self,hatch:str|tuple[str,...])->None:
  if hatch in ['',None]:hatch=['']
  elif isinstance(hatch,str):hatch=[hatch]
  self.data=NPString(hatch,depth_limit=2,dtype=str)
  prog=compile(r'^[/\\|\-+xo*O.]+$')
  for i in self.data:
   if i!='' and not prog.fullmatch(i):
    raise ValueError('指定できない値が含まれています')
 def __iter__(self):return iter(self.data)
 def __repr__(self):return f'Hatch({self.data.data})'
 def __getitem__(self,key):return self.data.get(key)