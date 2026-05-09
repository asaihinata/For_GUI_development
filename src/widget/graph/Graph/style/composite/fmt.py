from typing import Literal
__all__=['FMT','FMT_COLOR','FMT_MARKER','FMT_SOLID']
FMT_COLOR=['b','g','r','c','m','y','k','w']
FMT_MARKER=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_']
FMT_SOLID=['-','--','-.',':']
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
  if marker in FMT_MARKER:self.marker=marker
  else:self.marker=''
  if solid in FMT_SOLID:self.solid=solid
  else:self.solid=''
  if color in FMT_COLOR:self.color=color
  else:self.color=''
  self.fmt_txt=f'{self.marker}{self.solid}{self.color}'
 def __str__(self)->str:return self.fmt_txt