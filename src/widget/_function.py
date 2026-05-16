from ._color import Color
__all__=['allNone','allNones','bols','Color','ints','intsmin','listchose','nums','numsmin','parsecolor','typelist','int0','int0s','int1s','list2float','list2int','list2num','list4float','list4int','list4num','num0','num0s','num1s','range_num']
def allNone(a,b=None):return True if a is None and b is None else False
def allNones(a,b=None,other=None):
 if (a is not None and b is not None) or (a is not None and b is None):return a
 elif (a is None and b is not None):return b
 return other
def list2num(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,int|float)for i in lin) else False
def list2int(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,int)for i in lin) else False
def list2float(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,float)for i in lin) else False
def list4num(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==4 and all(isinstance(i,int|float)for i in lin) else False
def list4int(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==4 and all(isinstance(i,int)for i in lin) else False
def list4float(lin=None):return True if isinstance(lin,list|tuple) and len(lin)==4 and all(isinstance(i,float)for i in lin) else False
def typelist(val):
 if isinstance(val,tuple|list):return True
 return False
def listchose(val,arr,other=None):
 if isinstance(arr,tuple|list)and other==None:other=arr[0]
 elif not isinstance(arr,tuple|list)and other==None:other=arr
 if val in arr:return val
 return other
def numsmin(val,mins=0,other=None):
 if not isinstance(val,int|float) or not isinstance(mins,int|float):
  return other
 if mins<val:return val
 return other
def nums(val,other=None):return val if isinstance(val,int|float) else other
def num1s(val=0,mins=1):return val if isinstance(val,int|float)and 1<=val else mins
def num0s(val=0,mins=0):return val if isinstance(val,int|float)and 0<=val else mins
def num0(val=0,mins=0):return val if isinstance(val,int|float)and 0<val else mins
def intsmin(val,mins=0,other=None):
 if not isinstance(val,int) or not isinstance(mins,int):
  return other
 if mins<val:return val
 return other
def ints(val=0,other=None):return val if isinstance(val,int) else other
def int1s(val=0,mins=1):return val if isinstance(val,int)and 1<=val else mins
def int0s(val=0,mins=0):return val if isinstance(val,int)and 0<=val else mins
def int0(val=0,mins=0):return val if isinstance(val,int)and 0<val else mins
def range_num(val,mins=None,maxs=None,others=None):
 if (not isinstance(mins,int|float)) or (not isinstance(maxs,int|float)):return others
 if maxs<mins:mins,maxs=maxs,mins
 if mins<=val<=maxs:return val
 return others
def bols(j,o=True):
 if isinstance(j,bool):return j
 return o
def parsecolor(val,other=None):
 if val is None:return other
 return Color(val).color
def wparsecolor(val,other=None):
 if val is None:return other
 return Color(val,keep_alpha=False).color