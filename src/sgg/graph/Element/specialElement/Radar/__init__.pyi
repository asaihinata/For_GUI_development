from matplotlib.projections.polar import PolarAxes
from numpy import int64,ndarray
from ....typing import *
from ...Graph import GElement
from ....style import getLabel
__all__=['RadarElement']
class RadarElement(GElement):
 label:getLabel
 ax:PolarAxes
 data:ndarray
 theta:ndarray[float64,dtype[float64]]
 thetas:ndarray[int64,dtype[int64]]
 frametype:Literal['circle','polygon']='circle'
 def _updates(
self,
fg:ColorType,
bg:ColorType,
graph_grid:ColorType,
title:str
):...
 def _adjustment(self):'''グラフの調整を行う'''
 def clear(self):'''グラフ内のグラフをクリアする。'''
 def invert(self):'''x軸,y軸を反転させる。'''
 def invert_x(self):'''x軸を反転させる。'''
 def invert_y(self):'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:'''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:'''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:'''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:'''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''