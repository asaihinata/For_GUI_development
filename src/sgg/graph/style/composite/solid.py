'''グラフの線を設定するモジュール'''
from collections.abc import Iterator
from typing import Any,Literal
from ...typing import Type_Solid
from ..fmt import FMT
__all__=['Solid']
class Solid:
 solid_list:list[str]=['-','--','-.',':','None',' ','']
 def __init__(
self,
solid:Type_Solid|None=None,
fmtmarker:Literal[
'.',',','o',
'v','^','<',
'>','1','2',
'3','4','8',
's','p','P',
'*','h','H',
'+','x','X',
'D','d','|',
'_']|None=None,
fmtsolid:Literal['-','--','-.',':']|None=None,
fmtcolor:Literal['b','g','r','c','m','y','k','w']|None=None
)->None:
  if solid in self.solid_list:
   self.solid=solid
  elif (fmtmarker is not None) or (fmtmarker is not None) or (fmtcolor is not None):
   self.solid=FMT(fmtmarker,fmtsolid,fmtcolor).fmt_txt
  else:
   self.solid='-'
 def __str__(self)->str:return self.solid
 def __iter__(self)->Iterator[str]:return iter(self.solid_list)
 def __len__(self)->int:return len(self.solid_list)
 def __contains__(self,item:Any)->bool:return item in self.solid_list