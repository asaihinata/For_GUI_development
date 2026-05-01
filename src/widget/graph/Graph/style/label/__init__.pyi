from typing import Literal
from matplotlib.text import Text
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from .....developer import Number
class Xlabel:
 def __init__(
self,
ax:Axes|Axes3D,
text:str=...,
labelpad:int|float|Number|None=4,
loc:Literal['center','left','right']|None='center',
**kwargs:Text
)->None:...
 def __str__(self)->str:...
class Ylabel:
 def __init__(
self,
ax:Axes|Axes3D,
text:str=...,
labelpad:int|float|Number|None=4,
loc:Literal['center','left','right']|None='center',
**kwargs:Text
)->None:...
 def __str__(self)->str:...
class Zlabel:
 def __init__(
self,
ax:Axes3D,
text:str=...,
labelpad:int|float|Number|None=4,
loc:Literal['center','left','right']|None='center',
**kwargs:Text
)->None:...
 def __str__(self)->str:...