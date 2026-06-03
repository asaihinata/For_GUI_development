'''
色データを保管,色データを取得するモジュール


css_color.csv

https://drafts.csswg.org/css-color-4/#named-colors

xkcd_color.csv

https://xkcd.com/color/rgb.txt
'''
from pathlib import Path
import numpy as np
from polars import read_csv
from ..base import NPArray
__all__=['Get_color']
class Get_color(NPArray):
 '''色データのcsvファイルのデータを取得する。'''
 def __init__(self,target=None):
  if target not in ['color.csv','css_color.csv','xkcd_color.csv']:target='color.csv'
  colordata=read_csv(Path(__file__).parent/'data'/target,encoding='utf-8-sig',has_header=True).to_numpy().astype(np.str_)
  super().__init__(colordata,dtype=np.str_,depth_limit=2)
 def __repr__(self):return f'Get_color({self.data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,Get_color) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return Get_color(result)
   return result
  return NotImplemented
 def gets(self,colorname):
  c,_=np.where(colorname==self.data)
  if c.size==0:return None
  return self.data[c][0]