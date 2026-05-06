from tkinter import Misc
from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import float64,ndarray
from ....typing import *
class GElement:
 master:Misc
 fig:Figure
 graphdata:list
 size:TupleNumbertype2
 fg:ColorType
 graph_bg:ColorType
 graph_grid:ColorType
 title:str
 dpi:int|float
 alpha:int|float
 ax:Axes|Axes3D
 color:list[str]
 def __init__(
self,
master:Misc=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
graph_grid:ColorType='#b7b7b7',
title:str=...,
dpi:int|float=100,
alpha=1
)->None:
  '''2Dグラフと3Dグラフの基盤のグラフを作成する。
 :param size: グラフの大きさをタプルで指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param graph_grid: グラフ内の線を指定する。
 :type graph_grid: ColorType
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param dpi: グラフの解像度を指定する。
 :type dpi: int|float'''
  self.fig:Figure
  self._canvas_widget:None
  self.graphdata:list
  self.size:TupleNumbertype2
  self.fg:ColorType
  self.graph_bg:ColorType
  self.graph_grid:ColorType
  self.title:str
  self.dpi:int|float
  self.alpha:int|float
  self.ax:Axes|Axes3D
  self.max_depth:int
 def photo(
self,
filename:str='Graph',
ex:Literal['.eps','.jpg','.jpeg','.pdf','.pgf','.png','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']='.png',
dpi:int|float=100
)->NoReturn:'''グラフを画像にして画像を保存する。
 :param filename: 画像を保存するファイル名を指定する。
 :type filename: str
 :param ex: 画像ファイルの拡張子を指定する。
 :type ex: Literal['.eps','.jpg','.jpeg','.pdf','.pgf','.png','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']
 :param dpi: グラフの解像度を指定する。
 :type dpi: int|float
 :return:
 :rtype: NoReturn'''
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
 def _color_check(self,color:list)->list:...
 def _list_loop(self,lin:list|tuple,num:int)->list:...
 def legend(self,ncols:int|float=1)->NoReturn:...
 def _anchor(
self,
val:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=None,
other:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=None
)->None:'''凡例の位置を決定する。'''
 def _getlegendplace(
self,
place:str|int=...,
other:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right'
)->str:'''凡例の位置の基準を決定する。'''
 def pielabel(self,data:ndarray|list|tuple,label:list|tuple)->list:...
 def labels(self,label:labeltype)->list:...
 def markers(self,serch:str)->str:'''`serch`で指定したマーカーが`MARKERS`に存在するかを調べる
 :param serch: `MARKERS`に調べたいマーカーを指定する。
 :type serch: str
 :return:
 :rtype: str
参考
----
* https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers'''
 def lines(self,serch:str)->str:'''serch`で指定した枠線が`FMTSOLID`に存在するかを調べる
 :param serch: `FMTSOLID`に調べたいを指定する。
 :type serch: str
 :return:
 :rtype: str'''
 def nlines(self,serch:str)->str:'''serch`で指定した枠線が`SOLID`に存在するかを調べる
 :param serch: `SOLID`に調べたいを指定する。
 :type serch: str
 :return:
 :rtype: str
参考
----
* https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html'''
 def _arr(self,val:ndarray|list|tuple,j:bool=True)->ndarray:'''
 :param val: 配列を指定する。
 :type val: ndarray|list|tuple
 :raises TypeError: NpArraytype型以外を指定した場合に発生させる。
 :return:
 :rtype: ndarray'''
 def _floatarr(self,val:ndarray|list|tuple)->ndarray:...
 def _manyarr(self,val:ndarray|list|tuple,j:bool=True)->ndarray:...
 def _onearr(self,val:ndarray|list|tuple,j:bool=True)->ndarray:...
 def _dataarr(self,val:ndarray|list|tuple,j:bool=True)->ndarray:...
 def _pack(self)->NoReturn:'''ウィジェットを親ウィジェット内に配置します。'''
 def _redraw(self)->NoReturn:...
 def _size(self,sizes:TupleNumbertype2=(500,400))->TupleNumbertype2:'''グラフの大きさのサイズを定める。
 :param sizes: グラフの大きさを指定する。
 :type sizes: TupleNumbertype2
 :return: 決定したグラフの大きさをタプルで返す。
 :rtype: TupleNumbertype2'''
 def _apply_theme_colors(self)->NoReturn:'''目盛り,目盛りラベル,グリッド線,グラフのタイトル,軸ラベルの文字色を決定させる。'''
 def _adjustment(self)->NoReturn:'''グラフの調整を行う'''
