from typing import Literal

from matplotlib.axes._axes import Axes
from matplotlib.text import Text
from mpl_toolkits.mplot3d.axes3d import Axes3D

from ..typing import *

class Title:
 def __init__(
self,
ax:Axes|Axes3D,
title:str,
loc:Literal['center','left','right']='center',
pad:NumberNone=6.0,
y:NumberNone=None,
color:ColorType=None,
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
 :type pad: NumberNone
 :param y: タイトルを表示する垂直軸の位置を指定する。
 :type y: NumberNone
 :raises TypeError: `ax`が`Axes`もしくは`Axes3D`の型で指定しなかった場合に発生させる
 :raises TypeError: `pad`がNoneもしくは数値の型を指定しなかった場合に発生させる
 :raises TypeError: `y`がNoneもしくは数値の型を指定しなかった場合に発生させる'''
 def __str__(self)->str:...
 def title(self)->Text:'''ax.set_titleの戻り値を返す。

 :return: ax.set_titleの戻り値を返す。
 :rtype: Text'''