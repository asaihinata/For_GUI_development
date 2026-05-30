'''グラフの線を設定するモジュール'''
from ..fmt import FMT
from ....nparray import NPString
__all__=['Solid','Solidlist','fmtSolid']
class Solid:
 stlye=['-','--','-.',':','None',' ','']
 def __init__(self,solid):
  self.solid=solid if solid in self.stlye else '-'
class Solidlist:
 def __init__(self,solid):
  self.solid=[Solid(i).solid for i in NPString([solid] if isinstance(solid,str) else solid)]
 def __iter__(self):return iter(self.solid)
class fmtSolid:
 def __init__(self,fmtmarker=None,fmtsolid=None,fmtcolor=None):
  self.solid=FMT(fmtmarker,fmtsolid,fmtcolor).fmt_txt