'''塗りつぶし領域の領域内のマーカーを設定するモジュール'''
from re import compile

from ....nparray import NPString

__all__=['Hatch']
HATCH_LIST=['/','\\','|','-','+','x','o','O','.','*']
class Hatch(NPString):
 def __init__(self,hatch:str|tuple[str,...])->None:
  if hatch in ['',None]:hatch=['']
  elif isinstance(hatch,str):hatch=[hatch]
  super().__init__(hatch,depth_limit=1)
  prog=compile(r'^[/\\|\-+xo*O.]+$')
  for i in self.data:
   if i!='' and not prog.fullmatch(i):
    raise ValueError('指定できない値が含まれています')
 def __iter__(self):return iter(self.data)
 def __repr__(self):return f'Hatch({self.data})'
 def __getitem__(self,key):return self.get(key)