'''タイトルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ..dev import Rad,listchose,range_zero_one
__all__=['Title']
class Title:
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
  self.font=font
  self.color=color
  self.alpha=range_zero_one(alpha)
  if isinstance(fontsize,int|float) or fontsize in ['xx-small','x-small','small','medium','large','x-large','xx-large']:self.fontsize=fontsize
  else:self.fontsize=12
  if (isinstance(fontstretch,int|float) and 0<=fontstretch<=1000) or fontstretch in ['ultra-condensed','extra-condensed','condensed','semi-condensed','normal','semi-expanded','expanded','extra-expanded','ultra-expanded']:self.fontstretch=fontstretch
  else:self.fontstretch='normal'
  self.fontstyle=listchose(fontstyle,['normal','italic','oblique'])
  self.fontvariant=listchose(fontvariant,['normal','small-caps'])
  if (isinstance(fontweight,int|float) and 0<=fontweight<=1000) or fontweight in ['ultralight','light','normal','regular','book','medium','roman','semibold','demibold','demi','bold','heavy','extra bold','black']:self.fontweight=fontweight
  else:self.fontweight='normal'
  if not isinstance(zorder,int|float|None):self.zorder=4
  else:
   self.zorder=zorder
  if not isinstance(pad,int|float|None):
   raise TypeError('padにはNoneもしくは数値の型を指定してください')
  else:self.pad=pad
  if not isinstance(y,int|float|None):
   raise TypeError('yにはNoneもしくは数値の型を指定してください')
  else:self.y=y
  self.loc=listchose(loc,['center','left','right'])
  self.ha=listchose(ha,['center','left','right'])
  self.va=listchose(va,['baseline','bottom','center','center_baseline','top'])
  if rotation in ['horizontal','vertical']:self.rotation=rotation
  elif isinstance(rotation,int|float):
   if angle=='radian':self.rotation=float(Rad(rotation))
   elif angle=='degree':self.rotation=rotation
   else:self.rotation='horizontal'
  else:self.rotation='horizontal'
  if isinstance(rotation_mode,bool) and rotation_mode:self.rotation_mode='default'
  else:self.rotation_mode='anchor'
  self.title=self.ax.set_title(
title,
loc=self.loc,
pad=self.pad,
color=self.color,
ha=self.ha,
va=self.va,
rotation=self.rotation,
rotation_mode=self.rotation_mode,
alpha=self.alpha,
zorder=self.zorder,
fontproperties=self.font,
fontsize=self.fontsize,
fontstretch=self.fontstretch,
fontstyle=self.fontstyle,
fontvariant=self.fontvariant,
fontweight=self.fontweight
)
 def set_title(self,title):
  self.ax.set_title(
title,
loc=self.loc,
pad=self.pad,
color=self.color,
ha=self.ha,
va=self.va,
rotation=self.rotation,
rotation_mode=self.rotation_mode,
alpha=self.alpha,
zorder=self.zorder,
fontproperties=self.font,
fontsize=self.fontsize,
fontstretch=self.fontstretch,
fontstyle=self.fontstyle,
fontvariant=self.fontvariant,
fontweight=self.fontweight
)