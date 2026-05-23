from matplotlib.container import StemContainer
from .._Polarset import _polarset
from ....typing import *
__all__=['Stempolar']
class Stempolar(_polarset):
 def update(
self,
x:o_array,
y:o_array,
data:o_array,
linefmt:str|None,
markerfmt:str|None,
basefmt:str|None,
bottom:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''極軸幹図を再表示させる。'''
 def get(self)->list[StemContainer]:'''`StemContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''