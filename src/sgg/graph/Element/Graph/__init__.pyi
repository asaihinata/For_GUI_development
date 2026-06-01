from collections.abc import Iterator
from os import PathLike
from pathlib import Path
from tkinter import Misc
from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.projections.polar import PolarAxes
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import ndarray
from ....nparray import NPArray
from ...typing import *
__all__=['GElement','getLabel']
class getLabel(NPArray):
 label:ndarray
 def __init__(self,label:list|tuple|ndarray|None=None)->None:...
 def __iter__(self)->Iterator[Any|None]:...
 def __getitem__(self,val:int)->Any:...
 def __bool__(self)->bool:...
 def __repr__(self)->str:...
class GElement:
 labelfont:FontProperties
 tight_layout:bool
 ticksshow:bool
 label:getLabel
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
 ax:Axes|Axes3D|PolarAxes
 color:list[str]
 max_depth:int
 titlealpha:int|float
 titlezorder:int|float
 titlefg:ColorTypeN
 titleha:Literal['left','center','right']|None
 titleva:Literal['bottom','baseline','center','center_baseline','top']|None
 titlerotation:float|Literal['horizontal','vertical']|None
 titlerotation_mode:bool
 titlefontname:str|Type_Iterablestr|None
 titlefontpath:str|PathLike|Path|None
 def photo(
self,
filename:str='Graph',
ex:Literal['.eps','.jpg','.jpeg','.pdf','.pgf','.png','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']='.png',
dpi:int|float=100
):'''グラフを画像にして画像を保存する。

 :param filename: 画像を保存するファイル名を指定する。
 :type filename: str
 :param ex: 画像ファイルの拡張子を指定する。
 :type ex: Literal['.eps','.jpg','.jpeg','.pdf','.pgf','.png','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']
 :param dpi: グラフの解像度を指定する。
 :type dpi: int|float'''
 def set_title(self,title:str)->None:
  '''グラフにタイトルを設置する'''
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
 def legend(self):...
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
 def _pack(self):'''ウィジェットを親ウィジェット内に配置します。'''
 def _redraw(self):...
 def _size(self,sizes:TupleNumbertype2=(500,400))->TupleNumbertype2:'''グラフの大きさのサイズを定める。

 :param sizes: グラフの大きさを指定する。
 :type sizes: TupleNumbertype2
 :return: 決定したグラフの大きさをタプルで返す。
 :rtype: TupleNumbertype2'''
 def _apply_theme_colors(self):'''目盛り,目盛りラベル,グリッド線,グラフのタイトル,軸ラベルの文字色を決定させる。'''
 def _list_loop(self,lin:ndarray|list|tuple,num:int)->list:...