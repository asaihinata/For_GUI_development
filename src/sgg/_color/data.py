'''`data/color.csv`のデータを取得する。'''
from pathlib import Path
from typing import TypeAlias
import numpy as np
from ..readfile import Getcsv
List_like:TypeAlias=np.ndarray[str,str]
__all__=['COLOR_DATA','ColorData']
COLOR_DATA:List_like=Getcsv(Path(__file__).parent/'data/color.csv',has_header=False).get_numpy()
class ColorData:
 colorlist:List_like
 def __init__(self):self.colorlist:List_like=COLOR_DATA
 def __contains__(self,item)->bool:return np.where(item in self.colorlist,True,False)
 def __iter__(self):return iter(self.colorlist)
 def __len__(self)->int:return len(self.colorlist)
 def __getitem__(self,val):
  if isinstance(val,int):
   lens=len(self)
   if 0<=val<lens:return self.colorlist[val]
   elif val==lens:return self.colorlist[lens-1]
   raise IndexError('配列の範囲外です')
  elif isinstance(val,slice):return self.colorlist[val]
  raise TypeError('リストのインデックスはintまたはslicesである必要があります')
 @classmethod
 def get(cls,val):
  if isinstance(val,str):
   if np.where(val in COLOR_DATA,True,False):return COLOR_DATA[np.where(val==COLOR_DATA)[0]][0]
   else:
    raise ValueError('その色名は存在しません')
  elif isinstance(val,int|slice):return ColorData()[val]
  else:
   raise TypeError('valにはstr,int,sliceのどれかの型で指定してください')