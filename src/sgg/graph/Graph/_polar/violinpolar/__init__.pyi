from matplotlib.mlab import GaussianKDE
from .._Polarset import _polarset
from ....typing import *
__all__=['Violinpolar']
class Violinpolar(_polarset):
 def update(
self,
orientation:Literal['vertical','horizontal'],
width:int|float,
showextrema:bool,
showmeans:bool,
showmedians:bool,
points:int|float,
bw_method:Literal['scott','silverman']|float|Callable[[GaussianKDE],float],
side:Literal['both','low','high'],
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
):'''極軸バイオリングラフを再表示させる。'''
 def get(self)->list[dict[str,Collection]]:'''`matplotlib.axes.Axes.violinplot`のバイオリンプロットの各コンポーネントの辞書型が入った配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''