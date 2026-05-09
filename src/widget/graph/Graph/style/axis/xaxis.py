'''x軸のスタイルの設定'''
from matplotlib.axes._axes import Axes
from matplotlib.ticker import FixedLocator,LinearLocator,MaxNLocator,MultipleLocator
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ....._function import listchose
from .....dev import LISTNumber
__all__=['Xaxis']
class Xaxis:
 def __init__(self,ax):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.ax=ax
  self.xax=ax.xaxis
 def FixedLocator(self,locs=None,nbins=None):
  self.xax.set_major_locator(FixedLocator(locs=locs,nbins=nbins))
 def LinearLocator(self,numticks=None,presets=None):
  self.xax.set_major_locator(LinearLocator(numticks=numticks,presets=presets))
 def MultipleLocator(self,base=1.0,offset=0.0):
  self.xax.set_major_locator(MultipleLocator(base=base,offset=offset))
 def MaxNLocator(self,nbins=10,steps=None,integer=False,symmetric=False,prune=None,min_n_ticks=2):
  self.xax.set_major_locator(MaxNLocator(nbins=nbins,steps=steps,integer=integer,symmetric=symmetric,prune=prune,min_n_ticks=min_n_ticks))
 def set_log(self,base=10,nonpositive='clip',subs=None):
  nonpositive=listchose(nonpositive,['clip','mask'])
  subs=None if subs is None else list(LISTNumber(subs))
  self.ax.set_xscale('log',base=base,nonpositive=nonpositive,subs=subs)