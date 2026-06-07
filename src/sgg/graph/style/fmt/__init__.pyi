'''マーカー,線種,色を一度に設定するモジュール'''
from collections.abc import Iterator
from typing import Literal as L,TypeAlias
import numpy as np
__all__=['FMT','fmtstyle']
MarkerType:TypeAlias=L[
'.',',','o',
'v','^','<',
'>','1','2',
'3','4','8',
's','p','P',
'*','h','H',
'+','x','X',
'D','d','|','_']
class FMT:
 def __init__(
self,
marker:MarkerType|None=None,
solid:L['-','--','-.',':']|None=None,
color:L['b','g','r','c','m','y','k','w']|None=None
)->None:...
 def __str__(self)->str:...
 @property
 def txt(self)->str:...
class fmtstyle:
 def __init__(
self,
arr:np.typing.ArrayLike,
style:L['color','marker','solid']='color'
)->None:...
 def __iter__(self)->Iterator[str]:...
 @property
 def arr(self)->np.ndarray:...