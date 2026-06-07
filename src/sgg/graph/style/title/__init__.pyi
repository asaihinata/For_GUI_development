from matplotlib.axes._axes import Axes
from matplotlib.text import Text
from mpl_toolkits.mplot3d.axes3d import Axes3D
class Title:
 def __init__(
self,
ax:Axes|Axes3D,
title:str,
**kwd
)->None:'''グラフのタイトルを設定する。

 :param title: タイトルを指定する。
 :type title: str'''
 @property
 def title(self)->Text:...