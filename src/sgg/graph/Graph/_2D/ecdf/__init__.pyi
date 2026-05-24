from ....typing import *
from .._2gset import _2Gset
from matplotlib.lines import Line2D
__all__=['Ecdf']
class Ecdf(_2Gset):
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''