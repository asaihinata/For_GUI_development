'''軸ラベルのスタイルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
__all__=['Xlabel','Ylabel','Zlabel']
class Xlabel:
 def __init__(self,ax,text,**kwd):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  ax.set_xlabel(xlabel=text,**kwd)
class Ylabel:
 def __init__(self,ax,text,**kwd):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  ax.set_ylabel(xlabel=text,**kwd)
class Zlabel:
 def __init__(self,ax,text,**kwd):
  if not isinstance(ax,Axes3D):
   raise TypeError('axの型が違います')
  ax.set_zlabel(xlabel=text,**kwd)