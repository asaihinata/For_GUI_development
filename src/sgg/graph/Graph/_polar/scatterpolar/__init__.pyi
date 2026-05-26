from matplotlib.container import ErrorbarContainer
from .._Polarset import _polarset
from ....typing import *
__all__=['Scatterpolar']
class Scatterpolar(_polarset):
 def update(
self,
x:o_array,
y:o_array,
data:o_array,
err:o_array,
xerr:o_array,
yerr:o_array,
xuplims:bool,
xlolims:bool,
yuplims:bool,
ylolims:bool,
barsabove:bool,
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':'],
marker:Literal['.','s','o','p','v','*','^','D'],
linewidth:int|float,
capthick:int|float,
capsize:int|float,
errorevery:int|list[int]|tuple[int],
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
):'''極軸散布図を再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''