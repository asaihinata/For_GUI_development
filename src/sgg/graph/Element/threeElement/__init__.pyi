from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import ndarray
from ...typing import *
from ..Graph import GElement,getLabel
__all__=['threeElement']
class threeElement(GElement):
 label:getLabel
 ax:Axes3D
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
):...
 def _apply_labels(
self,
xlabel:labeltype=None,
ylabel:labeltype=None,
zlabel:labeltype=None
):'''3Dのグラフのx軸,y軸,z軸のラベルを作成する。

 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: labeltype'''
 def _apply_grid(self):'''グリッド線を加えるメソッド。'''
 def _adjustment(self):'''グラフの調整を行う'''
 def clear(self):'''グラフ内のグラフをクリアする。'''
 def invert(self):'''x軸,y軸,z軸を反転させる。'''
 def invert_x(self):'''x軸を反転させる。'''
 def invert_y(self):'''y軸を反転させる。'''
 def invert_z(self):'''z軸を反転させる。'''
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