from matplotlib.container import BarContainer,ErrorbarContainer,StemContainer
from matplotlib.projections.polar import PolarAxes
from numpy import ndarray
from ...typing import *
__all__:Type_all=['Barpolar','Errorpolar','Eventpolar','Linepolar','Scatterpolar','Stempolar','Violinpolar']
class _polarset:
 ax:PolarAxes
 def winsize(self)->TupleInt2:'''ウィジェットの現在の幅と高さを返す。

 :return: ウィジェットの現在の幅と高さをタプルで返す。
 :rtype: TupleInt2'''
 def winwidth(self)->int:'''ウィジェットの現在の幅を返す。

 :return: ウィジェットの現在の幅を返す。
 :rtype: int'''
 def winheight(self)->int:'''ウィジェットの現在の高さを返す。

 :return: ウィジェットの現在の高さを返す。
 :rtype: int'''
 def winxy(self)->TupleInt2:'''親ウィジェット内での座標を返す。

 :return: 親ウィジェット内での座標を返す。
 :rtype: TupleInt2'''
 def winx(self)->int:'''親ウィジェット内での左端のx座標を返す。

 :return: 親ウィジェット内での左端のx座標を返す。
 :rtype: int'''
 def winy(self)->int:'''親ウィジェット内での上端のy座標を返す。

 :return: 親ウィジェット内での上端のy座標を返す。
 :rtype: int'''
 def geometry(self)->TupleFloat4:'''ウィジェットのサイズと位置を返す。

 :return: ウィジェットのサイズと位置を返す。
 :rtype: TupleFloat4'''
 def rootxy(self)->TupleInt2:'''画面全体に対するウィジェットの座標を返す。

 :return: 画面全体に対するウィジェットの座標を返す。
 :rtype: TupleInt2'''
 def rootx(self)->int:'''画面全体に対するウィジェットの左端のx座標を返す。

 :return: 画面全体に対するウィジェットの左端のx座標を返す。
 :rtype: int'''
 def rooty(self)->int:'''画面全体に対するウィジェットの上端のy座標を返す。

 :return: 画面全体に対するウィジェットの上端のy座標を返す。
 :rtype: int'''
 def reqsize(self)->TupleInt2:'''ウィジェットが必要とする幅の長さと高さを返す。

 :return: ウィジェットが必要とする幅の長さと高さを返す。
 :rtype: TupleInt2'''
 def reqwidth(self)->int:'''ウィジェットが必要とする幅の長さを返す。

 :return: ウィジェットが必要とする幅の長さを返す。
 :rtype: int'''
 def reqheight(self)->int:'''ウィジェットが必要とする高さを返す。

 :return: ウィジェットが必要とする高さを返す。
 :rtype: int'''
 def visual(self)->str:'''色の表現形式を返す。'''
 def screen(self)->str:'''スクリーンの名前を返す。'''
 def id(self)->int:'''ウィジェットのウィンドウ識別子を返す。'''
 def name(self):'''ウィジェットのインスタンス名を返す。'''
 def invert(self)->NoReturn:'''x軸,y軸の軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸の軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸の軸を反転させる。'''
 def getbound(self)->tuple[
Typetuple_float64,
Typetuple_float64
]:'''表示されているx軸,y軸の範囲の下限値と上限値を昇順で返す。

 :return: x軸,y軸の順で表示されている範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[Typetuple_float64,Typetuple_float64]'''
 def getxbound(self)->Typetuple_float64:'''表示されているx軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているx軸の範囲の下限値と上限値のtupleを返す。
 :rtype: Typetuple_float64'''
 def getybound(self)->Typetuple_float64:'''表示されているy軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているy軸の範囲の下限値と上限値のtupleを返す。
 :rtype: Typetuple_float64'''
 def getticks(self)->tuple[ndarray,ndarray]:'''x軸,y軸の目盛りの位置を返す。

 :return: x軸,y軸の目盛りの位置を返す。
 :rtype: tuple[ndarray,ndarray]'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返す。

 :return: x軸の目盛りの位置を返す。
 :rtype: ndarray'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返す。

 :return: y軸の目盛りの位置を返す。
 :rtype: ndarray'''
class Barpolar(_polarset):
 def update(
self,
x:o_array,
y:o_array,
data:o_array,
logs:bool,
align:Literal['center','edge'],
width:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''極軸棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
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
class Errorpolar(_polarset):
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
)->NoReturn:'''極軸エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Linepolar(_polarset):
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
)->NoReturn:'''極軸エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Eventpolar(_polarset):
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
)->NoReturn:'''極軸エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
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
)->NoReturn:'''極軸エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Violinpolar(_polarset):
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
)->NoReturn:'''極軸エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''