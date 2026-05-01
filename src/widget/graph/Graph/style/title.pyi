from typing import Any,Literal
from matplotlib.text import Text
from matplotlib.axes._axes import Axes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ....developer import Number
class Title:
 def __init__(
self,
ax:Axes|Axes3D,
title:str,
fontdict:dict[str,Any]|None=None,
loc:Literal['center','left','right']|None='center',
pad:int|float|Number|None=6.0,
y:int|float|Number|None=None,
**kwargs:Text
)->None:'''グラフのタイトルを設定する。

 :param title: タイトルを指定する。
 :type title: str
 :param loc: タイトルの表示場所を指定する。
 :type loc: Literal["center","left","right"]|None
 :param pad: タイトルと上部の軸との距離をポイント単位で指定する。
 :type pad: int|float|Number|None
 :param y: タイトルを表示する垂直軸の位置を指定する。
 :type y: int|float|Number|None
 :raises TypeError: `ax`が`Axes`もしくは`Axes3D`の型で指定しなかった場合に発生させる
 :raises TypeError: `pad`がNoneもしくは数値の型を指定しなかった場合に発生させる
 :raises TypeError: `y`がNoneもしくは数値の型を指定しなかった場合に発生させる'''
 def __str__(self)->str:...
 def title(self)->Text:'''ax.set_titleで返ってきた戻り値を返す。

 :return: ax.set_titleで返ってきた戻り値を返す。
 :rtype: Text'''