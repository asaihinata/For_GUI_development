'''マーカーを設定するモジュール'''
from collections.abc import Iterator
from typing import Any,Literal
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from matplotlib.transforms import Affine2D
from numpy.typing import ArrayLike
from ....typing import Type_Marker,Type_Number,Type_NumberandNone,marKer
__all__=['Marker']
class Marker:
 marker_dict:dict[int|str,str]={'.':'point',',':'pixel','o':'circle','v':'triangle_down','^':'triangle_up','<':'triangle_left','>':'triangle_right','1':'tri_down','2':'tri_up','3':'tri_left','4':'tri_right','8':'octagon','s':'square','p':'pentagon','*':'star','h':'hexagon1','H':'hexagon2','+':'plus','x':'x','D':'diamond','d':'thin_diamond','|':'vline','_':'hline','P':'plus_filled','X':'x_filled',0:'tickleft',1:'tickright',2:'tickup',3:'tickdown',4:'caretleft',5:'caretright',6:'caretup',7:'caretdown',8:'caretleftbase',9:'caretrightbase',10:'caretupbase',11:'caretdownbase','None':'nothing','none':'nothing',' ':'nothing','':'nothing'}
 marker_list:list[int|str]=marKer
 marker:MarkerStyle
 def __init__(
self,
marker:str|int|Type_Marker,
*,
fill:Literal['full','left','right','bottom','top','none']|None=None,
cap:Literal['butt','round','projecting']|None=None,
transform:Type_NumberandNone=None,
join:Literal['miter','round','bevel']|None=None
)->None:
  if fill not in ['full','left','right','bottom','top','none']:fill=None
  if cap not in ['butt','round','projecting']:cap=None
  if join not in ['miter','round','bevel']:join=None
  if not isinstance(transform,Type_Number):transform=0
  self.marker=MarkerStyle(marker,fillstyle=fill,transform=Affine2D().rotate_deg(transform),joinstyle=join,capstyle=cap)
 def __iter__(self)->Iterator[int|str]:return iter(self.marker_list)
 def __len__(self)->int:return len(self.marker_list)
 def __contains__(self,item:Any)->bool:return item in self.marker_list
 def get_marker(self)->str|ArrayLike|Path|None:return self.marker.get_marker()