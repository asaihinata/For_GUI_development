from tkinter import Misc
from matplotlib.collections import EventCollection,FillBetweenPolyCollection,PathCollection,PolyCollection,QuadMesh
from matplotlib.container import BarContainer,ErrorbarContainer,StemContainer
from matplotlib.lines import Line2D
from matplotlib.mlab import GaussianKDE
from matplotlib.patches import Polygon,StepPatch,Wedge
from matplotlib.text import Text
from numpy import dtype,float64,ndarray
from numpy._typing import _AnyShape
from numpy.typing import ArrayLike
from ...types import *
from ..developer import Number
class _Gset:
 def winsize(self)->tuple[int,int]:'''ウィジェットの現在の幅と高さを返す。

 :return: ウィジェットの現在の幅と高さをタプルで返す。
 :rtype: tuple[int,int]'''
 def winwidth(self)->int:'''ウィジェットの現在の幅を返す。

 :return: ウィジェットの現在の幅を返す。
 :rtype: int'''
 def winheight(self)->int:'''ウィジェットの現在の高さを返す。

 :return: ウィジェットの現在の高さを返す。
 :rtype: int'''
 def winxy(self)->tuple[int,int]:'''親ウィジェット内での座標を返す。

 :return: 親ウィジェット内での座標を返す。
 :rtype: tuple[int,int]'''
 def winx(self)->int:'''親ウィジェット内での左端のx座標を返す。

 :return: 親ウィジェット内での左端のx座標を返す。
 :rtype: int'''
 def winy(self)->int:'''親ウィジェット内での上端のy座標を返す。

 :return: 親ウィジェット内での上端のy座標を返す。
 :rtype: int'''
 def geometry(self)->tuple[float,float,float,float]:'''ウィジェットのサイズと位置を返す。

 :return: ウィジェットのサイズと位置を返す。
 :rtype: tuple[float,float,float,float]'''
 def rootxy(self)->tuple[int,int]:'''画面全体に対するウィジェットの座標を返す。

 :return: 画面全体に対するウィジェットの座標を返す。
 :rtype: tuple[int,int]'''
 def rootx(self)->int:'''画面全体に対するウィジェットの左端のx座標を返す。

 :return: 画面全体に対するウィジェットの左端のx座標を返す。
 :rtype: int'''
 def rooty(self)->int:'''画面全体に対するウィジェットの上端のy座標を返す。

 :return: 画面全体に対するウィジェットの上端のy座標を返す。
 :rtype: int'''
 def reqsize(self)->tuple[int,int]:'''ウィジェットが必要とする幅の長さと高さを返す。

 :return: ウィジェットが必要とする幅の長さと高さを返す。
 :rtype: tuple[int,int]'''
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
class _2Gset(_Gset):
 def invert(self)->NoReturn:'''x軸,y軸の軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸の軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸の軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:'''表示されているx軸,y軸の範囲の下限値と上限値を昇順で返す。

 :return: x軸,y軸の順で表示されている範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[tuple[float64,float64],tuple[float64,float64]]'''
 def getxbound(self)->tuple[float64,float64]:'''表示されているx軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているx軸の範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[float64,float64]'''
 def getybound(self)->tuple[float64,float64]:'''表示されているy軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているy軸の範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[float64,float64]'''
 def getticks(self)->tuple[ndarray,ndarray]:'''x軸,y軸の目盛りの位置を返す。

 :return: x軸,y軸の目盛りの位置を返す。
 :rtype: tuple[ndarray,ndarray]'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返す。

 :return: x軸の目盛りの位置を返す。
 :rtype: ndarray'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返す。

 :return: y軸の目盛りの位置を返す。
 :rtype: ndarray'''
class _3Gset(_Gset):
 def invert(self)->NoReturn:'''x軸,y軸,z軸の軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸の軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸の軸を反転させる。'''
 def invert_z(self)->NoReturn:'''z軸の軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64],
