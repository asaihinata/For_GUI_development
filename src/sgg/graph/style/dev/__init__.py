import numpy as np
from ...typing import Type_Numberlike
from ....nparray import *
__all__=['bol','bols','listchose','list2float','list2number','num0','num0s','num1s','range_zero_one','Angle','Deg','Rad']
class Angle:
 def __init__(self,angle,dtype=True):
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
def range_zero_one(val,out=1.0,endpoint=True):
 if not isinstance(val,Type_Numberlike):return out
 if not isinstance(endpoint,bool):endpoint=True
 if endpoint and 0<=val<=1:return val
 elif not endpoint and 0<=val<1:return val
 return out
def num1s(val=0,mins=1):
 if isinstance(val,Type_Numberlike) and 1<=val:return val
 return mins
def num0s(val=0,mins=0):
 if isinstance(val,Type_Numberlike)and 0<=val:return val
 return mins
def num0(val=0,mins=0):
 if isinstance(val,Type_Numberlike)and 0<val:return val
 return mins
def list2number(lin=None):
 if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,Type_Numberlike)for i in lin):return True
 return False
def list2float(lin=None):
 if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,float)for i in lin):return True
 return False
def bol(vals,other=False):
 if isinstance(vals,bool):return vals
 return other
def bols(bools,trus=None,fals=None):
 if isinstance(bools,bool):return trus
 return fals
def listchose(val,arr,other=None):
 if isinstance(arr,tuple|list)and other==None:other=arr[0]
 elif not isinstance(arr,tuple|list)and other==None:other=arr
 if val in arr:return val
 return other