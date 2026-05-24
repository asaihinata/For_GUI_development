from matplotlib.container import BarContainer
from ....typing import *
from .._2gset import _2Gset
__all__=['Hatplot']
class Hatplot(_2Gset):
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->Typeget_data:'''`x`のデータを取得する。'''
 def getdata(self)->Typeget_data:'''`data`のデータを取得する。'''