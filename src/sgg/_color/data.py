from pathlib import Path
from numpy import where
from ..readfile import Getcsv
__all__=['Get_color']
class Get_color:
 '''色データを取得する'''
 colordata=Getcsv(Path(__file__).parent/'color.csv').get_numpy()
 @classmethod
 def gets(cls,colorname):
  cds=Get_color.colordata
  c,_=where(colorname==cds)
  if c.size==0:return None
  return cds[c][0]