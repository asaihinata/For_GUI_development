from matplotlib.axes._axes import Axes
from numpy import ndarray
from ...typing import *
from ..Graph import GElement,getLabel
class twoElement(GElement):
 label:getLabel
 ax:Axes
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
 def _adjustment(self)->NoReturn:'''グラフの調整を行う'''
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