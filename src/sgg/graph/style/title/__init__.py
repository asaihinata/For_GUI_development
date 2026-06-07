'''タイトルの設定'''
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
__all__=['Title']
class Title:
 def __init__(self,ax,title,**kwd):
  if not isinstance(ax,Axes|Axes3D):
   raise TypeError('axの型が違います')
  self.__title=ax.set_title(title,**kwd)
 @property
 def title(self):return self.__title