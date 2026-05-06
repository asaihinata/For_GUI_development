from collections.abc import Iterable
from typing import Any, Literal

from matplotlib.artist import Artist
from matplotlib.axes._axes import Axes
from matplotlib.font_manager import FontProperties
from matplotlib.legend_handler import HandlerBase
from matplotlib.transforms import BboxBase, Transform
from matplotlib.typing import ColorType
from mpl_toolkits.mplot3d.axes3d import Axes3D

class Legends:
 def __init__(
self,
ax:Axes|Axes3D,
handles:Iterable[Artist|tuple[Artist,...]],
labels:Iterable[str],
loc:Literal[
'upper right','upper left','lower left',
'lower right','right','center left',
'center right','lower center','upper center',
'center']
|tuple[float,float]
|int
|None=None,
numpoints:int|None=None,
markerscale:float|None=None,
markerfirst:bool=True,
reverse:bool=False,
scatterpoints:int|None=None,
scatteryoffsets:Iterable[float]|None=None,
prop:FontProperties|dict[str,Any]|None=None,
fontsize:float|str|None=None,
labelcolor:ColorType
|Iterable[ColorType]
|Literal['linecolor','markerfacecolor','mfc','markeredgecolor','mec']
|None=None,
borderpad:float|None=None,
labelspacing:float|None=None,
handlelength:float|None=None,
handleheight:float|None=None,
handletextpad:float|None=None,
borderaxespad:float|None=None,
columnspacing:float|None=None,
ncols:int=1,
mode:Literal['expand']|None=None,
fancybox:bool|None=None,
shadow:bool|dict[str,Any]|None=None,
title:str|None=None,
title_fontsize:float|None=None,
framealpha:float|None=None,
edgecolor:Literal['inherit']
|ColorType|None=None,
facecolor:Literal['inherit']
|ColorType|None=None,
bbox_to_anchor:BboxBase
|tuple[float,float]
|tuple[float,float,float,float]
|None=None,
bbox_transform:Transform|None=None,
frameon:bool|None=None,
handler_map:dict[Artist|type,HandlerBase]|None=None,
title_fontproperties:FontProperties|dict[str,Any]|None=None,
alignment:Literal['center','left','right']='center',
ncol:int=1,
draggable:bool=False
)->None:...