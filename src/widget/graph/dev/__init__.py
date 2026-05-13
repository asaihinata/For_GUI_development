from typing import TypeAlias
import japanize_matplotlib
import numpy as np
from matplotlib.pyplot import cm,rcParams
from ..._function import *
from ...typing import *
from ..base import polarElement,threeElement,twoElement
from ..base.lists import *
from ..base.style import *
Listlike:TypeAlias=list|tuple
nListlike:TypeAlias=np.ndarray|list|tuple
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
def mod(a:Type_Number,b:Type_Number)->TupleNumbertype2:
 '''整数除算と除算をtuple型で返す。

 :param a: 割られる数を指定する。
 :type a: Type_Number
 :param b: 割る数を指定する。
 :type b: Type_Number
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