tuple[float64,float64]
]:'''x軸,y軸,z軸の順で表示されている範囲の下限値と上限値を返す。

 :return: x軸,y軸,z軸の順で表示されている範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[tuple[float64,float64],tuple[float64,float64],tuple[float64,float64]]'''
 def getxbound(self)->tuple[float64,float64]:'''表示されているx軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているx軸の範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[float64,float64]'''
 def getybound(self)->tuple[float64,float64]:'''表示されているy軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているy軸の範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[float64,float64]'''
 def getzbound(self)->tuple[float64,float64]:'''表示されているz軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているz軸の範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[float64,float64]'''
 def getticks(self)->tuple[ndarray,ndarray,ndarray]:'''x軸,y軸,z軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''
 def getzticks(self)->ndarray:'''z軸の目盛りの位置を座標で返します。'''
class LineGraph(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
markersize:Numbertype=10,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']=None,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''折線グラフを作成する。

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
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param markersize: 折線グラフのマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param marker: 折線グラフのマーカーを指定する。
 :type marker: Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param linestyle: 折線グラフの線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',': ','none',None,' ','']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
marker:str,
markersize:Numbertype,
linestyle:str,
linewidth:Numbertype,
)->NoReturn:'''折線グラフを再表示させる。'''
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class BarGraph(_2Gset):
 def __init__(
self,
x:o_array=...,
y:n_array=...,
logs:bool=False,
align:Literal['center','edge']='center',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
width:Numbertype=1,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''縦軸棒グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param logs: y軸を対数スケールにするかを指定する。
 :type logs: bool
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param width: 棒グラフのバー幅を指定する。
 :type width: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
y:n_array,
logs:bool,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
width:Numbertype,
align:Literal['center','edge']
)->NoReturn:'''縦軸棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class BarhGraph(_2Gset):
 def __init__(
self,
x:o_array=...,
y:n_array=...,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelheight:Numbertype=1,
align:Literal['center','edge']='center'
)->None:'''横軸棒グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param logs: x軸を対数スケールにするかを指定する。
 :type logs: bool
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param height: 棒グラフのバーの幅を指定する。
 :type height: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
y:n_array,
height:Numbertype,
align:Literal['center','edge'],
logs:bool,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''横軸棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Funne(_2Gset):
 def __init__(
self,
x:o_array=...,
y:n_array=...,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelheight:Numbertype=1,
align:Literal['center','edge']='center'
)->None:'''じょうごグラフを生成する。

 :param data: `data`のデータを指定する。
 :type data: o_array
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。2n+1(nは正の整数)の整数を指定する。
 :type xmajormaxbins: int
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param height: 棒グラフのバーの幅を指定する。
 :type height: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
