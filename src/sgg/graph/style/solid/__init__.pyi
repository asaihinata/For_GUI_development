'''グラフの線を設定するモジュール'''
from typing import Literal
from ....nparray import NPString
from ...typing import Type_Solid
__all__=['Solid','Solidlist','fmtSolid']
class Solid:
 stlye=['-','--','-.',':','None',' ','']
 solid:str
 def __init__(
self,
solid:Type_Solid='-',
)->None:...
class Solidlist(NPString):
 data:NPString
 def __init__(
self,
solid:Type_Solid='-',
)->None:...
 def __iter__(self):...
 def __getitem__(self,key:int):...
class fmtSolid:
 solid:str
 def __init__(
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
)->None:...