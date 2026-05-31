from itertools import product
from ...dev import *
__all__=['SSBarhGraph']
class SSBarhGraph(twoElement):
 def update(self,data=None,dataname=None,**kw):'''横並び棒グラフを再描画する。'''
 def get(self):return self.graphdata
 def getx(self):return self.data
 def gety(self):return self.dataname