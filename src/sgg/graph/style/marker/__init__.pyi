'''マーカーを設定するモジュール'''
from typing import Any,Literal
from matplotlib.markers import MarkerStyle
from ....nparray import NPString
from ...typing import Type_Marker,Type_NumberlikeN
__all__=['Marker','MarkerList']
class Marker:
 marker_list:list[int|str]
 marker:MarkerStyle
 def __init__(
self,
marker:str|int|Type_Marker,
fill:Literal['full','left','right','bottom','top','none']|None=None,
cap:Literal['butt','round','projecting']|None=None,
transform:Type_NumberlikeN=None,
join:Literal['miter','round','bevel']|None=None
)->None:...
 def __contains__(self,item:Any)->bool:...
class MarkerList(NPString):
 data:NPString
 def __init__(
self,
marker:str|int|Type_Marker,
fill:Literal['full','left','right','bottom','top','none']|None=None,
cap:Literal['butt','round','projecting']|None=None,
transform:Type_NumberlikeN=None,
join:Literal['miter','round','bevel']|None=None
):...
 def __iter__(self):...