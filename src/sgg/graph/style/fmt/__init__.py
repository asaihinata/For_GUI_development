'''マーカー,線種,色を一度に設定するモジュール'''
import numpy as np
from .constants import FMT_COLOR,FMT_MARKER,FMT_SOLID
__all__=['FMT','fmtstyle']
class FMT:
 def __init__(self,marker=None,solid=None,color=None):
  self.__txt=f'{marker if marker in FMT_MARKER else ''}{solid if solid in FMT_SOLID else ''}{color if color in FMT_COLOR else ''}'
 def __str__(self):return self.__txt
 @property
 def txt(self):return self.__txt
class fmtstyle:
 def __init__(self,arr,style='color'):
  style=style.lower()
  if style=='marker':style=FMT_MARKER
  elif style=='solid':style=FMT_SOLID
  else:style=FMT_COLOR
  if isinstance(arr,str):self.__arr=np.array([arr])
  elif isinstance(arr,list|tuple):self.__arr=np.array(arr)
  else:self.__arr=arr
  self.__arr=np.array([i if i in style else '' for i in np.nditer(self.__arr)])
 def __iter__(self):return iter(self.__arr)
 @property
 def arr(self):return self.__arr