class twoDElement(GElement):
 def __init__(
self,
master:Misc=None,
data:ndarray|list|tuple=None,
x:ndarray|list|tuple=None,
y:ndarray|list|tuple=None,
label:labeltype=None,
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
setxy:bool=True
)->None:
  '''2Dグラフの基盤のグラフを作成する。
 :param data: dataを指定する。
 :type data: ndarray|list|tuple
 :param x: x軸のデータを指定する。
 :type x: ndarray|list|tuple
 :param y: y軸のデータを指定する。
 :type y: ndarray|list|tuple
 :param label: グラフのラベルを指定する。
 :type label: labeltype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param xticksshow: x軸の目盛りを線を表示させるか指定する。
 :type xticksshow: bool
 :param yticksshow: y軸の目盛りを線を表示させるか指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout'] '''
  self.ax:Axes
  self.x:ndarray
  self.y:ndarray
  self.data:ndarray
  self.label:labeltype
  self.xlabel:labeltype
  self.ylabel:labeltype
  self.grid_xy:bool
  self.grid_x:bool
  self.grid_y:bool
  self.y_verwrit:str
  self.xmajorint:bool
  self.ymajorint:bool
 def _updates(
self,
fg:ColorType,
bg:ColorType,
graph_grid:ColorType,
title:str,
xlabel:labeltype,
ylabel:labeltype
)->NoReturn:...
 def _apply_labels(
self,
xlabel:labeltype=None,
ylabel:labeltype=None
)->NoReturn:'''2Dのグラフのx軸,y軸のラベルを作成する。
 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :return:
 :rtype: NoReturn'''
 def clear(self)->NoReturn:'''グラフ内のグラフをクリアする。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:'''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:'''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:'''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:'''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''
class threeDElement(GElement):
 def __init__(
self,
master:Misc=None,
x:ndarray|list|tuple=None,
y:ndarray|list|tuple=None,
z:ndarray|list|tuple=None,
label:labeltype=None,
grid_xyz:bool=True,
grid_x:bool=False,
grid_y:bool=False,
grid_z:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
zmajorint:bool=True,
elev:int|float=30,
azim:int|float=45,
mouse_rotation:bool=True,
xticksshow:bool=False,
yticksshow:bool=False,
zticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out'
)->None:
  '''3Dのグラフを作成する。
 :param x: x軸のデータを指定する。
 :type x: ndarray|list|tuple
 :param y: y軸のデータを指定する。
 :type y: ndarray|list|tuple
 :param z: z軸のデータを指定する。
 :type z: ndarray|list|tuple
 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: labeltype
 :param grid_xyz: x軸,y軸,z軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`,`grid_z`より優先度が高い。
 :type grid_xyz: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_y: bool
 :param grid_z: z軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_z: bool
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param zmajorint: z軸の目盛りを整数で自動調整させるか指定する。
 :type zmajorint: bool
 :param mouse_rotation: グラフをマウスでできるか指定する。
 :type mouse_rotation: bool
 :param elev: 仰角を度数表記で指定する。
 :type elev: int|float
 :param azim: 方位角を度数表記で指定する。
 :type azim: int|float
 :param xticksshow: x軸の目盛りを線を表示させるか指定する。
 :type xticksshow: bool
 :param yticksshow: y軸の目盛りを線を表示させるか指定する。
 :type yticksshow: bool
 :param zticksshow: z軸の目盛りを線を表示させるか指定する。
 :type zticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']'''
  self.ax:Axes3D
  self.x:ndarray|list|tuple
  self.y:ndarray|list|tuple
  self.z:ndarray|list|tuple
  self.label:labeltype
  self.xlabel:labeltype
  self.ylabel:labeltype
  self.zlabel:labeltype
  self.grid_xyz:bool
  self.grid_x:bool
  self.grid_y:bool
  self.grid_z:bool
  self.xmajorint:bool
  self.ymajorint:bool
  self.zmajorint:bool
  self.elev:int|float
  self.azim:int|float
 def _updates(
self,
fg:ColorType,
bg:ColorType,
graph_grid:ColorType,
title:str,
elev:int|float,
azim:int|float,
xlabel:labeltype,
ylabel:labeltype,
zlabel:labeltype
)->NoReturn:...
 def _apply_labels(
self,
xlabel:labeltype=None,
ylabel:labeltype=None,
zlabel:labeltype=None
)->NoReturn:'''3Dのグラフのx軸,y軸,z軸のラベルを作成する。
 :param xlabel: x軸のラベルを指定する。
 :type label: labeltype
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: labeltype
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: labeltype'''
 def _apply_grid(self)->NoReturn:'''グリッド線を加えるメソッド。'''
 def clear(self)->NoReturn:'''グラフ内のグラフをクリアする。'''
 def invert(self)->NoReturn:'''x軸,y軸,z軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def invert_z(self)->NoReturn:'''z軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64],
tuple[float64,float64]
]:'''x軸,y軸,z軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:'''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:'''y軸の下限値と上限値を昇順で返す。'''
 def getzbound(self)->tuple[float64,float64]:'''z軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray,ndarray]:'''x軸,y軸,z軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:'''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:'''y軸の目盛りの位置を座標で返します。'''
 def getzticks(self)->ndarray:'''z軸の目盛りの位置を座標で返します。'''