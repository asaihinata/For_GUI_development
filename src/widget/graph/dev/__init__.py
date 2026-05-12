import japanize_matplotlib
import numpy as np
from ...typing import *
from ..._function import *
from ..base import threeElement,twoElement,polarElement
from ..base.lists import *
from ..base.style import *
class Angle:
 def __init__(self,angle,dtype=True):
  if not isinstance(angle,bool|float|int|np.float16|np.float32|np.float64|np.int16|np.int32|np.int64|np.int8|np.uint16|np.uint32|np.uint64|np.uint8):
   raise TypeError('angleには数値の型を指定してください')
  if isinstance(dtype,bool) and dtype:self.angle=np.rad2deg(angle) # rad to deg
  else:self.angle=np.deg2rad(angle) # deg to rad
 def __str__(self):return str(self.angle)
 def __int__(self):return int(self.angle)
 def __float__(self):return float(self.angle)
 def __eq__(self,val):return self.angle==val
 def __ne__(self,val):return self.angle!=val
 def __lt__(self,val):return self.angle<val
 def __le__(self,val):return self.angle<=val
 def __gt__(self,val):return self.angle>val
 def __ge__(self,val):return self.angle>=val
class Rad(Angle):
 def __init__(self,angle):
  if isinstance(angle,Rad|Deg):angle=angle.angle
  super().__init__(angle)
class Deg(Angle):
 def __init__(self,angle):
  if isinstance(angle,Rad|Deg):angle=angle.angle
  super().__init__(angle,False)
def mod(a:int|float,b:int|float)->TupleNumbertype2:
 '''整数除算と除算をtuple型で返す。

 :param a: 割られる数を指定する。
 :type a: int|float
 :param b: 割る数を指定する。
 :type b: int|float
 :rtype: TupleNumbertype2'''
 return(a//b,a%b)
def datareversed(data:np.ndarray|list|tuple)->np.ndarray|list|tuple:
 '''配列の逆順を返す。

 :param data: 逆順したい配列を指定する。
 :type data: np.ndarray|list|tuple
 :rtype: np.ndarray|list|tuple'''
 if isinstance(data,list):return data.reverse()
 if isinstance(data,tuple|np.ndarray):return data[::-1]
 return data