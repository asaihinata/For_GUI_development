from matplotlib.collections import PathCollection
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import ndarray
from ...typing import *
__all__=[
'DScatter'
]
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
 def update(
self,
x:o_array,
y:o_array,
z:o_array,
fg:ColorType,
bg:ColorType,
alpha:int|float,
graph_grid:ColorType,
title:str,
marker:str,
markersize:int|float,
linewidth:int|float,
elev:int|float,
azim:int|float,
xlabel:str,
ylabel:str,
zlabel:str
)->NoReturn:'''3Dの散布図を再表示させる。'''
 def get(self)->list[PathCollection]:'''`PathCollection`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def gety(self)->Typeget_data:'''`y`のデータを取得する。'''
 def getz(self)->Typeget_data:'''`z`のデータを取得する。'''