from os import PathLike
from pathlib import Path
from matplotlib.collections import PathCollection
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import ndarray
from ...typing import *
class _3Gset:
 ax:Axes3D
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
 def invert(self)->NoReturn:'''x軸,y軸,z軸の軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸の軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸の軸を反転させる。'''
 def invert_z(self)->NoReturn:'''z軸の軸を反転させる。'''
 def getbound(self)->tuple[
Typetuple_float64,
Typetuple_float64,
Typetuple_float64
]:'''x軸,y軸,z軸の順で表示されている範囲の下限値と上限値を返す。

 :return: x軸,y軸,z軸の順で表示されている範囲の下限値と上限値のtupleを返す。
 :rtype: tuple[Typetuple_float64,Typetuple_float64,Typetuple_float64]'''
 def getxbound(self)->Typetuple_float64:'''表示されているx軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているx軸の範囲の下限値と上限値のtupleを返す。
 :rtype: Typetuple_float64'''
 def getybound(self)->Typetuple_float64:'''表示されているy軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているy軸の範囲の下限値と上限値のtupleを返す。
 :rtype: Typetuple_float64'''
 def getzbound(self)->Typetuple_float64:'''表示されているz軸の範囲の下限値と上限値を昇順で返す。

 :return: 表示されているz軸の範囲の下限値と上限値のtupleを返す。
 :rtype: Typetuple_float64'''
 def getticks(self)->tuple[ndarray,ndarray,ndarray]:'''x軸,y軸,z軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''
 def getzticks(self)->ndarray:'''z軸の目盛りの位置を座標で返します。'''
class DScatter(_3Gset):
 def __init__(
self,
x:o_array=...,
y:o_array=...,
z:o_array=...,
xlabel:str=...,
xlabelalpha:Type_Number=1.0,
xlabelzorder:Type_Number=4,
xlabelfg:ColorTypes=...,
xlabelha:Literal['left','center','right']|None=None,
xlabelva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
xlabelrotation:float|Literal['vertical','horizontal']|None='horizontal',
xlabelrotation_mode:bool=True,
xlabelfontname:str|Type_Iterablestr|None=None,
xlabelfontpath:str|PathLike|Path|None=None,
ylabel:str=...,
ylabelalpha:Type_Number=1.0,
ylabelzorder:Type_Number=4,
ylabelfg:ColorTypes=...,
ylabelha:Literal['left','center','right']|None=None,
ylabelva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
ylabelrotation:float|Literal['vertical','horizontal']|None='vertical',
ylabelrotation_mode:bool=True,
ylabelfontname:str|Type_Iterablestr|None=None,
ylabelfontpath:str|PathLike|Path|None=None,
zlabel:str=...,
zlabelalpha:Type_Number=1.0,
zlabelzorder:Type_Number=4,
zlabelfg:ColorTypes=...,
zlabelha:Literal['left','center','right']|None=None,
zlabelva:Literal['bottom','baseline','center','center_baseline','top']|None=None,
zlabelrotation:float|Literal['vertical','horizontal']|None='vertical',
zlabelrotation_mode:bool=True,
zlabelfontname:str|Type_Iterablestr|None=None,
zlabelfontpath:str|PathLike|Path|None=None,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
markersize:Type_Number=10,
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
alpha:Type_Number=1,
graph_grid:ColorTypes='#b7b7b7',
grid_xyz:bool=True,
grid_x:bool=False,
grid_y:bool=False,
grid_z:bool=False,
tight_layout:bool=True,
xticksrange:Type_Number|tuple[int|tuple,...]=0,
yticksrange:Type_Number|tuple[int|tuple,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
zmajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
zticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
znumticks:Type_Number|None=None,
legendanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
legendplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
legendtitle:str=...,
legendframe:bool=True,
legendshadow:bool=False,
labelmouse_rotation:bool=True,
elev:Type_Number=30,
azim:Type_Number=45
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
 :type markersize: Type_Number
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
 :type xticksrange: Type_Number|tuple[int|tuple,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: Type_Number|tuple[int|tuple,...]
 :param zticksrange: z軸の目盛の範囲を変更する。
 :type zticksrange: Type_Number|tuple[int|tuple,...]
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
 :type znumticks: Type_Number|None
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
 :type legendalpha: Type_Number
 :param mouse_rotation: 表示されているグラフをマウスで操作できるか指定する。
 :type mouse_rotation: bool
 :param elev: 仰角を度数表記で指定する。
 :type elev: Type_Number
 :param azim: 方位角を度数表記で指定する。
 :type azim: Type_Number'''
 def update(
self,
x:o_array,
y:o_array,
z:o_array,
fg:ColorTypes,
bg:ColorTypes,
alpha:Type_Number,
graph_grid:ColorTypes,
title:str,
marker:str,
markersize:Type_Number,
linewidth:Type_Number,
elev:Type_Number,
azim:Type_Number,
xlabel:str,
ylabel:str,
zlabel:str
)->NoReturn:'''3Dの散布図を再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
 def getz(self)->Typeget_data:'''`z`のデータを取得する。'''