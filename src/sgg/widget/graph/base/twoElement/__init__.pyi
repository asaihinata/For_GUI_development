from tkinter import Misc
from matplotlib.axes._axes import Axes
from numpy import ndarray
from ...typing import *
from ..Graph import GElement
class twoElement(GElement):
 def __init__(
self,
master:Misc=None,
data:nListlike=None,
x:nListlike=None,
y:nListlike=None,
label:labeltype=None,
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
setxy:bool=True
)->None:
  '''2Dグラフの基盤のグラフを作成する。

 :param data: dataを指定する。
 :type data: nListlike
 :param x: x軸のデータを指定する。
 :type x: nListlike
 :param y: y軸のデータを指定する。
 :type y: nListlike
 :param label: グラフのラベルを指定する。
 :type label: labeltype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param xticksshow: x軸の目盛りを線を表示させるか指定する。
 :type xticksshow: bool
 :param yticksshow: y軸の目盛りを線を表示させるか指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout'] '''
  self.ax:Axes
  self.x:ndarray
  self.y:ndarray
  self.data:ndarray
  self.label:labeltype
  self.xlabel:labeltype
  self.ylabel:labeltype
  self.grid_xy:bool
  self.grid_x:bool
  self.grid_y:bool
  self.xmajorint:bool
  self.ymajorint:bool
 def _updates(
self,
fg:ColorType,
bg:ColorType,
graph_grid:ColorType,
title:str,
xlabel:labeltype,
ylabel:labeltype
)->NoReturn:...
 def _apply_labels(
self,
xlabel:labeltype=None,
ylabel:labeltype=None
)->NoReturn:'''2Dのグラフのx軸,y軸のラベルを作成する。

 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :return:
 :rtype: NoReturn'''
 def clear(self)->NoReturn:'''グラフ内のグラフをクリアする。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:'''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:'''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:'''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:'''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''