from matplotlib.collections import PathCollection
from .._Polarset import _polarset
from ....typing import *
__all__=['Scatterpolar']
class Scatterpolar(_polarset):
 def update(
self,
marker:Type_Marker,
markersize:int|float,
linewidth:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
):'''極軸散布図を再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''