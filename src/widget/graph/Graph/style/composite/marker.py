from collections.abc import Iterator
from typing import Literal
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D
__all__=['Marker']
class Marker:
 marker_list=list(MarkerStyle.markers.keys())
 def __init__(
self,
marker,
fill:Literal['full','left','right','bottom','top','none']|None=None,
cap:Literal['butt','round','projecting']|None=None,
transform:int|float|None=None,
join:Literal['miter','round','bevel']|None=None
)->None:
  if fill not in ['full','left','right','bottom','top','none']:fill=None
  if cap not in ['butt','round','projecting']:cap=None
  if join not in ['miter','round','bevel']:join=None
  if not isinstance(transform,int|float):transform=0
  self.marker=MarkerStyle(marker,fillstyle=fill,transform=Affine2D().rotate_deg(transform),joinstyle=join,capstyle=cap)
 def __iter__(self)->Iterator[int|str]:return iter(self.marker_list)
 def __len__(self)->int:return len(self.marker_list)
 def __contains__(self,item:str)->bool:return item in self.marker_list
 def get_marker(self):return self.marker.get_marker()