height:Numbertype,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''じょうごグラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Stacked(_2Gset):
 def __init__(
self,
data:n_array=...,
dataname:o_array=...,
width:Numbertype=0.8,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=(0,1),
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='lower left',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''積み上げ縦棒グラフを生成する。

 :param data: `data`を指定する。
 :type data: n_array
 :param dataname: カテゴリ名を指定する。
 :type dataname: o_array
 :param width: 積み上げ縦棒グラフの幅のサイズを指定する。
 :type width: Numbertype
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:n_array,
dataname:o_array,
width:Numbertype,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''積み上げ縦棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Stackedh(_2Gset):
 def __init__(
self,
data:n_array=...,
dataname:o_array=...,
height:Numbertype=0.8,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=(0,1),
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='lower left',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''積み上げ横棒グラフを生成する。

 :param data: `data`を指定する。
 :type data: n_array
 :param dataname: カテゴリ名を指定する。
 :type dataname: o_array
 :param height: 積み上げ横棒グラフの高さのサイズを指定する。
 :type height: Numbertype
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:n_array,
dataname:o_array,
height:Numbertype,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''積み上げ横棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Pie(_2Gset):
 def __init__(
self,
data:o_array=...,
startangle:Numbertype=0,
startangletype:bool=True,
shadow:bool=False,
counterclock:bool=False,
labeldistance:Numbertype=1.1,
explode:list[int,float,Number]|tuple[int,float,Number]|int|float|Number=...,
label:labeltype=...,
color:tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100
)->None:'''円グラフを作成する。

 :param data: データを指定する。
 :type data: o_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param startangle: 各要素の出力を開始する角度を指定する。
 :type startangle: Numbertype
 :param startangletype: 各要素の出力を開始する角度を度数法(True)か弧度法(False)かを指定する。
 :type startangletype: bool
 :param shadow: 円グラフに影を追加するか指定する。
 :type shadow: bool
 :param counterclock: 時計回りで出力するか指定する。
 :type counterclock: bool
 :param labeldistance: 中心からラベルの距離を指定する。
 :type labeldistance: Numbertype
 :param explode: 中心から各セグメントの離す距離を指定する。
 :type explode: list[int,float,Number]|tuple[int,float,Number]|int|float|Number
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype'''
 def update(
self,
data:o_array,
labeldistance:Numbertype,
startangletype:bool,
explode:tuple[int,float,Number]|int|float|Number,
startangle:Numbertype,
shadow:bool,
counterclock:bool,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''円グラフを再表示させる。'''
 def get(self)->tuple[tuple[Wedge,Text],...]:'''`matplotlib.axes.Axes.pie`の戻り値を配列で返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Boxplot(_2Gset):
 def __init__(
self,
data:n_array=...,
width:Numbertype=0.15,
whis:float|TupleFloat2=1.5,
legend:bool=True,
fill:bool=False,
notch:bool=False,
showfliers:bool=True,
orientation:Literal['vertical','horizontal']='vertical',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''箱ひげ図を作成する。

 :param data: dataのデータを指定する。
 :type data: n_array
 :param label: 箱ひげ図のデータ名を指定する。指定しなかった場合`box`+データの数になる。例)box0,box1
 :type label: labeltype
 :param legend: 凡例を表示させるか指定する。
 :type legend: bool
 :param fill: 箱内を塗りつぶすかを指定する。
 :type fill: bool
 :param notch: 箱の中央をくびれさすか指定する。
 :type notch: bool
 :param showfliers: 外れ値を表示させるか指定する。
 :type showfliers: bool
 :param whis: ヒゲの位置を指定する。
 :type whis: float|TupleFloat2
 :param orientation: 箱ひげ図の向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:n_array,
width:Numbertype,
whis:Numbertype,
label:labeltype,
legend:bool,
fill:bool,
notch:bool,
showfliers:bool,
orientation:Literal['horizontal','vertical'],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''箱ひげ図を再表示させる。'''
 def get(self)->list[dict[str,Any]]:'''`matplotlib.axes.Axes.boxplot`の戻り値の配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Waterfall(_2Gset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
sums:bool=False,
sumstext:str='sum',
ucolor:ColorType='#156082',
dcolor:ColorType='#e97132',
width:Numbertype=1,
colorline:ColorType='#4477aa',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''x軸向きの滝グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param sums: 合計値を表示するかを指定する。
 :type sums: bool
 :param sumstext: 合計のラベルを指定する。
 :type sumstext: str
 :param colorline: バーとバーを繋げる線の色を指定する。
 :type colorline: ColorType
 :param linestyle: バーとバーを繋げる線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param ucolor: 上昇バーの色を指定する。
 :type ucolor: ColorType
 :param dcolor: 下降バーの色を指定する。
 :type dcolor: ColorType
 :param width: バーの幅を指定する。
 :type width: Numbertype'''
 def update(
self,
x:o_array,
y:o_array,
colorline:ColorType,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
ucolor:ColorType,
dcolor:ColorType,
width:Numbertype,
align:Literal['center','edge'],
)->NoReturn:'''滝グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Waterfallh(_2Gset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
ucolor:ColorType='#156082',
dcolor:ColorType='#e97132',
height:Numbertype=1,
sums:bool=False,
sumstext:str='sum',
colorline:ColorType='#4477aa',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''y軸向きの滝グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param sums: 合計値を表示するかを指定する。
 :type sums: bool
 :param sumstext: 合計のラベルを指定する。
 :type sumstext: str
 :param colorline: バーとバーを繋げる線の色を指定する。
 :type colorline: ColorType
 :param linestyle: バーとバーを繋げる線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param ucolor: 上昇バーの色を指定する。
 :type ucolor: ColorType
 :param dcolor: 下降バーの色を指定する。
 :type dcolor: ColorType
 :param height: バーの幅を指定する。
 :type height: Numbertype'''
 def update(
self,
x:o_array,
y:o_array,
colorline:ColorType,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
ucolor:ColorType,
dcolor:ColorType,
height:Numbertype,
align:Literal['center','edge'],
)->NoReturn:'''横向きの滝グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Scatter(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
markersize:Numbertype=10,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''散布図を作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param marker: 散布図のマーカーを指定する。
 :type marker: Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
marker:str,
markersize:Numbertype,
linewidth:Numbertype,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''散布図を再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class DScatter(_3Gset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
z:o_array=...,
xlabel:str=...,
ylabel:str=...,
zlabel:str=...,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
markersize:Numbertype=10,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xyz:bool=True,
grid_x:bool=False,
grid_y:bool=False,
grid_z:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
zmajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
zticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
znumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelmouse_rotation:bool=True,
elev:Numbertype=30,
azim:Numbertype=45
)->None:'''3Dの散布図を作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param z: `z`のデータを指定する。
 :type z: o_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: str
 :param marker: 散布図のマーカーを指定する。
 :type marker: Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xyz: x軸,y軸,z軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`,`grid_z`より優先度が高い。
 :type grid_xyz: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_y: bool
 :param grid_z: z軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_z: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param zticksrange: z軸の目盛の範囲を変更する。
 :type zticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param zmajorint: z軸の目盛りを整数で自動調整させるか指定する。
 :type zmajorint: bool
 :param ticksshow: x軸,y軸,z軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param zticksshow: z軸のグリッド線と目盛り値について表示するかを指定する。
 :type zticksshow: bool
 :param znumticks: z軸の目盛りの数を指定する。
 :type znumticks: Numbertype|None
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param mouse_rotation: 表示されているグラフをマウスで操作できるか指定する。
 :type mouse_rotation: bool
 :param elev: 仰角を度数表記で指定する。
 :type elev: Numbertype
 :param azim: 方位角を度数表記で指定する。
 :type azim: Numbertype'''
 def update(
self,
x:o_array,
y:o_array,
z:o_array,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str,
marker:str,
markersize:Numbertype,
linewidth:Numbertype,
elev:Numbertype,
azim:Numbertype,
xlabel:str,
ylabel:str,
zlabel:str
)->NoReturn:'''3Dの散布図を再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
 def getz(self)->ndarray[_AnyShape,dtype[Any]]:'''`z`のデータを取得する。'''
class Stem(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
orientation:Literal['vertical','horizontal']='vertical',
bottom:Numbertype=0,
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...,
color:Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
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
 :type bottom: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
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
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
bottom:Numbertype,
orientation:Literal['horizontal','vertical'],
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...
)->NoReturn:'''幹図を再表示させる。'''
 def get(self)->list[StemContainer]:'''`StemContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Hist(_2Gset):
 def __init__(
self,
data:o_array=...,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
width:Numbertype=1,
min:Numbertype=...,
max:Numbertype=...,
decimalpoint:Numbertype=0,
orientation:Literal['vertical','horizontal']='vertical',
bottom:Numbertype=0,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']=10,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labely_verwrit:Literal['vertical','horizontal']='vertical'
)->None:'''ヒストグラムを作成する。

 :param data: dataのデータを指定する。
 :type data: o_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param width: ヒストグラムのバーのサイズを指定する。
 :type width: Numbertype
 :param orientation: ヒストグラムの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param bottom: ヒストグラムのバーの位置を指定する。
 :type bottom: Numbertype
 :param min: ヒストグラムで表示される最小値を指定する。
 :type min: Numbertype
 :param max: ヒストグラムで表示される最大値を指定する。
 :type max: Numbertype
 :param decimalpoint: ヒストグラムのbinの小数点を指定する。
 :type decimalpoint: Numbertype
 :param bins: binsを指定する。
 :type bins: int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
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
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']'''
 def update(
self,
data:o_array,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
decimalpoint:Numbertype,
graph_grid:ColorType,
title:str,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt'],
min:Numbertype,
max:Numbertype,
bottom:Numbertype,
orientation:Literal['horizontal','vertical'],
width:Numbertype
)->NoReturn:'''ヒストグラムを再表示させる。'''
 def get(self)->list[ndarray|list[ndarray],ndarray,BarContainer|Polygon|list[BarContainer|Polygon]]:'''`matplotlib.axes.Axes.hist`の戻り値を配列で返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
 @overload
 def getrange(self,num:bool)->tuple[float64,float64]|tuple[float,float]:'''ヒストグラムの`bins`の上限値と下限値をtuple型で返す。

 :param num: 戻り値内の数値がfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の上限値と下限値を返す。
 :rtype: tuple[float64,float64]|tuple[float,float]'''
 @overload
 def getrange(self,num:bool=True)->tuple[float64,float64]:'''ヒストグラムの`bins`の上限値と下限値をtuple型で返す。

 :param num: 戻り値内の数値がfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :return: ヒストグラムの`bins`の上限値と下限値を返す。
 :rtype: tuple[float64,float64]'''
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
 def __init__(
self,
data:n_array=...,
linewidth:Numbertype=2,
xlabel:str=...,
ylabel:str=...,
range:int|float|ListNumbertype2|TupleNumbertype2=...,
fill:bool=False,
baseline:Numbertype=0,
orientation:Literal['vertical','horizontal']='vertical',
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labely_verwrit:Literal['vertical','horizontal']='vertical',
label:labeltype=...
)->None:'''階段グラフを作成する。

 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param data: dataのデータを指定する。
 :type data: n_array
 :param linewidth: 線の幅を指定する。
 :type linewidth: Numbertype
 :param range: 階段の端の座標を配列もしくは数値で指定する。
 :type range: int|float|ListNumbertype2|TupleNumbertype2
 :param baseline: 階段の下端の開始位置を指定する。
 :type baseline: Numbertype
 :param fill: 階段の下部から`baseline`の間を塗りつぶすかを指定する。
 :type fill: bool
 :param orientation: グラフの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
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
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']'''
 def update(
self,
data:n_array,
linewidth:Numbertype,
range:int|float|ListNumbertype2|TupleNumbertype2,
fill:bool,
baseline:Numbertype,
orientation:Literal['horizontal','vertical'],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''階段グラフを再表示させる。'''
 def get(self)->list[StepPatch]:'''`StepPatch`の配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Stack(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']=None,
baseline:Literal['zero','sym','wiggle','weighted_wiggle']='zero',
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''積み上げエリアチャートを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param hatch: 塗りつぶし領域内の模様を指定する。
 :type hatch: Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']
 :param baseline: 基準値の算出方法を指定する。
 :type baseline: Literal['zero','sym','wiggle','weighted_wiggle']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||'],
baseline:Literal['zero','sym','wiggle','weighted_wiggle'],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str
)->NoReturn:'''積み上げエリアチャートを再表示させる。'''
 def get(self)->list[FillBetweenPolyCollection]:'''`FillBetweenPolyCollection`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Bubble(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
data:n_array=...,
bubblesize:Numbertype=1,
xlabel:str=...,
ylabel:str=...,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=0.5,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''バブルグラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param data: バブルグラフのバブルの大きさを指定する。
 :type data: n_array
 :param bubblesize: バブルの大きさの倍率を指定する。
 :type bubblesize: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param marker: バブルグラフのマーカーを指定する。
 :type marker: Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
bubblesize:Numbertype,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str,
marker:str,
markersize:Numbertype,
linewidth:Numbertype,
xlabel:str,
ylabel:str
)->NoReturn:'''バブルグラフを再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Linefill(_2Gset):
 def __init__(
self,
x:o_array=...,
ymin:n_array=...,
ymax:n_array=...,
centerlinewidth:Numbertype=2,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=0.5,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''積上げ面グラフを作成する。

 :param x: 曲線を定義する節点のx座標を指定する。
 :type x: o_array
 :param ymin: 最初の曲線を定義する節点のy座標を指定する。
 :type ymin: n_array
 :param ymax: 2つ目の曲線を定義する節点のy座標を指定する。
 :type ymax: n_array
 :param centerlinewidth: 線の太さを指定する。
 :type centerlinewidth: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
ymin:n_array,
ymax:n_array,
centerlinewidth:Numbertype,
xlabel:str,
ylabel:str,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''2つの水平曲線の間の領域を埋めるグラフを再表示させる。'''
 def get(self)->list[FillBetweenPolyCollection,Line2D]:'''`PathCollection`と`Line2D`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def getymin(self)->ndarray[_AnyShape,dtype[Any]]:'''`ymin`のデータを取得する。'''
 def getymax(self)->ndarray[_AnyShape,dtype[Any]]:'''`ymax`のデータを取得する。'''
class Ecdf(_2Gset):
 def __init__(
self,
data:n_array=...,
complementary:bool=False,
compress:bool=False,
orientation:Literal['vertical','horizontal']='vertical',
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':']='-',
linewidth:Numbertype=1.5,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''経験的累積分布関数を作成する。

 :param complementary: 補累積分布を描画するか指定する。
 :type complementary: bool
 :param compress: 同一値のデータをまとめて最適化するかどうか指定する。
 :type compress: bool
 :param orientation: プロットの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param linestyle: 線の種類を指定する。
 :type linestyle: Literal['dashdot','dashed','dotted','solid','-','--','-.',':']
 :param linewidth: 線の太さを指定する。
 :type linewidth: Numbertype
 :param data: 入力データを指定する。
 :type data: n_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:o_array,
complementary:bool,
compress:bool,
orientation:Literal['horizontal','vertical'],
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':'],
linewidth:Numbertype,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
decimalpoint:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''経験的累積分布関数を再表示させる。'''
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Errorbar(_2Gset):
 def __init__(
self,
x:n_array=...,
y:n_array=...,
err:o_array=...,
xerr:o_array=...,
yerr:o_array=...,
xuplims:bool=False,
xlolims:bool=False,
yuplims:bool=False,
ylolims:bool=False,
barsabove:bool=False,
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':']='solid',
marker:Literal['.','s','o','p','v','*','^','D']=None,
linewidth:Numbertype=1.5,
capthick:Numbertype=10,
capsize:Numbertype=0,
errorevery:int|list[int]|tuple[int]=1,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''誤差範囲付きの線グラフもしくはマーカーグラフ,あるいはその両方のエラーグラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param err: `x`と`y`のデータの誤差の配列を指定する。
 :type err: o_array
 :param xerr: `x`のデータの誤差の配列を指定する。
 :type xerr: o_array
 :param yerr: `y`のデータの誤差の配列を指定する。
 :type yerr: o_array
 :param xuplims: `x`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type xuplims: bool
 :param xlolims: `x`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type xlolims: bool
 :param yuplims: `y`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type yuplims: bool
 :param ylolims: `y`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type ylolims: bool
 :param barsabove: 誤差範囲をグラフ記号の上に表示させるか指定する。
 :type barsabove: bool
 :param linestyle: データ点とデータ点を結ぶ線の種類を指定する。
 :type linestyle: Literal['dashdot','dashed','dotted','solid','-','--','-.',':']
 :param marker: データ点のマーカーの種類を指定する。
 :type marker: Literal['.','s','o','p','v','*','^','D']
 :param linewidth: データ点を結ぶ線の太さを指定する。
 :type linewidth: Numbertype
 :param capthick: キャップの厚みを指定する。
 :type capthick: Numbertype
 :param capsize: エラーバーの先端にあるキャップの長さを指定する。
 :type capsize: Numbertype
 :param errorevery: エラーバーを表示する頻度を指定する。
 :type errorevery: int|list[int]|tuple[int]
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
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
linewidth:Numbertype,
capthick:Numbertype,
capsize:Numbertype,
errorevery:int|list[int]|tuple[int],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
decimalpoint:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''エラーグラフを再表示させる。'''
 def get(self)->list[ErrorbarContainer]:'''`ErrorbarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Eventplot(_2Gset):
 def __init__(
self,
data:o_array=...,
linewidth:Numbertype=1,
linelength:Numbertype=1,
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':']='solid',
orientation:Literal['vertical','horizontal']='vertical',
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''イベントグラフを作成する。

 :param data: `data`のデータを指定する。
 :type data: o_array
 :param linewidth: エラーバーの線の太さを指定する。
 :type linewidth: Numbertype
 :param linelength: 線の合計の高さを指定する。
 :type linelength: Numbertype
 :param linestyle: 線の種類を指定する。
 :type linestyle: Literal['dashdot','dashed','dotted','solid','-','--','-.',':']
 :param orientation: 向きを指定する。
 :type orientation: Literal['vertical','horizontal']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:o_array,
linewidth:Numbertype,
linelength:Numbertype,
orientation:Literal['vertical','horizontal'],
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':'],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''円グラフを再表示させる。'''
 def get(self)->list[EventCollection]:'''`EventCollection`の配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Hist2d(_2Gset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
max:Numbertype=...,
min:Numbertype=...,
xmax:Numbertype=...,
xmin:Numbertype=...,
ymax:Numbertype=...,
ymin:Numbertype=...,
bins:int|TupleInt2|ArrayLike|tuple[ArrayLike,ArrayLike]=...,
density:bool=False,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labely_verwrit:Literal['vertical','horizontal']='vertical'
)->None:'''2次元ヒストグラムを作成する。

 :param x: `x`のデータを一次元配列で指定する。
 :type x: o_array
 :param y: `y`のデータを一次元配列で指定する。
 :type y: o_array
 :param max,min: 表示させたいカウントの範囲を指定する。
 :type max,min: Numbertype
 :param xmax,xmin: x軸の`bins`の範囲を指定する。
 :type xmax,xmin: Numbertype
 :param ymax,ymin: y軸の`bins`の範囲を指定する。
 :type ymax,ymin: Numbertype
 :param bins: ビンの数を指定する。
 :type bins: int|tuple[int,int]|ArrayLike|tuple[ArrayLike,ArrayLike]
 :param density: ヒストグラムを正規化かするか指定する。
 :type density: bool
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
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
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :raises TypeError: `x`もしくは`y`もしくはその両方が二次元配列以上の多次元配列の場合に発生させる。
 :raises TypeError: `x`と`y`の要素の数が同じではない時に発生させる。'''
 def update(
self,
x:o_array,
y:o_array,
max:Numbertype,
min:Numbertype,
xmax:Numbertype,
xmin:Numbertype,
ymax:Numbertype,
ymin:Numbertype,
bins:int|TupleInt2|ArrayLike|tuple[ArrayLike,ArrayLike],
density:bool,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''2次元ヒストグラムを再表示させる。

 :raises TypeError: `x`もしくは`y`もしくはその両方が二次元配列以上の多次元配列の場合に発生させる。
 :raises TypeError: `x`と`y`の要素の数が同じではない時に発生させる。'''
 def get(self)->list[ndarray,ndarray,ndarray,QuadMesh]:'''`matplotlib.axes.Axes.hist2d`の戻り値を配列で返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Violinplot(_2Gset):
 def __init__(
self,
data:n_array=...,
x:o_array=...,
y:o_array=...,
orientation:Literal['vertical','horizontal']='vertical',
width:Numbertype=1,
showextrema:bool=True,
showmeans:bool=False,
showmedians:bool=False,
points:Numbertype=100,
bw_method:Literal['scott','silverman']|float|Callable[[GaussianKDE],float]='scott',
side:Literal['both','low','high']='both',
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''バイオリングラフを作成する。

 :param data: 入力データを指定する。
 :type data: n_array
 :param x: `orientation`が`vertical`の時にx軸上にバイオリンが設置される配列を指定する。
 :type x: n_array
 :param y: `orientation`が`horizontal`の時にy軸上にバイオリンが設置される配列を指定する。
 :type y: n_array
 :param orientation: バイオリンが設置される軸の向きを指定する。
 :type orientation: Literal['vertical','horizontal']
 :param width: バイオリンの幅を指定する。
 :type width: Numbertype
 :param showextrema: 極値を線で示すか指定する。
 :type showextrema: bool
 :param showmeans: 平均値を線で示すかどうか指定する。
 :type showmeans: bool
 :param showmedians: 中央値を線で示すかどうか指定する。
 :type showmedians: bool
 :param points: 各ガウスカーネル密度推定値を評価する点の数を指定する。
 :type points: Numbertype
 :param bw_method: 推定器の帯域幅を計算するために使用されるメソッドを指定する。
 :type bw_method: Literal['scott','silverman']|float|Callable[[GaussianKDE],float]
 :param side: バイオリンの左右対称もしくは左右(上下)のみを描画するか指定する。
 :type side: Literal['both','low','high']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:n_array,
x:o_array,
y:o_array,
orientation:Literal['vertical','horizontal'],
width:Numbertype,
showextrema:bool,
showmeans:bool,
showmedians:bool,
points:Numbertype,
bw_method:Literal['scott','silverman']|float|Callable[[GaussianKDE],float],
side:Literal['both','low','high'],
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
decimalpoint:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''バイオリングラフを再表示させる。'''
 def get(self)->list[dict[str,Collection]]:'''`matplotlib.axes.Axes.violinplot`のバイオリンプロットの各コンポーネントの辞書型が入った配列を返す。'''
 def getdata(self)->ndarray[_AnyShape,dtype[Any]]:'''`data`のデータを取得する。'''
class Hexbin(_2Gset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
c:o_array|None=None,
gridsize:int|tuple[int,int]=100,
extent:tuple[float,float,float,float]|None=None,
xscale:Literal['linear','log']='linear',
yscale:Literal['linear','log']='linear',
mincnt:int=1,
bins:Literal['log']|int|tuple[float,...]|None=None,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''2次元六角形グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param c: 各ポイントの値を指定する。
 :type c: o_array
 :param gridsize: `bins`の細かさを指定する。
 :type gridsize: int|tuple[int,int]
 :param extent: 各ポイントの値を指定する。
 :type extent: tuple[float,float,float,float]|None
 :param xscale,yscale: 軸のスケールを指定する。
 :type xscale,yscale: Literal['linear','log']
 :param mincnt: 描画する`bins`の最小カウント数を指定する。
 :type mincnt: int
 :param bins: ビンのカウント方法を指定する。
 :type bins: Literal['log']|int|tuple[float,...]|None
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
y:o_array,
c:o_array|None,
gridsize:int|tuple[int,int],
extent:tuple[float,float,float,float]|None,
xscale:Literal['linear','log'],
yscale:Literal['linear','log'],
mincnt:int,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
decimalpoint:Numbertype,
graph_grid:ColorType,
title:str
)->NoReturn:'''2次元六角形グラフを再表示させる。'''
 def get(self)->list[PolyCollection]:'''`PolyCollection`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''
class Hatplot(_2Gset):
 def __init__(
self,
x:o_array,
data:o_array,
color:ColorType='#4477aa',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
master:Misc=None
)->None:'''ハットグラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param data: `data`のデータを指定する。
 :type data: o_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
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
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
data:o_array,
label:labeltype,
color:ColorType,
fg:ColorType,
bg:ColorType,
alpha:Numbertype,
xlabel:str,
ylabel:str,
graph_grid:ColorType,
title:str,
)->NoReturn:'''ハットグラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->ndarray[_AnyShape,dtype[Any]]:'''`x`のデータを取得する。'''
 def gety(self)->ndarray[_AnyShape,dtype[Any]]:'''`y`のデータを取得する。'''