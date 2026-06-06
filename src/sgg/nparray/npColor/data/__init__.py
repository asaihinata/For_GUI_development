'''
色データを保管,色データを取得するモジュール

color.csvはhttps://drafts.csswg.org/css-color-4/#named-colorsを元に作成
'''
from pathlib import Path
from numpy import ndarray,str_,where
from polars import read_csv
from ...npArray import NPArray
__all__=['Get_color']
class Get_color(NPArray):
 '''色データのcsvファイルのデータを取得する。'''
 def __init__(self):
  colordata=read_csv(Path(__file__).parent/'color.csv',encoding='utf-8-sig',has_header=True).to_numpy()
  super().__init__(colordata,dtype=str_)
 def __repr__(self):return f'Get_color({self.__data})'
 def __array_ufunc__(self,ufunc,method,*args,**kwargs):
  if method=='__call__':
   args=[x.data if isinstance(x,Get_color) else x for x in args]
   result=ufunc(*args,**kwargs)
   if isinstance(result,ndarray):return Get_color(result)
   return result
  return NotImplemented
 @staticmethod
 def gets(colorname):
  data=Get_color().data
  c,_=where(colorname==data)
  if c.size==0:return None
  return data[c][0]