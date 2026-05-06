'''タイトルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ..developer import Rad,listchose,range_zero_one
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
font=None
):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  alpha=range_zero_one(alpha)
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
fontproperties=font
)
 def title(self):return self.title_data