from tkinter import Misc
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import ndarray
from ...typing import *
from ..Graph import GElement
class threeElement(GElement):
 def __init__(
self,
master:Misc=None,
x:nListlike=None,
y:nListlike=None,
z:nListlike=None,
label:labeltype=None,
grid_xyz:bool=True,
grid_x:bool=False,
grid_y:bool=False,
grid_z:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
zmajorint:bool=True,
elev:int|float=30,
azim:int|float=45,
mouse_rotation:bool=True,
xticksshow:bool=False,
yticksshow:bool=False,
zticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out'
)->None:
  '''3Dのグラフを作成する。

 :param x: x軸のデータを指定する。
 :type x: nListlike
 :param y: y軸のデータを指定する。
 :type y: nListlike
 :param z: z軸のデータを指定する。
 :type z: nListlike
 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: labeltype
 :param grid_xyz: x軸,y軸,z軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`,`grid_z`より優先度が高い。
 :type grid_xyz: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_y: bool
 :param grid_z: z軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_z: bool
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param zmajorint: z軸の目盛りを整数で自動調整させるか指定する。
 :type zmajorint: bool
 :param mouse_rotation: グラフをマウスでできるか指定する。
 :type mouse_rotation: bool
 :param elev: 仰角を度数表記で指定する。
 :type elev: int|float
 :param azim: 方位角を度数表記で指定する。
 :type azim: int|float
 :param xticksshow: x軸の目盛りを線を表示させるか指定する。
 :type xticksshow: bool
 :param yticksshow: y軸の目盛りを線を表示させるか指定する。
 :type yticksshow: bool
 :param zticksshow: z軸の目盛りを線を表示させるか指定する。
 :type zticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']'''
  self.ax:Axes3D
  self.x:nListlike
  self.y:nListlike
  self.z:nListlike
  self.label:labeltype
  self.xlabel:labeltype
  self.ylabel:labeltype
  self.zlabel:labeltype
  self.grid_xyz:bool
  self.grid_x:bool
  self.grid_y:bool
  self.grid_z:bool
  self.xmajorint:bool
  self.ymajorint:bool
  self.zmajorint:bool
  self.elev:int|float
  self.azim:int|float
 def _updates(
self,
fg:ColorType,
bg:ColorType,
graph_grid:ColorType,
title:str,
elev:int|float,
azim:int|float,
xlabel:labeltype,
ylabel:labeltype,
zlabel:labeltype
)->NoReturn:...
 def _apply_labels(
self,
xlabel:labeltype=None,
ylabel:labeltype=None,
zlabel:labeltype=None
)->NoReturn:'''3Dのグラフのx軸,y軸,z軸のラベルを作成する。

 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: labeltype'''
 def _apply_grid(self)->NoReturn:'''グリッド線を加えるメソッド。'''
 def clear(self)->NoReturn:'''グラフ内のグラフをクリアする。'''
 def invert(self)->NoReturn:'''x軸,y軸,z軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def invert_z(self)->NoReturn:'''z軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64],
tuple[float64,float64]
]:'''x軸,y軸,z軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:'''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:'''y軸の下限値と上限値を昇順で返す。'''
 def getzbound(self)->tuple[float64,float64]:'''z軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray,ndarray]:'''x軸,y軸,z軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''
 def getzticks(self)->ndarray:'''z軸の目盛りの位置を座標で返します。'''