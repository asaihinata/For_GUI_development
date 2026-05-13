from typing import Literal
from matplotlib.axes._axes import Axes
from matplotlib.text import Text
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ....typing import ColorTypes,Type_NumberandNone
class Title:
 title:Text
 def __init__(
self,
ax:Axes|Axes3D,
title:str,
loc:Literal['center','left','right']='center',
pad:Type_NumberandNone=6.0,
y:Type_NumberandNone=None,
color:ColorTypes=None,
ha:Literal['left','center','right']='center',
va:Literal['bottom','baseline','center','center_baseline','top']=None,
rotation:float|Literal['vertical','horizontal']|None='horizontal',
rotation_mode:bool=True,
angle:Literal['degree','radian']='degree',
alpha:float=1.0,
zorder:int|float=4
)->None:'''グラフのタイトルを設定する。

 :param title: タイトルを指定する。
 :type title: str
 :param loc: タイトルの表示場所を指定する。
 :type loc: Literal['center','left','right']|None
 :param pad: タイトルと上部の軸との距離をポイント単位で指定する。
 :type pad: Type_NumberandNone
 :param y: タイトルを表示する垂直軸の位置を指定する。
 :type y: Type_NumberandNone'''