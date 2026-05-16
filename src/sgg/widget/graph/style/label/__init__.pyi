from typing import Literal
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ...typing import ColorType,Type_NumberlikeN
class Xlabel:
 def __init__(
self,
ax:Axes|Axes3D,
text:str=...,
labelpad:Type_NumberlikeN=4,
color:ColorType=None,
ha:Literal['left','center','right']='center',
va:Literal['bottom','baseline','center','center_baseline','top']=None,
rotation:float|Literal['vertical','horizontal']|None='horizontal',
rotation_mode:bool=True,
angle:Literal['degree','radian']='degree',
alpha:float=1.0,
zorder:int|float=4
)->None:...
class Ylabel:
 def __init__(
self,
ax:Axes|Axes3D,
text:str=...,
labelpad:Type_NumberlikeN=4,
color:ColorType=None,
ha:Literal['left','center','right']='center',
va:Literal['bottom','baseline','center','center_baseline','top']=None,
rotation:float|Literal['vertical','horizontal']|None='horizontal',
rotation_mode:bool=True,
angle:Literal['degree','radian']='degree',
alpha:float=1.0,
zorder:int|float=4
)->None:...
class Zlabel:
 def __init__(
self,
ax:Axes3D,
text:str=...,
labelpad:Type_NumberlikeN=4,
color:ColorType=None,
ha:Literal['left','center','right']='center',
va:Literal['bottom','baseline','center','center_baseline','top']=None,
rotation:float|Literal['vertical','horizontal']|None='horizontal',
rotation_mode:bool=True,
angle:Literal['degree','radian']='degree',
alpha:float=1.0,
zorder:int|float=4
)->None:...