'''タイトルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ..developer import Rad,listchose,range_zero_one
__all__=['Title']
class Title:
 fontsize_list=['xx-small','x-small','small','medium','large','x-large','xx-large']
 fontstretch_list=['ultra-condensed','extra-condensed','condensed','semi-condensed','normal','semi-expanded','expanded','extra-expanded','ultra-expanded']
 fontstyle_list=['normal','italic','oblique']
 fontvariant_list=['normal','small-caps']
 fontweight_list=['ultralight','light','normal','regular','book','medium','roman','semibold','demibold','demi','bold','heavy','extra bold','black']
 def __init__(
self,
ax,
title,
loc=None,
pad=None,
y=None,
color=None,
ha=None,
va=None,
rotation='horizontal',
rotation_mode=True,
angle='degree',
alpha=1,
zorder=4,
font=None,
fontsize=12,
fontstretch=None,
fontstyle=None,
fontvariant=None,
fontweight=None
):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  alpha=range_zero_one(alpha)
  if isinstance(fontsize,int|float) or fontsize in self.fontsize_list:fontsize=fontsize
  else:fontsize=12
  if (isinstance(fontstretch,int|float) and 0<=fontstretch<=1000) or fontstretch in self.fontstretch_list:fontstretch=fontstretch
  else:fontstretch='normal'
  fontstyle=listchose(fontstyle,self.fontstyle_list)
  fontvariant=listchose(fontvariant,self.fontvariant_list)
  if (isinstance(fontweight,int|float) and 0<=fontweight<=1000) or fontweight in self.fontweight_list:fontweight=fontweight
  else:fontweight='normal'
  if not isinstance(zorder,int|float|None):zorder=4
  if isinstance(pad,int|float|None):pad=pad
  else:
   raise TypeError('padにはNoneもしくは数値の型を指定してください')
  if isinstance(y,int|float|None):y=y
  else:
   raise TypeError('yにはNoneもしくは数値の型を指定してください')
  loc=listchose(loc,['center','left','right'])
  ha=listchose(ha,['center','left','right'])
  va=listchose(va,['baseline','bottom','center','center_baseline','top'])
  if rotation in ['horizontal','vertical']:rotation=rotation
  elif isinstance(rotation,int|float):
   if angle=='radian':rotation=float(Rad(rotation))
   elif angle=='degree':rotation=rotation
   else:rotation='horizontal'
  else:rotation='horizontal'
  if isinstance(rotation_mode,bool) and rotation_mode:rotation_mode='default'
  else:rotation_mode='anchor'
  self.title_data=self.ax.set_title(
title,
loc=loc,
pad=pad,
color=color,
ha=ha,
va=va,
rotation=rotation,
rotation_mode=rotation_mode,
alpha=alpha,
zorder=zorder,
fontproperties=font,
fontsize=fontsize,
fontstretch=fontstretch,
fontstyle=fontstyle,
fontvariant=fontvariant,
fontweight=fontweight
)
 def title(self):return self.title_data