'''マーカーを設定するモジュール'''
from collections.abc import Iterator
from typing import Any,Literal
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from numpy.typing import ArrayLike
from ....typing import Type_Marker,Type_NumberlikeN
__all__=['Marker']
class Marker:
 marker_dict:dict[int|str,str]
 marker_list:list[int|str]
 marker:MarkerStyle
 def __init__(
self,
marker:str|int|Type_Marker,
*,
fill:Literal['full','left','right','bottom','top','none']|None=None,
cap:Literal['butt','round','projecting']|None=None,
transform:Type_NumberlikeN=None,
join:Literal['miter','round','bevel']|None=None
)->None:...
 def __iter__(self)->Iterator[int|str]:...
 def __len__(self)->int:...
 def __contains__(self,item:Any)->bool:...
 def get_marker(self)->str|ArrayLike|Path|None:...