from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ..dev import *
__all__=['Legends']
class Legends:
 def __init__(self,ax,**kwd):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  handles,labels=ax.get_legend_handles_labels()
  self.legend=ax.legend(handles[::-1],labels[::-1],**kwd)