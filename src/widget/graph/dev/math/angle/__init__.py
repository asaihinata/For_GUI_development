import numpy as np
from ...typing import *
__all__:list[str]=['Angle','Deg','Rad']
class Angle:
 def __init__(self,angle:Type_Numberlike,dtype:bool=True)->None:
  if not isinstance(angle,Type_Numberlike):
   raise TypeError('angleには数値の型を指定してください')
  if isinstance(dtype,bool) and dtype:self.angle=np.rad2deg(angle) # rad to deg
  else:self.angle=np.deg2rad(angle) # deg to rad
 def __str__(self)->str:return str(self.angle)
 def __int__(self)->int:return int(self.angle)
 def __float__(self)->float:return float(self.angle)
 def __eq__(self,val:Type_Numberlike)->bool:return self.angle==val
 def __ne__(self,val:Type_Numberlike)->bool:return self.angle!=val
 def __lt__(self,val:Type_Numberlike)->bool:return self.angle<val
 def __le__(self,val:Type_Numberlike)->bool:return self.angle<=val
 def __gt__(self,val:Type_Numberlike)->bool:return self.angle>val
 def __ge__(self,val:Type_Numberlike)->bool:return self.angle>=val
class Rad(Angle):
 def __init__(self,angle:Type_Numberlike|Rad|Deg)->None:
  if isinstance(angle,Rad|Deg):angle=angle.angle
  super().__init__(angle)
class Deg(Angle):
 def __init__(self,angle:Type_Numberlike|Rad|Deg)->None:
  if isinstance(angle,Rad|Deg):angle=angle.angle
  super().__init__(angle,False)