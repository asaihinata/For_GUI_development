'''matplotlib.text.Textに使用するbbox'''
from typing import Any
from matplotlib import rcParams
from matplotlib._enums import CapStyle,JoinStyle
from ..dev import bols,range_zero_one
from ..tool import Color
from ..typing import Type_Color,Type_Numberlike,Type_Solid
from .solid import Solid
__all__=['BBox']
class BBox:
 bbox_dict:dict[str,Any]
 def __init__(
self,*,
alpha:Type_Numberlike=1,
edgecolor:Type_Color|None=None,
facecolor:Type_Color|None=None,
color:Type_Color|None=None,
linewidth:Type_Numberlike=2,
linestyle:Type_Solid='solid',
antialiased:bool=True,
hatch:bool=None,
fill:bool=True,
capstyle:CapStyle|str=CapStyle.butt,
joinstyle:JoinStyle|str=JoinStyle.miter,
hatch_linewidth:int|float=None,
in_layout:bool=True,
mouseover:bool=True,
rasterized:bool=False,
visible:bool=True,
zorder:int|float=4
):
  self.alpha=range_zero_one(alpha,1.0)
  self.edgecolor=bols(edgecolor is not None,Color(edgecolor).color[0])
  self.facecolor=bols(facecolor is not None,Color(facecolor).color[0])
  self.color=bols(color is not None,Color(color).color[0])
  self.linewidth=bols(isinstance(linewidth,int|float),linewidth,2)
  self.linestyle=bols(linestyle in Solid(),linestyle,'solid')
  self.antialiased=bols(isinstance(antialiased,bool),antialiased)
  self.hatch=bols(isinstance(hatch,bool),hatch)
  self.fill=bols(isinstance(fill,bool),fill)
  self.capstyle=bols(isinstance(capstyle,CapStyle) or capstyle in ['butt','projecting','round'],capstyle,CapStyle.butt)
  self.joinstyle=bols(isinstance(joinstyle,JoinStyle) or joinstyle in ['miter','round','bevel'],joinstyle,JoinStyle.miter)
  self.hatch_linewidth=bols(isinstance(hatch_linewidth,int|float),hatch_linewidth,rcParams['hatch.linewidth'])
  self.in_layout=bols(isinstance(in_layout,bool),in_layout,True)
  self.mouseover=bols(isinstance(mouseover,bool),mouseover,True)
  self.rasterized=bols(isinstance(rasterized,bool),rasterized,False)
  self.visible=bols(isinstance(visible,bool),visible,True)
  self.zorder=bols(isinstance(zorder,int|float),zorder,4)
  self.bbox_dict={
'alpha':self.alpha,
'edgecolor':self.edgecolor,
'facecolor':self.facecolor,
'color':self.color,
'linewidth':self.linewidth,
'linestyle':self.linestyle,
'antialiased':self.antialiased,
'hatch':self.hatch,
'fill':self.fill,
'capstyle':self.capstyle,
'joinstyle':self.joinstyle,
'hatch_linewidth':self.hatch_linewidth,
'in_layout':self.in_layout,
'mouseover':self.mouseover,
'rasterized':self.rasterized,
'visible':self.visible,
'zorder':self.zorder}
 def get_bbox(self)->dict[str,Any]:return self.bbox_dict