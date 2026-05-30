'''グラフの線を設定するモジュール'''
from ....nparray import NPString
from ..fmt import FMT
__all__=['Solid','Solidlist','fmtSolid']
class Solid:
 stlye=['-','--','-.',':','None',' ','']
 def __init__(self,solid):
  self.solid=solid if solid in self.stlye else '-'
class Solidlist(NPString):
 def __init__(self,solid):
  if isinstance(solid,str):solid=[solid]
  super().__init__(solid,depth_limit=1)
 def __iter__(self):return iter(self.data)
 def __getitem__(self,key):return self.get(key)
 def __str__(self):return str(self.data[0])
class fmtSolid:
 def __init__(self,fmtmarker=None,fmtsolid=None,fmtcolor=None):
  self.solid=FMT(fmtmarker,fmtsolid,fmtcolor).fmt_txt