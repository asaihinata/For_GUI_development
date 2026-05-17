from os import PathLike
from pathlib import Path
from tkinter import Misc
from matplotlib.axes._axes import Axes
from matplotlib.collections import EventCollection,FillBetweenPolyCollection,PathCollection,PolyCollection,QuadMesh
from matplotlib.container import BarContainer,ErrorbarContainer,StemContainer
from matplotlib.lines import Line2D
from matplotlib.mlab import GaussianKDE
from matplotlib.patches import Polygon,StepPatch,Wedge
from matplotlib.text import Text
from numpy import float64,ndarray
from numpy.typing import ArrayLike
from ...typing import *
__all__=['BarGraph','BarhGraph','Boxplot','Ecdf','Errorbar','Eventplot','Funne','Hatplot','Hexbin','Hist','Linefill','LineGraph','Pie','Scatter','Stack','Stacked','Stackedh','Stem','Step','Violinplot','Waterfall','Waterfallh','Hist2d']
class _2Gset:
 ax:Axes
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
class LineGraph(_2Gset):
 def update(
self,
x:n_array,
y:n_array,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
marker:str,
markersize:int|float,
linestyle:str,
linewidth:int|float,
)->NoReturn:'''折線グラフを再表示させる。'''
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class BarGraph(_2Gset):
 def update(
self,
x:o_array,
y:n_array,
logs:bool,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
width:int|float,
align:Literal['center','edge']
)->NoReturn:'''縦軸棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class BarhGraph(_2Gset):
 def update(
self,
x:o_array,
y:n_array,
height:int|float,
align:Literal['center','edge'],
logs:bool,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''横軸棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Funne(_2Gset):
 def update(
self,
x:o_array,
height:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
aylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''じょうごグラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Stacked(_2Gset):
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
)->NoReturn:'''積み上げ縦棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Stackedh(_2Gset):
 def update(
self,
data:n_array,
dataname:o_array,
height:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''積み上げ横棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Pie(_2Gset):
 def update(
self,
data:o_array,
labeldistance:int|float,
startangletype:bool,
explode:tuple[int,float]|int|float,
startangle:int|float,
shadow:bool,
counterclock:bool,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''円グラフを再表示させる。'''
 def get(self)->tuple[tuple[Wedge,Text],...]:'''`matplotlib.axes.Axes.pie`の戻り値を配列で返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Boxplot(_2Gset):
 def update(
self,
data:n_array,
width:int|float,
whis:int|float,
label:labeltype,
legend:bool,
fill:bool,
notch:bool,
showfliers:bool,
orientation:Literal['horizontal','vertical'],
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''箱ひげ図を再表示させる。'''
 def get(self)->list[dict[str,Any]]:'''`matplotlib.axes.Axes.boxplot`の戻り値の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Waterfall(_2Gset):
 def update(
self,
x:o_array,
y:o_array,
colorline:ColorType,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
ucolor:ColorType,
dcolor:ColorType,
width:int|float,
align:Literal['center','edge'],
)->NoReturn:'''滝グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Waterfallh(_2Gset):
 def update(
self,
x:o_array,
y:o_array,
colorline:ColorType,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
ucolor:ColorType,
dcolor:ColorType,
height:int|float,
align:Literal['center','edge'],
)->NoReturn:'''横向きの滝グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Scatter(_2Gset):
 def update(
self,
x:n_array,
y:n_array,
marker:str,
markersize:int|float,
linewidth:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''散布図を再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Stem(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
label:labeltype=...,
labelalpha:int|float=1.0,
labelzorder:int|float=4,
labelfg:ColorType=...,
labelha:Literal['left','center','right']|None=None,
labelva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
labelrotation:float|Literal['vertical','horizontal']|None='horizontal',
labelrotation_mode:bool=True,
labelfontname:str|Type_Iterablestr|None=None,
labelfontpath:str|PathLike|Path|None=None,
xlabel:str=...,
xlabelalpha:int|float=1.0,
xlabelzorder:int|float=4,
xlabelfg:ColorType=...,
xlabelha:Literal['left','center','right']|None=None,
xlabelva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
xlabelrotation:float|Literal['vertical','horizontal']|None='horizontal',
xlabelrotation_mode:bool=True,
xlabelfontname:str|Type_Iterablestr|None=None,
xlabelfontpath:str|PathLike|Path|None=None,
ylabel:str=...,
ylabelalpha:int|float=1.0,
ylabelzorder:int|float=4,
ylabelfg:ColorType=...,
ylabelha:Literal['left','center','right']|None=None,
ylabelva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
ylabelrotation:float|Literal['vertical','horizontal']|None='vertical',
ylabelrotation_mode:bool=True,
ylabelfontname:str|Type_Iterablestr|None=None,
ylabelfontpath:str|PathLike|Path|None=None,
orientation:Literal['vertical','horizontal']='vertical',
bottom:int|float=0,
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...,
color:Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
titlealpha:int|float=1.0,
titlezorder:int|float=4,
titlefg:ColorType=...,
titleha:Literal['left','center','right']|None=None,
titleva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
titlerotation:float|Literal['vertical','horizontal']|None='horizontal',
titlerotation_mode:bool=True,
titlefontname:str|Type_Iterablestr|None=None,
titlefontpath:str|PathLike|Path|None=None,
dpi:int|float=100,
alpha:int|float=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|tuple[int|tuple,...]=0,
yticksrange:int|float|tuple[int|tuple,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
legendanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
legendplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
legendtitle:str=...,
legendframe:bool=True,
legendshadow:bool=False,
legendalpha:int|float=1,
legendncols:int=1,
master:Misc=None
)->None:'''幹図を作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param orientation: 茎の向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param bottom: ベースラインの位置を指定する。
 :type bottom: int|float
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param titlealpha: グラフの透明度を指定する。
 :type titlealpha: int|float
 :param titlezorder: グラフのタイトルの重なりの順を指定する。
 :type titlezorder: int|float
 :param titlefg: グラフのタイトルの文字色を指定する。
 :type titlefg: ColorType
 :param titleha: グラフのタイトルの水平方向の配置を指定する。
 :type titleha: Literal['left','center','right']|None
 :param titleva: グラフのタイトルの垂直方向を指定する。
 :type titleva: Literal['bottom','baseline','center','center_baseline','top']|None
 :param titlerotation: グラフのタイトルの回転角度を指定する。
 :type titlerotation: float|Literal['vertical','horizontal']|None
 :param titlerotation_mode: グラフのタイトルの回転方法を指定する。
 :type titlerotation_mode: bool
 :param titlefontname: グラフのタイトルのフォント名を指定する。
 :type titlefontname: str|Type_Iterablestr|None
 :param titlefontpath: グラフのタイトルのフォントファイルを指定する。
 :type titlefontpath: str|PathLike|Path|None
 :param marker: 幹のマーカーの種類を指定する。
 :type marker: Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']
 :param line: 幹の線の種類を指定する。
 :type line: Literal['-','--','-.','-.']
 :param color: 色を指定する。
 :type color: Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: int|float
 :param alpha: グラフの透明度を指定する。
 :type alpha: int|float
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|tuple[int|tuple,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|tuple[int|tuple,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param legendanchor: 凡例の位置を指定する。
 :type legendanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param legendplace: 凡例の位置の基準点を指定する。
 :type legendplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param legendtitle: 凡例のタイトルを指定する。
 :type legendtitle: bool
 :param legendframe: 凡例の背景を含む外枠を表示するか指定する。
 :type legendframe: bool
 :param legendshadow: 凡例に影を付与するか指定する。
 :type legendshadow: bool
 :param legendalpha: 凡例の背景の透明度を指定する。
 :type legendalpha: int|float
 :param legendncols: 凡例の列数を指定する。
 :type legendncols: int'''
 def update(
self,
x:n_array,
y:n_array,
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
bottom:int|float,
orientation:Literal['horizontal','vertical'],
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...
)->NoReturn:'''幹図を再表示させる。'''
 def get(self)->list[StemContainer]:'''`StemContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Hist(_2Gset):
 def update(
self,
data:o_array,
fg:ColorType,
bg:ColorType,
alpha:int|float,
decimalpoint:int|float,
graph_grid:ColorType,
title:str,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt'],
min:int|float,
max:int|float,
bottom:int|float,
orientation:Literal['horizontal','vertical'],
width:int|float
)->NoReturn:'''ヒストグラムを再表示させる。'''
 def get(self)->list[ndarray|list[ndarray],ndarray,BarContainer|Polygon|list[BarContainer|Polygon]]:'''`matplotlib.axes.Axes.hist`の戻り値を配列で返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''

 @overload
 def getrange(self,num:bool)->Typetuple_float64|tuple[float,float]:'''ヒストグラムの`bins`の上限値と下限値をtuple型で返す。

 :param num: 戻り値内の数値がfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の上限値と下限値を返す。
 :rtype: Typetuple_float64|tuple[float,float]'''
 @overload
 def getrange(self,num:bool=True)->Typetuple_float64:'''ヒストグラムの`bins`の上限値と下限値をtuple型で返す。

 :param num: 戻り値内の数値がfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の上限値と下限値を返す。
 :rtype: Typetuple_float64'''
 @overload
 def getrange(self,num:bool=False)->tuple[float,float]:'''ヒストグラムの`bins`の上限値と下限値をtuple型で返す。

 :param num: 戻り値内の数値がfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の上限値と下限値を返す。
 :rtype: tuple[float,float]'''
 @overload
 def getmin(self,num:bool)->float64|float:'''ヒストグラムの`bins`の下限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: float64|float'''
 @overload
 def getmin(self,num:bool=True)->float64:'''ヒストグラムの`bins`の下限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の下限値を返す。
 :rtype: float64'''
 @overload
 def getmin(self,num:bool=False)->float:'''ヒストグラムの`bins`の下限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の下限値を返す。
 :rtype: float'''
 @overload
 def getmax(self,num:bool)->float64|float:'''ヒストグラムの`bins`の上限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: float64|float'''
 @overload
 def getmax(self,num:bool=True)->float64:'''ヒストグラムの`bins`の上限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: float64'''
 @overload
 def getmax(self,num:bool=False)->float:'''ヒストグラムの`bins`の上限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: float'''
class Step(_2Gset):
 def update(
self,
data:n_array,
linewidth:int|float,
range:int|float|ListNumbertype2|TupleNumbertype2,
fill:bool,
baseline:int|float,
orientation:Literal['horizontal','vertical'],
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''階段グラフを再表示させる。'''
 def get(self)->list[StepPatch]:'''`StepPatch`の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Stack(_2Gset):
 def update(
self,
x:n_array,
y:n_array,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||'],
baseline:Literal['zero','sym','wiggle','weighted_wiggle'],
fg:ColorType,
bg:ColorType,
alpha:int|float,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''積み上げエリアチャートを再表示させる。'''
 def get(self)->list[FillBetweenPolyCollection]:'''`FillBetweenPolyCollection`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Linefill(_2Gset):
 def update(
self,
x:o_array,
ymin:n_array,
ymax:n_array,
centerlinewidth:int|float,
xlabel:str,
ylabel:str,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''2つの水平曲線の間の領域を埋めるグラフを再表示させる。'''
 def get(self)->list[FillBetweenPolyCollection,Line2D]:'''`PathCollection`と`Line2D`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def getymin(self)->Typeget_data:'''`ymin`のデータを取得する。'''
 def getymax(self)->Typeget_data:'''`ymax`のデータを取得する。'''
class Ecdf(_2Gset):
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Errorbar(_2Gset):
 def update(
self,
x:n_array,
y:n_array,
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
decimalpoint:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Eventplot(_2Gset):
 def update(
self,
data:o_array,
linewidth:int|float,
linelength:int|float,
orientation:Literal['vertical','horizontal'],
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':'],
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''円グラフを再表示させる。'''
 def get(self)->list[EventCollection]:'''`EventCollection`の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Hist2d(_2Gset):
 def update(
self,
x:o_array,
y:o_array,
max:int|float,
min:int|float,
xmax:int|float,
xmin:int|float,
ymax:int|float,
ymin:int|float,
bins:int|TupleInt2|ArrayLike|tuple[ArrayLike,ArrayLike],
density:bool,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''2次元ヒストグラムを再表示させる。

 :raises TypeError: `x`もしくは`y`もしくはその両方が二次元配列以上の多次元配列の場合に発生させる。
 :raises TypeError: `x`と`y`の要素の数が同じではない時に発生させる。'''
 def get(self)->list[ndarray,ndarray,ndarray,QuadMesh]:'''`matplotlib.axes.Axes.hist2d`の戻り値を配列で返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Violinplot(_2Gset):
 def update(
self,
data:n_array,
x:o_array,
y:o_array,
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
decimalpoint:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''バイオリングラフを再表示させる。'''
 def get(self)->list[dict[str,Collection]]:'''`matplotlib.axes.Axes.violinplot`のバイオリンプロットの各コンポーネントの辞書型が入った配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''
class Hexbin(_2Gset):
 def update(
self,
x:o_array,
y:o_array,
c:o_array|None,
gridsize:int|TupleInt2,
extent:TupleFloat4|None,
xscale:Literal['linear','log'],
yscale:Literal['linear','log'],
mincnt:int,
fg:ColorType,
bg:ColorType,
alpha:int|float,
decimalpoint:int|float,
graph_grid:ColorType,
title:str
)->NoReturn:'''2次元六角形グラフを再表示させる。'''
 def get(self)->list[PolyCollection]:'''`PolyCollection`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Hatplot(_2Gset):
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''