'''x軸ラベルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from .....developer import Number
__all__=['Xlabel']
class Xlabel:
 def __init__(self,ax,text,labelpad=None,loc=None,**kwargs):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  self.txt=text
  if labelpad is None or isinstance(labelpad,(int,float)):self.labelpad=labelpad
  elif isinstance(labelpad,Number):self.labelpad=labelpad.val
  else:
   raise TypeError('labelpadにはNoneもしくは数値の型を指定してください')
  if loc in ['left','center','right']:self.loc=loc
  else:self.loc=None
  self.ax.set_xlabel(self.txt,labelpad=self.labelpad,loc=self.loc,**kwargs)
 def __str__(self):return str(self.txt)