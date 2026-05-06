'''y軸ラベルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ..developer import Rad,listchose,range_zero_one
__all__=['Ylabel']
class Ylabel:
 def __init__(
self,
ax,
text,
color=None,
ha=None,
va=None,
rotation='horizontal',
rotation_mode=True,
angle='degree',
alpha=1,
zorder=4
):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  if isinstance(labelpad,int|float|None):labelpad=labelpad
  else:
   raise TypeError('labelpadにはNoneもしくは数値の型を指定してください')
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
  alpha=range_zero_one(alpha)
  if not isinstance(zorder,int|float|None):zorder=4
  self.ax.set_ylabel(
text,
labelpad=labelpad,
color=color,
ha=ha,
va=va,
rotation=rotation,
rotation_mode=rotation_mode
)