from os import PathLike
from pathlib import Path
from tkinter import Misc
from matplotlib.container import BarContainer
from matplotlib.projections.polar import PolarAxes
from matplotlib.container import StemContainer
from numpy import ndarray
from ...typing import *
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
 def __init__(
self,
x:o_array=...,
y:o_array=...,
data:o_array=...,
logs:bool=False,
align:Literal['center','edge']='center',
width:Type_Number=1,
alpha:Type_Number=1,
color:ColorTypes|tuple[ColorTypes,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorTypes='#000000',
bg:ColorTypes='#ffffff',
title:str=...,
titlealpha:Type_Number=1.0,
titlezorder:Type_Number=4,
titlefg:ColorTypes=...,
titleha:Literal['left','center','right']|None=None,
titleva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
titlerotation:float|Literal['vertical','horizontal']|None='horizontal',
titlerotation_mode:bool=True,
titlefontname:str|Type_Iterablestr|None=None,
titlefontpath:str|PathLike|Path|None=None,
dpi:Type_Number=100,
graph_grid:ColorTypes='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:Type_Number|tuple[int|tuple,...]=0,
yticksrange:Type_Number|tuple[int|tuple,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
master:Misc=None
)->None:'''極軸棒グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param data: `data`のデータを指定する。
 :type data: o_array
 :param logs: y軸を対数スケールにするかを指定する。
 :type logs: bool
 :param width: 棒グラフのバー幅を指定する。
 :type width: Type_Number
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param titlealpha: グラフの透明度を指定する。
 :type titlealpha: Type_Number
 :param titlezorder: グラフのタイトルの重なりの順を指定する。
 :type titlezorder: Type_Number
 :param titlefg: グラフのタイトルの文字色を指定する。
 :type titlefg: ColorTypes
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
 :param color: 色を指定する。
 :type color: ColorTypes|tuple[ColorTypes,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorTypes
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorTypes
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Type_Number
 :param alpha: グラフの透明度を指定する。
 :type alpha: Type_Number
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorTypes
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: Type_Number|tuple[int|tuple,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: Type_Number|tuple[int|tuple,...]
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
 :type yticksdirection: Literal['out','in','inout']'''
 def update(
self,
x:o_array,
y:o_array,
data:o_array,
logs:bool,
align:Literal['center','edge'],
width:Type_Number,
fg:ColorTypes,
bg:ColorTypes,
alpha:Type_Number,
graph_grid:ColorTypes,
title:str
)->NoReturn:'''極軸棒グラフを再表示させる。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
class Stempolar(_polarset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
data:o_array=...,
linefmt:str|None=None,
markerfmt:str|None=None,
basefmt:str|None=None,
bottom:Type_Number=0,
alpha:Type_Number=1,
size:TupleNumbertype2=(500,400),
fg:ColorTypes='#000000',
bg:ColorTypes='#ffffff',
title:str=...,
titlealpha:Type_Number=1.0,
titlezorder:Type_Number=4,
titlefg:ColorTypes=...,
titleha:Literal['left','center','right']|None=None,
titleva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
titlerotation:float|Literal['vertical','horizontal']|None='horizontal',
titlerotation_mode:bool=True,
titlefontname:str|Type_Iterablestr|None=None,
titlefontpath:str|PathLike|Path|None=None,
dpi:Type_Number=100,
graph_grid:ColorTypes='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:Type_Number|tuple[int|tuple,...]=0,
yticksrange:Type_Number|tuple[int|tuple,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
master:Misc=None
)->None:'''極軸幹図を作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param data: `data`のデータを指定する。
 :type data: o_array
 :param linefmt: 垂直線の色や線を指定する。
 :type linefmt: str|None
 :param markerfmt: 茎の先端にあるマーカーの色や形状を指定する。
 :type markerfmt: str|None
 :param basefmt: ベースラインのプロパティを指定する。
 :type basefmt: str|None
 :param bottom: ベースラインの座標を指定する。
 :type bottom: Type_Number
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param titlealpha: グラフの透明度を指定する。
 :type titlealpha: Type_Number
 :param titlezorder: グラフのタイトルの重なりの順を指定する。
 :type titlezorder: Type_Number
 :param titlefg: グラフのタイトルの文字色を指定する。
 :type titlefg: ColorTypes
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
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorTypes
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorTypes
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Type_Number
 :param alpha: グラフの透明度を指定する。
 :type alpha: Type_Number
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorTypes
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: Type_Number|tuple[int|tuple,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: Type_Number|tuple[int|tuple,...]
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
 :type yticksdirection: Literal['out','in','inout']'''
 def update(
self,
x:o_array,
y:o_array,
data:o_array,
linefmt:str|None,
markerfmt:str|None,
basefmt:str|None,
bottom:Type_Number,
fg:ColorTypes,
bg:ColorTypes,
alpha:Type_Number,
graph_grid:ColorTypes,
title:str
)->NoReturn:'''極軸幹図を再表示させる。'''
 def get(self)->list[StemContainer]:'''`StemContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''