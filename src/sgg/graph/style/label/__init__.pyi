from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
class Xlabel:
 def __init__(
self,
ax:Axes|Axes3D,
text:str=...,
**kwd
)->None:...
class Ylabel:
 def __init__(
self,
ax:Axes|Axes3D,
text:str=...,
**kwd
)->None:...
class Zlabel:
 def __init__(
self,
ax:Axes3D,
text:str=...,
**kwd
)->None:...