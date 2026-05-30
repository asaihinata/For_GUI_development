from matplotlib.container import BarContainer
from matplotlib.patches import Polygon
from ....typing import *
from .._2gset import _2Gset
__all__=['Hist']
class Hist(_2Gset):
 def update(
self,
data:o_array,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt'],
min:int|float,
max:int|float,
bottom:int|float,
orientation:Literal['horizontal','vertical'],
width:int|float,
fg:ColorType,
bg:ColorType,
alpha:int|float,
decimalpoint:int|float,
graph_grid:ColorType,
title:str
):'''ヒストグラムを再表示させる。'''
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