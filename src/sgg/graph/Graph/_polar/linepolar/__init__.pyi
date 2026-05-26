from matplotlib.lines import Line2D
from .._Polarset import _polarset
from ....typing import *
__all__=['Linepolar']
class Linepolar(_polarset):
 def update(
self,
x:o_array,
y:o_array,
data:o_array,
linestyle:Type_Solid,
marker:Type_Marker,
linewidth:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
):'''極軸折線グラフを再表示させる。'''
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''