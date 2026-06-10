'''グラフの線を設定するモジュール'''
from ....nparray import NPArray

__all__=['Solid','Solidlist']
class Solid:
 def __init__(self,solid):
  self.__solid=solid if solid in ['-','--','-.',':','None',' ',''] else '-'
 @property
 def solid(self):return self.__solid
class Solidlist(NPArray):
 def __init__(self,solid):
  if isinstance(solid,str):solid=[solid]
  super().__init__(solid,depth_limit=1)
 def __iter__(self):return iter(self.data)
 def __str__(self):return str(self.data[0])
 def __repr__(self):return f'Solidlist({self.data})'
 def __getitem__(self,key):return self.get(key)