'''
色データを保管,色データを取得するモジュール

color.csvはhttps://drafts.csswg.org/css-color-4/#named-colorsを元に作成
'''
from pathlib import Path
import numpy as np
from polars import read_csv
from ...base import NPArray
__all__=['Get_color']
class Get_color(NPArray):
 '''色データのcsvファイルのデータを取得する。'''
 def __init__(self):
  colordata=read_csv(Path(__file__).parent/'color.csv',encoding='utf-8-sig',has_header=True).to_numpy()
  super().__init__(colordata,dtype=np.str_)
 def __repr__(self):return f'Get_color({self.data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,Get_color) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,np.ndarray):return Get_color(result)
   return result
  return NotImplemented
 @staticmethod
 def gets(colorname):
  data=Get_color().data
  c,_=np.where(colorname==data)
  if c.size==0:return None
  return data[c][0]