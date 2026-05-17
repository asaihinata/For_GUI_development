'''マーカー,線種,色を一度に設定するモジュール'''
from typing import Literal
from ._data import FMT_COLOR,FMT_MARKER,FMT_SOLID
__all__=['FMT']
class FMT:
 fmt_txt:str
 def __init__(
self,
marker:Literal[
'.',',','o',
'v','^','<',
'>','1','2',
'3','4','8',
's','p','P',
'*','h','H',
'+','x','X',
'D','d','|','_']|None=None,
solid:Literal['-','--','-.',':']|None=None,
color:Literal['b','g','r','c','m','y','k','w']|None=None
)->None:
  self.fmt_txt=f'{marker if marker in FMT_MARKER else ''}{solid if solid in FMT_SOLID else ''}{color if color in FMT_COLOR else ''}'
 def __str__(self)->str:return self.fmt_txt