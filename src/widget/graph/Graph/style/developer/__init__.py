from .....developer import Number
def num1s(val=0,mins=1):
 if isinstance(val,int|float|Number) and 1<=val:return val
 return mins
def num0s(val=0,mins=0):
 if isinstance(val,int|float|Number)and 0<=val:
  return val
 return mins
def num0(val=0,mins=0):
 if isinstance(val,int|float|Number)and 0<val:
  return val
 return mins
def list2float(lin=None):
 if isinstance(lin,list|tuple) and len(lin)==2 and all(isinstance(i,float)for i in lin):
  return True
 return False