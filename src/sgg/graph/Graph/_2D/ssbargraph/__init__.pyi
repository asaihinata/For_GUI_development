from matplotlib.container import BarContainer
from ....typing import *
from .._2gset import _2Gset
__all__=['SSBarGraph']
class SSBarGraph(_2Gset):
 def update(
self,
data:n_array,
dataname:o_array,
width:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
):'''横並び棒グラフを再描画する。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getdata(self):'''`data`のデータを取得する。'''
 def getdataname(self):'''`dataname`のデータを取得する。'''