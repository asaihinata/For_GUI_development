'''タイトルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from .....developer import Number
__all__=['Title']
class Title:
 def __init__(self,ax,title,loc=None,pad=None,y=None,**kwargs):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  self.titles=title
  if pad is None or isinstance(pad,int|float):self.pad=pad
  elif isinstance(pad,Number):self.pad=pad.val
  else:
   raise TypeError('padにはNoneもしくは数値の型を指定してください')
  if y is None or isinstance(y,int|float):self.y=y
  elif isinstance(y,Number):self.y=y.val
  else:
   raise TypeError('yにはNoneもしくは数値の型を指定してください')
  if loc in ['left','center','right']:self.loc=loc
  else:self.loc=None
  self.title_data=self.ax.set_title(self.titles,loc=self.loc,pad=self.pad,y=self.y,**kwargs)
 def __str__(self):return str(self.titles)
 def title(self):return self.title_data