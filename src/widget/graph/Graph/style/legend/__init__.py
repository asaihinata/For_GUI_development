import numpy as np
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D

from .....developer import Number
from ..developer import *
from ..tool import Color

__all__=['Legends']
LOC={
'best':0,'upper right':1,'upper left':2,
'lower left':3,'lower right':4,'right':5,
'center left':6,'center right':7,'lower center':8,
'upper center':9,'center':10
}
class Legends:
 def __init__(
self,ax,handles,labels,
loc=None,numpoints=None,markerscale=None,
markerfirst=True,reverse=False,
scatterpoints=None,
scatteryoffsets=None,
prop=None,fontsize=None,labelcolor=None,
borderpad=None,labelspacing=None,
handlelength=None,
handleheight=None,
handletextpad=None,
borderaxespad=None,
columnspacing=None,
ncols=1,mode=None,fancybox=None,
shadow=None,title=None,
title_fontsize=None,framealpha=None,edgecolor=None,
facecolor=None,bbox_to_anchor=None,
bbox_transform=None,
frameon=None,handler_map=None,
title_fontproperties=None,
alignment='center',ncol=1,draggable=False
):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  if(
     (isinstance(loc,str) and loc in LOC.keys()) or
     (isinstance(loc,list|tuple) and list2float(loc)) or
     (isinstance(loc,int) and 0<=loc<=10)
    ):loc=loc
  else:loc='best'
  if numpoints is not None and isinstance(numpoints,int|float|Number) and numpoints<=0:
   numpoints=1
  labelcolor=np.array(Color(labelcolor))
  self.ax.legend(
handles=handles,labels=labels,loc=loc,
numpoints=numpoints,reverse=reverse,
markerscale=markerscale,
markerfirst=markerfirst,
scatterpoints=scatterpoints,
scatteryoffsets=scatteryoffsets,
prop=prop,fontsize=fontsize,
labelcolor=labelcolor,
borderpad=borderpad,
labelspacing=labelspacing,
handlelength=handlelength,
handleheight=handleheight,
handletextpad=handletextpad,
borderaxespad=borderaxespad,
columnspacing=columnspacing,
ncols=ncols,mode=mode,fancybox=fancybox,
shadow=shadow,title=title,
title_fontsize=title_fontsize,ncol=ncol,
framealpha=framealpha,
edgecolor=edgecolor,facecolor=facecolor,
bbox_to_anchor=bbox_to_anchor,
bbox_transform=bbox_transform,
frameon=frameon,handler_map=handler_map,
title_fontproperties=title_fontproperties,
alignment=alignment,draggable=draggable
)
