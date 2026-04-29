'''x軸のスタイルの設定'''
from matplotlib.axes._axes import Axes
from ....._function import listchose
from .....developer import LISTNumber
class Xaxis:
 def __init__(self,ax):
  if isinstance(ax,Axes):self.ax=ax
  else:
   raise TypeError('axの型が違います')
 def set_log(self,base=10,nonpositive='clip',subs=None):
  nonpositive=listchose(nonpositive,['clip','mask'])
  subs=None if subs is None else list(LISTNumber(subs))
  self.ax.set_xscale('log',base=base,nonpositive=nonpositive,subs=subs)